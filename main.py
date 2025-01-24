from modules.pdf_handler import download_pdf, extract_pdf_links
from modules.email_extractor import extract_emails_from_url
from modules.web_scraper import get_pdf_from_url
from modules.file_handler import save_pdf


def main():
    # Descargar y guardar el PDF desde una URL
    URL = 'https://minciencias.gov.co/sites/default/files/listado_resultados_finales_-_grupos_-_version_consulta.pdf'
    pdf_path = 'WEBSCRAPINGHERNANdocument.pdf'

    download_pdf(URL, pdf_path)

    # Extraer enlaces desde el PDF descargado
    links = extract_pdf_links(pdf_path)

    for link in links:
        emails = extract_emails_from_url(link)
        print(f"Correos electrónicos encontrados en {link}: {emails}")


if __name__ == "__main__":
    main()

