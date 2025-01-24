import requests

def get_pdf_from_url(url, save_path):
    """Descargar un PDF desde una URL."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF guardado en {save_path}")
    else:
        print(f"Error al descargar el PDF desde {url}")
