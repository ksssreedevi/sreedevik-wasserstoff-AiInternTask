from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Make sure to download NLTK data first: 
# Run this in terminal: `import nltk; nltk.download('punkt'); nltk.download('stopwords')`

def frequency_based_summary(text, summary_ratio=0.2):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    
    # Calculate word frequencies (ignoring stopwords)
    word_frequencies = Counter([word for word in words if word.isalnum() and word not in stop_words])
    
    # Tokenize sentences and rank them based on the frequency of their words
    sentences = sent_tokenize(text)
    sentence_scores = {sent: sum(word_frequencies[word] for word in word_tokenize(sent.lower())) for sent in sentences}
    
    # Select top sentences based on score
    num_sentences = max(1, int(len(sentences) * summary_ratio))
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    print("processing")
    # Return the summary
    return ' '.join(top_sentences)
