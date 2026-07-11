# 🎯 Smart Resume Analyzer

An intelligent web application that analyzes resumes, extracts key information, and matches them with suitable job roles using AI-powered natural language processing and machine learning.

## Features

✨ **Resume Upload & Analysis**
- Upload PDF, TXT, DOC, or DOCX resumes (Max 5MB)
- Extract and analyze resume content
- Automatic keyword extraction
- Text preprocessing and tokenization

🔍 **Manual Resume Entry**
- Paste resume content directly into the application
- Real-time analysis and processing
- Quick keyword identification

🎯 **Job Matching**
- Match resume with specific job descriptions
- Calculate compatibility percentage
- Identify common keywords between resume and job posting
- Get matching suggestions

💼 **Job Recommendations**
- Automatic job role recommendations based on resume
- Match percentage for each recommended role
- Sorted by compatibility score

## Technology Stack

### Backend
- **Framework:** Flask (Python Web Framework)
- **NLP:** NLTK (Natural Language Toolkit)
- **ML:** Scikit-learn (Machine Learning)
- **PDF Processing:** pdfplumber
- **Data Processing:** Pandas, NumPy

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Dynamic interactions
- **Axios** - HTTP client for API calls

### Database
- CSV-based job roles dataset

## Project Structure

```
Smart-Resume-Analyzer/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── test_pdf.py              # Test script for PDF reading
│
├── utils/                   # Utility modules
│   ├── __init__.py
│   ├── pdf_reader.py        # PDF extraction
│   ├── nlp_processor.py      # NLP processing & keyword extraction
│   ├── similarity.py         # Text similarity calculation
│   ├── recommender.py        # Job recommendations
│   └── ai.py                 # AI analysis functions
│
├── static/                  # Static files
│   └── style.css            # Stylesheet
│
├── templets/                # HTML templates
│   ├── index.html           # Main page
│   └── result.html          # Results page
│
├── dataset/                 # Data files
│   └── job_roles.csv        # Job roles database
│
└── uploads/                 # User uploaded files (temporary)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone/Download the project**
   ```bash
   cd Smart-Resume-Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to: `http://localhost:5000`

## Usage Guide

### 1. Upload Resume
- Click the "Upload Resume" tab
- Drag and drop a PDF/DOC/DOCX file or click to browse
- The system will automatically analyze your resume

### 2. Manual Entry
- Click the "Manual Entry" tab
- Paste your resume text
- Click "Analyze Resume"

### 3. Job Matching
- Click the "Job Matcher" tab
- Paste your resume text
- Paste the job description
- Click "Calculate Match" to see compatibility

## API Endpoints

### POST /upload
Upload a resume file for analysis
- **File:** resume (PDF, TXT, DOC, DOCX)
- **Response:** Analysis data with keywords and recommendations

### POST /analyze
Analyze resume text
- **Body:** `{ "resume_text": "..." }`
- **Response:** Analysis results

### POST /match
Match resume with job description
- **Body:** `{ "resume_text": "...", "job_description": "..." }`
- **Response:** Match percentage and keyword comparison

### GET /health
Health check endpoint
- **Response:** `{ "status": "ok", "message": "..." }`

## How It Works

1. **Resume Extraction**
   - Extracts text from uploaded PDF/documents
   - Handles various document formats

2. **Text Processing**
   - Tokenizes text into individual words
   - Removes common stopwords
   - Converts to lowercase for normalization

3. **Keyword Extraction**
   - Uses frequency analysis to identify important terms
   - Extracts top 15 keywords from resume

4. **Job Matching**
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
   - Calculates cosine similarity between resume and job description
   - Returns match percentage (0-100%)

5. **Recommendations**
   - Compares resume against job roles in database
   - Ranks by compatibility score
   - Returns top 5 recommended roles

## Configuration

Edit `app.py` to modify:
- **UPLOAD_FOLDER** - Where uploaded files are stored
- **ALLOWED_EXTENSIONS** - Supported file types
- **MAX_FILE_SIZE** - Maximum upload size (default: 5MB)
- **DEBUG MODE** - Set to `False` for production

## Error Handling

The application includes comprehensive error handling:
- File type validation
- File size checking
- Empty file detection
- PDF reading errors
- Text processing exceptions

All errors return user-friendly messages via JSON response.

## Performance

- Fast resume analysis (< 2 seconds for most resumes)
- Efficient keyword extraction
- Optimized text similarity calculation
- Suitable for 1000+ job role matching

## Future Enhancements

🚀 Planned features:
- User authentication and profiles
- Save analysis history
- Advanced skills extraction
- Salary predictions
- LinkedIn integration
- Multiple language support
- Export reports (PDF)
- Skill gap analysis
- Interview preparation suggestions

## Troubleshooting

### Port 5000 Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Dependencies Not Installing
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### NLTK Data Missing
The app automatically downloads required NLTK data on first run.
If issues persist:
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## License

This project is open source and available for educational purposes.

## Author

Created as an AI-powered resume analysis tool.

## Support

For issues or suggestions, please check the application logs or contact support.

---

**Made with ❤️ using Flask, NLP, and Machine Learning**
