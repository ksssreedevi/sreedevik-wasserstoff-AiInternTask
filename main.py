from summarization import frequency_based_summary
from keywords import extract_keywords
from mongodb import connect_mongodb, insert_pdf_data
from pipeline import process_pdf_folder

def process_and_store_pdfs(folder_path):
    collection = connect_mongodb()
    texts = process_pdf_folder(folder_path)
    corpus = list(texts)  # Use all PDFs as a corpus for keyword extraction

    for text in texts:
        summary = frequency_based_summary(text)
        keywords = extract_keywords(text, corpus)
        
        # Insert into MongoDB
        insert_pdf_data(collection, 'example.pdf', text, summary, keywords)

if __name__ == "__main__":
    folder_path = 'pdfs/'
    process_and_store_pdfs(folder_path)
