from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import pathlib
from app.gemini_client import generate_section_gemini
from app.latex_utils import merge_into_template, compile_pdf
import os


app = FastAPI()


# Serve static files for frontend and /static
frontend_path = pathlib.Path(__file__).parent.parent / "frontend"
static_path = pathlib.Path(__file__).parent.parent / "static"
app.mount("/frontend", StaticFiles(directory=str(frontend_path)), name="frontend")
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Serve index.html at root
@app.get("/")
def serve_index():
    index_path = frontend_path / "index.html"
    with open(index_path, encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.post("/generate")
def generate_paper(title: str = Form(...)):
    # Generate all content using Groq API and the title
    # Authors
    authors_prompt = (
        f"Generate a realistic list of IEEE-style authors and affiliations for a research paper titled '{title}'. "
        f"Format using LaTeX IEEE author blocks. Make it look like a real multi-author international collaboration."
    )
    authors = generate_section_gemini(authors_prompt)
    if authors.startswith("ERROR:"):
        return {"latex_code": f"% {authors}\n"}
    abstract_prompt = (
        f"Generate an IEEE-compliant abstract for a research paper titled '{title}'. Format using LaTeX. "
        f"Make it 100% humanized and original, no plagiarism."
    )
    abstract = generate_section_gemini(abstract_prompt)
    if abstract.startswith("ERROR:"):
        return {"latex_code": f"% {abstract}\n"}
    keywords_prompt = (
        f"Generate 5-7 IEEE-style keywords for a research paper titled '{title}'. Format as comma separated."
    )
    keywords = generate_section_gemini(keywords_prompt)
    if keywords.startswith("ERROR:"):
        return {"latex_code": f"% {keywords}\n"}
    section_names = [
        "Introduction", "Related Work", "Methodology", "Results", "Discussion", "Conclusion"
    ]
    import re
    section_texts = []
    for i, section in enumerate(section_names):
        prompt = (
            f"Write a detailed, original, IEEE-compliant research paper section titled '{section}' for the topic '{title}'. "
            f"Format using LaTeX. Make it 100% humanized, non-plagiarized, and long enough to fill at least 1.5 pages of IEEE conference format. Leave placeholders for images as \\includegraphics{{image{i+1}}}. "
            f"Do not repeat section headings."
        )
        section_content = generate_section_gemini(prompt)
        if section_content.startswith("ERROR:"):
            return {"latex_code": f"% {section_content}\n"}
        # Remove any LaTeX section heading from Gemini output
        section_content = re.sub(r"\\section\*?\{.*?\}\s*", "", section_content, flags=re.IGNORECASE)
        section_texts.append(f"\\section{{{section}}}\n" + section_content)
    sections_latex = "\n".join(section_texts)
    ack_prompt = (
        f"Generate a short IEEE-style acknowledgment for a research paper titled '{title}'. Format using LaTeX."
    )
    acknowledgment = generate_section_gemini(ack_prompt)
    if acknowledgment.startswith("ERROR:"):
        return {"latex_code": f"% {acknowledgment}\n"}
    ref_prompt = (
        f"Generate 15 IEEE-style references for a research paper titled '{title}'. Format using LaTeX bibliography. Only use real, relevant references."
    )
    references = generate_section_gemini(ref_prompt)
    if references.startswith("ERROR:"):
        return {"latex_code": f"% {references}\n"}
    latex_code = merge_into_template(title, authors, keywords, abstract, sections_latex, acknowledgment, references)
    return {"latex_code": latex_code}

@app.get("/download/{file_type}")
def download_file(file_type: str):
    base_path = os.path.join(os.path.dirname(__file__), '..', 'generated')
    if file_type == "tex":
        return FileResponse(os.path.join(base_path, "paper.tex"), media_type="application/x-tex")
    elif file_type == "pdf":
        return FileResponse(os.path.join(base_path, "paper.pdf"), media_type="application/pdf")
    else:
        return HTMLResponse("File not found", status_code=404)
