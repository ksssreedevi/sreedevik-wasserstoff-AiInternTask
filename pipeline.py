import os
import PyPDF2
from concurrent.futures import ThreadPoolExecutor

# Function to read PDF and extract text
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function to process a folder of PDFs
def process_pdf_folder(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    with ThreadPoolExecutor() as executor:
        results = executor.map(extract_text_from_pdf, [os.path.join(folder_path, pdf) for pdf in pdf_files])
    return results

if __name__ == "__main__":
    print("processing")
    folder_path = 'pdfs/'
    texts = process_pdf_folder(folder_path)
    for text in texts:
        print(text[:500])  # Print first 500 characters of each PDF text
