"""
Similarity calculation module for comparing resume with job descriptions.
Uses pure Python implementation without scikit-learn.
"""
from collections import Counter
import math


def get_words(text):
    """Extract and clean words from text."""
    if not text:
        return []
    # Convert to lowercase, remove special characters, split into words
    words = text.lower().split()
    # Filter out empty strings and very short words
    words = [w.strip('.,!?;:\'"()[]{}') for w in words if len(w.strip('.,!?;:\'"()[]{}')) > 2]
    return words


def calculate_similarity(text1, text2):
    """
    Calculate similarity between two texts using word frequency.
    Returns a score between 0 and 1.
    
    Uses Jaccard similarity + word frequency weighting.
    """
    if not text1 or not text2:
        return 0.0
    
    try:
        words1 = get_words(text1)
        words2 = get_words(text2)
        
        if not words1 or not words2:
            return 0.0
        
        # Count word frequencies
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        
        # Find common words
        common_words = set(freq1.keys()) & set(freq2.keys())
        
        if not common_words:
            return 0.0
        
        # Calculate weighted similarity
        common_score = sum(min(freq1[w], freq2[w]) for w in common_words)
        total_score = sum(freq1.values()) + sum(freq2.values())
        
        # Normalize to 0-1 range
        similarity = (2 * common_score) / total_score if total_score > 0 else 0.0
        
        return round(float(similarity), 3)
    
    except Exception as e:
        print(f"Error calculating similarity: {str(e)}")
        return 0.0


def get_match_percentage(resume_text, job_description):
    """
    Get percentage match between resume and job description (0-100).
    """
    similarity_score = calculate_similarity(resume_text, job_description)
    match_percentage = similarity_score * 100
    return round(match_percentage, 2)
