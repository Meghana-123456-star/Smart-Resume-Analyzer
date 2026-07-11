import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def preprocess_text(text):
    """
    Preprocess text by tokenizing and removing stopwords.
    """
    try:
        tokens = word_tokenize(text.lower())
    except:
        # Fallback to simple split if tokenizer fails
        tokens = text.lower().split()
    
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return filtered_tokens


def extract_keywords(text, num_keywords=10):
    """
    Extract top keywords from text.
    """
    from nltk import FreqDist
    
    tokens = preprocess_text(text)
    if not tokens:
        return []
    
    freq_dist = FreqDist(tokens)
    keywords = freq_dist.most_common(num_keywords)
    return [word for word, _ in keywords]
