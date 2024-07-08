import PyPDF2

def open_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            
            if pdf_reader.isEncrypted:
                pdf_reader.decrypt('')
            
            num_pages = pdf_reader.getNumPages()
            print(f'The PDF file has {num_pages} pages.')

            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                print(f'Page {page_num + 1}:')
                print(text)
                print('---')
    except Exception as e:
        print(f'An error occurred: {e}')

pdf_path = 'path/to/your/pdf_file.pdf'
open_pdf(pdf_path)
