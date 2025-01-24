Project Overview:
This project performs several tasks related to web scraping and data extraction from PDFs, including:

Downloading a PDF: The project downloads a PDF file from a given URL and saves it locally on the user's system.

Extracting Links from PDFs: It opens the downloaded PDF file and extracts any embedded links (URLs) from the annotations present in the document.

Extracting Email Addresses: For each extracted URL, the project performs a web scraping operation to retrieve email addresses present on the linked web pages. It uses regular expressions to identify emails in the text of the page.

Organizing Code into Modular Structure: The project is organized into separate modules for each distinct functionality. This structure ensures that the code is easier to maintain and extend.

Modules:
main.py: This is the entry point of the project. It orchestrates the flow of downloading the PDF, extracting links from it, and scraping emails from those links.

pdf_handler.py: This module is responsible for downloading the PDF from a specified URL and extracting links (URLs) from the PDF annotations.

email_extractor.py: It extracts email addresses from the text of web pages linked from the PDF annotations using BeautifulSoup and regular expressions.

web_scraper.py: A module for web scraping functionalities. It includes the function to download PDFs from a URL.

file_handler.py: A module meant for handling files, such as CSV or Excel, though it can be expanded for more file operations as needed.

Dependencies:
The project uses several Python libraries to handle requests, web scraping, and PDF processing. The key dependencies are:

requests (for making HTTP requests)
beautifulsoup4 (for web scraping and extracting email addresses)
pdfplumber (for working with PDF files)
openpyxl (for handling Excel files)
pandas (for working with data in tabular form)
numpy (for numerical operations)
Key Features:
Web Scraping: Extracts emails from web pages linked in the PDF.
PDF Parsing: Downloads and parses PDF documents to extract links.
Modular Design: The code is organized into different modules for easy maintenance and readability.
This project is useful for automating the process of downloading PDFs, extracting URLs, and scraping emails from those URLs, and it can be extended for other types of web scraping tasks or data extraction workflows.
