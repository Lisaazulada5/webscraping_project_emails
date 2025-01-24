import requests
import pandas as pd
import csv
import numpy as np
import openpyxl
from bs4 import BeautifulSoup, NavigableString, Tag
from datetime import datetime
import json
import requests
#import fitz  # PyMuPDF
import PyPDF2
import re

"""WebScraping Ratings"""

import requests

# URL del PDF
URL = 'https://minciencias.gov.co/sites/default/files/listado_resultados_finales_-_grupos_-_version_consulta.pdf'

# Descargar el PDF
response = requests.get(URL)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    with open("C:/Users/licit/OneDrive/Documentos/Proyectos python/WEBSCRAPINGHERNANdocument.pdf", "wb") as file:
        file.write(response.content)
else:
    print(f"Error al acceder al PDF: {response.status_code}")


import pdfplumber

# Ruta al archivo PDF descargado
pdf_path = 'C:/Users/licit/OneDrive/Documentos/Proyectos python/WEBSCRAPINGHERNANdocument.pdf'

# Abrir el PDF y extraer texto y enlaces
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        annotations = page.annots

        #print("\nEnlaces encontrados en la página:")
        #for annot in annotations:
        #    if annot['uri']:
        #        print(f"Enlace: {annot['uri']}")


# Función para extraer direcciones de correo electrónico de una página web
def extract_emails_from_url(url):
    page_response = requests.get(url)
    if page_response.status_code == 200:
        soup = BeautifulSoup(page_response.text, 'html.parser')
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
        return emails
    else:
        print(f"Error al acceder a la URL: {url}")
        return set()

# Abrir el PDF y extraer enlaces
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        annotations = page.annots
        print(f"\nEnlaces encontrados en la página {page_num + 1}:")
        for annot in annotations:
            if annot['uri']:
                link = annot['uri']
                print(f"Enlace: {link}")
                emails = extract_emails_from_url(link)
                print(f"Correos electrónicos encontrados: {emails}")