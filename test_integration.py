"""
Integration tests for Smart Resume Analyzer
Tests all core functionality
"""

import sys
from utils.nlp_processor import extract_keywords, preprocess_text
from utils.similarity import calculate_similarity, get_match_percentage
from utils.recommender import recommend_jobs
from utils.ai import analyze_resume, analyze_job_description

def test_nlp_processor():
    """Test NLP processor functions"""
    print("\n📝 Testing NLP Processor...")
    
    sample_text = "Python Developer with 5 years of experience in web development and machine learning"
    
    # Test preprocessing
    tokens = preprocess_text(sample_text)
    print(f"  ✓ Text preprocessing: {len(tokens)} tokens extracted")
    
    # Test keyword extraction
    keywords = extract_keywords(sample_text, num_keywords=5)
    print(f"  ✓ Keyword extraction: {keywords}")

def test_similarity():
    """Test similarity calculation"""
    print("\n🔍 Testing Similarity Calculation...")
    
    resume = "Python developer with machine learning expertise and 5 years of experience"
    job_desc = "Seeking Python developer with machine learning skills and experience"
    
    similarity = calculate_similarity(resume, job_desc)
    print(f"  ✓ Text similarity: {similarity}")
    
    match_percentage = get_match_percentage(resume, job_desc)
    print(f"  ✓ Match percentage: {match_percentage}%")

def test_ai_analysis():
    """Test AI analysis functions"""
    print("\n🤖 Testing AI Analysis...")
    
    resume_text = "Senior Software Engineer with 10 years in Python, Java, and cloud technologies"
    
    analysis = analyze_resume(resume_text)
    print(f"  ✓ Resume analysis: {analysis['words_count']} words, {analysis['text_length']} characters")

def test_recommender():
    """Test job recommendations"""
    print("\n💼 Testing Job Recommendations...")
    
    resume_text = "Python Developer with Django and React experience, 3 years background in full-stack development"
    
    recommendations = recommend_jobs(resume_text, top_n=3)
    print(f"  ✓ Top {len(recommendations)} job recommendations generated:")
    for i, rec in enumerate(recommendations, 1):
        print(f"    {i}. {rec['job_title']} - Match: {rec['match_score']}%")

def main():
    """Run all tests"""
    print("=" * 50)
    print("🧪 Smart Resume Analyzer - Integration Tests")
    print("=" * 50)
    
    try:
        test_nlp_processor()
        test_similarity()
        test_ai_analysis()
        test_recommender()
        
        print("\n" + "=" * 50)
        print("✅ All tests passed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
