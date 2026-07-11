"""
Similarity calculation module for comparing resume with job descriptions.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(text1, text2):
    """
    Calculate similarity between two texts using TF-IDF and cosine similarity.
    Returns a score between 0 and 1.
    """
    if not text1 or not text2:
        return 0.0
    
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    
    try:
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return round(float(similarity), 3)
    except Exception as e:
        print(f"Error calculating similarity: {str(e)}")
        return 0.0


def get_match_percentage(resume_text, job_description):
    """
    Get percentage match between resume and job description.
    """
    similarity_score = calculate_similarity(resume_text, job_description)
    match_percentage = similarity_score * 100
    return round(match_percentage, 2)
