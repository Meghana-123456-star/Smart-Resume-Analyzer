# Smart Resume Analyzer Configuration
# This file contains additional configuration settings

import os

# Flask Configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = FLASK_ENV == 'development'
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Upload Configuration
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}

# NLP Configuration
NLP_MAX_KEYWORDS = 15
NLP_BATCH_SIZE = 100

# Recommender Configuration
RECOMMENDATIONS_COUNT = 5
MATCH_THRESHOLD = 0.3

# Database Configuration (for future use)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
