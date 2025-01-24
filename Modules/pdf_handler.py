import requests
import pdfplumber

def download_pdf(url, path):
    """Descargar el PDF desde una URL y guardarlo localmente."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as file:
            file.write(response.content)
        print(f"PDF descargado y guardado en {path}")
    else:
        print(f"Error al acceder al PDF: {response.status_code}")

def extract_pdf_links(pdf_path):
    """Extraer enlaces desde un archivo PDF."""
    links = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            annotations = page.annots
            for annot in annotations:
                if annot['uri']:
                    links.append(annot['uri'])
    return links
