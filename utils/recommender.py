"""
Recommender system for suggesting suitable jobs based on resume.
Uses pure Python CSV reading without pandas.
"""
import csv
from utils.similarity import get_match_percentage


def load_job_roles(csv_path):
    """
    Load job roles from CSV file using pure Python.
    Returns list of dictionaries with job data.
    """
    try:
        jobs = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                jobs.append(row)
        return jobs
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found")
        return []
    except Exception as e:
        print(f"Error loading job roles: {str(e)}")
        return []


def recommend_jobs(resume_text, csv_path="dataset/job_roles.csv", top_n=5):
    """
    Recommend top N job roles based on resume similarity.
    """
    jobs = load_job_roles(csv_path)
    
    if not jobs:
        return []
    
    recommendations = []
    
    for job in jobs:
        # Handle different column names
        job_title = None
        job_description = ''
        
        # Try to find role/title column
        for col in ['Role', 'role', 'title', 'Title', 'Job Title', 'job_title']:
            if col in job:
                job_title = job[col]
                break
        
        # Try to find skills/description column
        for col in ['Skills', 'skills', 'description', 'Description', 'Job Description', 'job_description']:
            if col in job:
                job_description = job[col]
                break
        
        if not job_title:
            job_title = 'Unknown Role'
        
        # Calculate match score
        match_score = get_match_percentage(resume_text, job_description)
        
        recommendations.append({
            'job_title': job_title,
            'match_score': match_score,
            'description': job_description
        })
    
    # Sort by match score in descending order
    recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    
    return recommendations[:top_n]
