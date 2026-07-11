import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


def preprocess_text(text):
    """
    Preprocess text by tokenizing and removing stopwords.
    """
    try:
        tokens = word_tokenize(text.lower())
    except Exception as e:
        # Fallback to simple split if tokenizer fails
        print(f"Tokenizer warning: {e}, using simple split")
        tokens = text.lower().split()
    
    try:
        stop_words = set(stopwords.words('english'))
    except:
        # Fallback: use common English stopwords if NLTK stopwords not available
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'was', 'are', 'were', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how'}
    
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
