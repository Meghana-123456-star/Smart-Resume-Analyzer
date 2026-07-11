"""
Smart Resume Analyzer - Main Flask Application
Analyzes resumes and matches them with suitable job roles
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import sys
from werkzeug.utils import secure_filename

# Configure app before imports that need it
app = Flask(__name__, template_folder='templates')

# Configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
app.config['DEBUG'] = os.environ.get('FLASK_ENV', 'development') == 'development'

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Download NLTK data on startup (for Render deployment)
try:
    import nltk
    print("Downloading NLTK data...")
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    print("✓ NLTK data ready")
except Exception as e:
    print(f"Warning: Could not download NLTK data: {e}")

# Now import utilities
try:
    from utils.pdf_reader import extract_text_from_pdf
    from utils.nlp_processor import extract_keywords
    from utils.similarity import get_match_percentage
    from utils.recommender import recommend_jobs
    from utils.ai import analyze_resume, analyze_job_description
    print("✓ All modules loaded successfully")
except ImportError as e:
    print(f"Error importing modules: {e}", file=sys.stderr)
    sys.exit(1)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Home page - resume upload."""
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering index: {e}")
        return jsonify({'error': f'Error loading page: {str(e)}'}), 500


@app.route('/upload', methods=['POST'])
def upload_resume():
    """Handle resume upload and analysis."""
    try:
        # Check if file is in request
        if 'resume' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['resume']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check file extension
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: PDF, TXT, DOC, DOCX'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from resume
        try:
            if filename.endswith('.pdf'):
                resume_text = extract_text_from_pdf(filepath)
            else:
                with open(filepath, 'r', encoding='utf-8') as f:
                    resume_text = f.read()
        except Exception as e:
            return jsonify({'error': f'Error reading file: {str(e)}'}), 400
        
        if not resume_text or len(resume_text.strip()) < 10:
            return jsonify({'error': 'Resume appears to be empty or invalid'}), 400
        
        # Analyze resume
        try:
            analysis = analyze_resume(resume_text)
            keywords = extract_keywords(resume_text, num_keywords=15)
            recommendations = recommend_jobs(resume_text)
        except Exception as e:
            return jsonify({'error': f'Error analyzing resume: {str(e)}'}), 500
        
        # Prepare response data
        result_data = {
            'filename': filename,
            'resume_text': resume_text[:500] + '...' if len(resume_text) > 500 else resume_text,
            'full_text': resume_text,
            'analysis': analysis,
            'keywords': keywords,
            'recommendations': recommendations
        }
        
        return jsonify(result_data), 200
    
    except Exception as e:
        print(f"Upload error: {e}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/analyze', methods=['POST'])
def analyze_manual():
    """Analyze resume text provided manually."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        resume_text = data.get('resume_text', '').strip()
        
        if not resume_text or len(resume_text) < 10:
            return jsonify({'error': 'Please provide resume text'}), 400
        
        # Analyze resume
        try:
            analysis = analyze_resume(resume_text)
            keywords = extract_keywords(resume_text, num_keywords=15)
            recommendations = recommend_jobs(resume_text)
        except Exception as e:
            return jsonify({'error': f'Error analyzing resume: {str(e)}'}), 500
        
        result_data = {
            'analysis': analysis,
            'keywords': keywords,
            'recommendations': recommendations
        }
        
        return jsonify(result_data), 200
    
    except Exception as e:
        print(f"Analyze error: {e}")
        return jsonify({'error': f'Error: {str(e)}'}), 500


@app.route('/match', methods=['POST'])
def match_resume():
    """Match resume with specific job description."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        resume_text = data.get('resume_text', '').strip()
        job_description = data.get('job_description', '').strip()
        
        if not resume_text or len(resume_text) < 10:
            return jsonify({'error': 'Please provide resume text'}), 400
        
        if not job_description or len(job_description) < 10:
            return jsonify({'error': 'Please provide job description'}), 400
        
        try:
            # Calculate match percentage
            match_percentage = get_match_percentage(resume_text, job_description)
            
            # Extract keywords from both texts
            resume_keywords = extract_keywords(resume_text, num_keywords=10)
            job_keywords = extract_keywords(job_description, num_keywords=10)
            
            # Find common keywords
            common_keywords = list(set(resume_keywords) & set(job_keywords))
        except Exception as e:
            return jsonify({'error': f'Error matching: {str(e)}'}), 500
        
        result_data = {
            'match_percentage': match_percentage,
            'resume_keywords': resume_keywords,
            'job_keywords': job_keywords,
            'common_keywords': common_keywords,
            'match_status': 'Excellent' if match_percentage >= 80 else 'Good' if match_percentage >= 60 else 'Fair' if match_percentage >= 40 else 'Poor'
        }
        
        return jsonify(result_data), 200
    
    except Exception as e:
        print(f"Match error: {e}")
        return jsonify({'error': f'Error: {str(e)}'}), 500


@app.route('/results')
def results():
    """Results page."""
    return render_template('result.html')


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok', 'message': 'Smart Resume Analyzer is running'}), 200


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('index.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    flask_env = os.environ.get('FLASK_ENV', 'development')
    debug = flask_env == 'development'
    
    print("\n" + "="*60)
    print("🚀 Starting Smart Resume Analyzer")
    print("="*60)
    print(f"Environment: {flask_env}")
    print(f"Debug: {debug}")
    print(f"Port: {port}")
    print(f"Upload folder: {app.config['UPLOAD_FOLDER']}")
    print("="*60)
    
    if flask_env == 'production':
        print("⚠️  Production mode - Debug is OFF")
    else:
        print("ℹ️  Development mode")
    
    print("\n✓ Starting Flask application...")
    print("="*60 + "\n")
    
    app.run(debug=debug, host='0.0.0.0', port=port, use_reloader=False)
