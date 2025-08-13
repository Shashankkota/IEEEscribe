import subprocess
import tempfile
import os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'ieee_template.tex')
GENERATED_DIR = os.path.join(os.path.dirname(__file__), '..', 'generated')

# Merge generated content into LaTeX template
def merge_into_template(title, authors, keywords, abstract, sections, acknowledgment, references):
    with open(TEMPLATE_PATH, encoding='utf-8') as f:
        template = f.read()
    template = template.replace("__TITLE__", title)
    template = template.replace("__AUTHORS__", authors)
    template = template.replace("__KEYWORDS__", keywords)
    template = template.replace("__ABSTRACT__", abstract)
    template = template.replace("__SECTIONS__", sections)
    template = template.replace("__ACKNOWLEDGMENT__", acknowledgment)
    template = template.replace("__REFERENCES__", references)
    return template

# Compile LaTeX to PDF using pdflatex
def compile_pdf(latex_code: str, output_name: str = "paper") -> str:
    tex_path = os.path.join(GENERATED_DIR, f"{output_name}.tex")
    pdf_path = os.path.join(GENERATED_DIR, f"{output_name}.pdf")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_code)
    # Run pdflatex twice for references
    subprocess.run(["pdflatex", "-output-directory", GENERATED_DIR, tex_path], check=True)
    subprocess.run(["pdflatex", "-output-directory", GENERATED_DIR, tex_path], check=True)
    return pdf_path
