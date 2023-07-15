from pypdf import PdfReader
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf():
    pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/docs-pytest-org-en-latest.pdf'))
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    assert number_of_pages == 412
    assert "Release 0.1" in text
    print(page)
    print(number_of_pages)
    print(text)
