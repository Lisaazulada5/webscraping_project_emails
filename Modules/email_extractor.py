import requests
import re
from bs4 import BeautifulSoup

def extract_emails_from_url(url):
    """Extraer direcciones de correo electrónico de una página web."""
    page_response = requests.get(url)
    if page_response.status_code == 200:
        soup = BeautifulSoup(page_response.text, 'html.parser')
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
        return emails
    else:
        print(f"Error al acceder a la URL: {url}")
        return set()
