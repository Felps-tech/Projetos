import pydf

pdf = pydf.generate_pdf('<h1>Meu pdf gerado com python</h1>')
with open('meu_pdf_python.pdf','wb') as f:
    f.write(pdf)
