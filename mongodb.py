from pymongo import MongoClient

# Connect to MongoDB
def connect_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['pdf_database']
    collection = db['pdf_data']
    return collection

# Insert document metadata and results into MongoDB
def insert_pdf_data(collection, pdf_name, text, summary, keywords):
    document = {
        'pdf_name': pdf_name,
        'text': text,
        'summary': summary,
        'keywords': keywords
    }
    collection.insert_one(document)
