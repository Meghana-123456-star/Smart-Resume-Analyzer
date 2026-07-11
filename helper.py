#!/usr/bin/env python3
"""
Smart Resume Analyzer - Helper Script
Provides utility functions and commands
"""

import os
import sys
import shutil
from pathlib import Path

def clear_uploads():
    """Clear the uploads folder"""
    uploads_dir = Path('uploads')
    if uploads_dir.exists():
        for file in uploads_dir.glob('*'):
            if file.is_file():
                file.unlink()
        print("✓ Uploads folder cleared")
    else:
        print("✗ Uploads folder not found")

def create_sample_resume():
    """Create a sample resume file"""
    sample_resume = """
JOHN DOE
Senior Software Engineer

CONTACT INFORMATION
Email: john.doe@example.com
Phone: (555) 123-4567
LinkedIn: linkedin.com/in/johndoe

PROFESSIONAL SUMMARY
Experienced Senior Software Engineer with 8+ years of expertise in full-stack web development, 
cloud architecture, and team leadership. Proven track record of building scalable applications 
using Python, JavaScript, and modern frameworks.

TECHNICAL SKILLS
Programming Languages: Python, JavaScript, Java, SQL
Web Frameworks: Flask, Django, React, Node.js
Databases: PostgreSQL, MongoDB, Redis
Cloud Platforms: AWS, Google Cloud, Azure
Tools & Technologies: Docker, Kubernetes, Git, Jenkins, CI/CD
Machine Learning: TensorFlow, Scikit-learn, NLP

PROFESSIONAL EXPERIENCE
Senior Software Engineer
Tech Company Inc. | 2020 - Present
- Led development of microservices architecture serving 1M+ users
- Implemented machine learning pipeline for recommendation system
- Mentored team of 5 junior developers
- Reduced API response time by 40% through optimization

Full Stack Developer
Digital Solutions Ltd. | 2018 - 2020
- Developed full-stack web applications using React and Flask
- Implemented real-time data processing system
- Managed database optimization and scaling
- Collaborated with cross-functional teams

Junior Developer
StartUp Co. | 2016 - 2018
- Built responsive web interfaces using JavaScript
- Contributed to backend services in Python
- Participated in agile development processes

EDUCATION
Bachelor of Science in Computer Science
State University | 2016

CERTIFICATIONS
- AWS Solutions Architect Associate
- Certified Kubernetes Administrator

PROJECTS
Smart Resume Analyzer
- Built full-stack application for resume analysis using Flask and NLP
- Implemented machine learning for job matching
- Achieved 90% accuracy in skill extraction

E-Commerce Platform
- Developed scalable e-commerce platform using React and Django
- Integrated payment processing and inventory management
- Handled 10,000+ concurrent users

LANGUAGES
- English (Fluent)
- Spanish (Intermediate)
"""
    
    with open('uploads/sample_resume.txt', 'w') as f:
        f.write(sample_resume.strip())
    print("✓ Sample resume created: uploads/sample_resume.txt")

def show_stats():
    """Show project statistics"""
    print("\n" + "="*50)
    print("PROJECT STATISTICS")
    print("="*50)
    
    files_count = 0
    lines_count = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden and cache directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for file in files:
            if file.endswith('.py'):
                files_count += 1
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        lines_count += len(f.readlines())
                except:
                    pass
    
    print(f"\nPython Files: {files_count}")
    print(f"Lines of Code: {lines_count}")
    print("\nProject Structure:")
    print("  ├── Backend: Flask + Python")
    print("  ├── Frontend: HTML5 + CSS3 + JavaScript")
    print("  ├── NLP: NLTK + Scikit-learn")
    print("  ├── Database: CSV (CSV-based)")
    print("  └── Storage: File uploads")
    print("\n" + "="*50)

def install_dependencies():
    """Install or upgrade dependencies"""
    print("\nInstalling dependencies...")
    os.system('pip install -r requirements.txt -U')
    print("✓ Dependencies installed")

def run_tests():
    """Run integration tests"""
    print("\nRunning integration tests...")
    os.system('python test_integration.py')

def main():
    """Main menu"""
    commands = {
        '1': ('Clear uploads folder', clear_uploads),
        '2': ('Create sample resume', create_sample_resume),
        '3': ('Show project stats', show_stats),
        '4': ('Install/upgrade dependencies', install_dependencies),
        '5': ('Run tests', run_tests),
        '0': ('Exit', lambda: None)
    }
    
    while True:
        print("\n" + "="*50)
        print("SMART RESUME ANALYZER - HELPER")
        print("="*50)
        
        for key, (desc, _) in commands.items():
            print(f"{key}. {desc}")
        
        choice = input("\nSelect option: ").strip()
        
        if choice in commands:
            if choice == '0':
                print("Goodbye! 👋")
                break
            else:
                commands[choice][1]()
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
