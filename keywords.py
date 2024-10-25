from collections import Counter
from math import log

def compute_tf(text):
    words = text.split()
    tf = Counter(words)
    total_words = len(words)
    return {word: count / total_words for word, count in tf.items()}

def compute_idf(corpus):
    idf = {}
    total_docs = len(corpus)
    all_words = set([word for doc in corpus for word in doc.split()])
    
    for word in all_words:
        doc_count = sum(1 for doc in corpus if word in doc.split())
        idf[word] = log(total_docs / (1 + doc_count))
    
    return idf

def extract_keywords(text, corpus, num_keywords=10):
    tf = compute_tf(text)
    idf = compute_idf(corpus)
    tf_idf = {word: tf[word] * idf[word] for word in tf.keys()}
    
    # Sort by tf-idf scores and return top keywords
    return sorted(tf_idf, key=tf_idf.get, reverse=True)[:num_keywords]
