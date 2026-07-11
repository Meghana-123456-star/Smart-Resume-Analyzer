"""
Recommender system for suggesting suitable jobs based on resume.
"""
import pandas as pd
from utils.similarity import get_match_percentage


def load_job_roles(csv_path):
    """
    Load job roles from CSV file.
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found")
        return None
    except Exception as e:
        print(f"Error loading job roles: {str(e)}")
        return None


def recommend_jobs(resume_text, csv_path="dataset/job_roles.csv", top_n=5):
    """
    Recommend top N job roles based on resume similarity.
    """
    job_roles_df = load_job_roles(csv_path)
    
    if job_roles_df is None or job_roles_df.empty:
        return []
    
    recommendations = []
    
    # Handle different column names
    role_col = 'Role' if 'Role' in job_roles_df.columns else 'title' if 'title' in job_roles_df.columns else job_roles_df.columns[0]
    skills_col = 'Skills' if 'Skills' in job_roles_df.columns else 'description' if 'description' in job_roles_df.columns else (job_roles_df.columns[1] if len(job_roles_df.columns) > 1 else None)
    
    for idx, row in job_roles_df.iterrows():
        job_title = str(row[role_col]) if role_col in row.index else 'N/A'
        job_description = str(row[skills_col]) if skills_col and skills_col in row.index else ''
        
        match_score = get_match_percentage(resume_text, job_description)
        
        recommendations.append({
            'job_title': job_title,
            'match_score': match_score,
            'description': job_description
        })
    
    # Sort by match score in descending order
    recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    
    return recommendations[:top_n]
