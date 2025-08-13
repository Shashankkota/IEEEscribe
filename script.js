document.getElementById('paperForm').onsubmit = async function(e) {
    e.preventDefault();
    document.getElementById('status').textContent = 'Generating paper...';
    document.getElementById('latexOutput').style.display = 'none';
    const formData = new FormData(this);
    const response = await fetch('/generate', {
        method: 'POST',
        body: formData
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById('status').textContent = 'Paper generated!';
        document.getElementById('latexCode').value = data.latex_code;
        document.getElementById('latexOutput').style.display = 'block';
    } else {
        document.getElementById('status').textContent = 'Error generating paper.';
    }
};

document.getElementById('downloadLatex').onclick = function() {
    const latex = document.getElementById('latexCode').value;
    const blob = new Blob([latex], {type: 'text/x-tex'});
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'paper.tex';
    link.click();
};
