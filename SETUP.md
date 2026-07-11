# Smart Resume Analyzer - Setup Instructions

## Quick Start

### 1. Prerequisites
- Python 3.8+
- pip
- Git (optional)

### 2. Installation

#### Step 1: Navigate to project directory
```bash
cd Smart-Resume-Analyzer
```

#### Step 2: Create virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Run the application
```bash
python app.py
```

#### Step 5: Open in browser
Navigate to: **http://localhost:5000**

---

## Features Overview

### 📤 Upload Resume
1. Drag and drop a PDF, DOC, or DOCX file
2. System automatically extracts and analyzes content
3. View keywords and job recommendations

### ✏️ Manual Entry
1. Paste resume text directly
2. Click "Analyze Resume"
3. Get instant analysis

### 🎯 Job Matcher
1. Paste resume and job description
2. Get compatibility score
3. See matching keywords

---

## Project Structure

```
Smart-Resume-Analyzer/
├── app.py                 # Main Flask app
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── SETUP.md              # This file
│
├── utils/                 # Python modules
│   ├── pdf_reader.py      # PDF extraction
│   ├── nlp_processor.py   # Text processing
│   ├── similarity.py      # Similarity calculation
│   ├── recommender.py     # Job recommendations
│   └── ai.py              # AI analysis
│
├── static/
│   └── style.css          # Styling
│
├── templets/
│   ├── index.html         # Home page
│   └── result.html        # Results page
│
├── dataset/
│   └── job_roles.csv      # Job database
│
└── uploads/               # User files (temp)
```

---

## Common Issues & Solutions

### Issue: Port 5000 already in use

**Solution:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process
taskkill /PID <PID> /F
```

### Issue: Module not found errors

**Solution:**
```bash
# Ensure you're in virtual environment
pip install -r requirements.txt --upgrade

# Or install specific package
pip install Flask scikit-learn nltk pdfplumber pandas numpy
```

### Issue: NLTK data missing

**Solution:**
```bash
python -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### Issue: PDF not extracting text

**Solution:**
- Ensure pdfplumber is installed: `pip install --upgrade pdfplumber`
- Try converting PDF to ensure it's not image-based
- Use alternative format: TXT or DOCX

---

## Testing

Run integration tests:
```bash
python test_integration.py
```

Test PDF reading:
```bash
python test_pdf.py
```

---

## Development

### Adding New Features

1. **Add new utility function**
   - Edit relevant file in `utils/`
   - Add tests

2. **Add new API endpoint**
   - Edit `app.py`
   - Add route handler
   - Update HTML if needed

3. **Modify frontend**
   - Edit `templets/index.html` or `result.html`
   - Update `static/style.css`

### Running in Production

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Performance Tips

- **Cache recommendations** for faster response
- **Limit keyword extraction** to top 10-15 keywords
- **Use async processing** for batch operations
- **Implement database** for storing analysis history

---

## Security Notes

- Change `SECRET_KEY` in `config.py` for production
- Validate file uploads (already implemented)
- Use HTTPS in production
- Implement user authentication for multi-user setup
- Add rate limiting for API endpoints

---

## Troubleshooting Checklist

- [ ] Python 3.8+ installed?
- [ ] Virtual environment activated?
- [ ] Dependencies installed? (`pip install -r requirements.txt`)
- [ ] Port 5000 available?
- [ ] NLTK data downloaded?
- [ ] Running from project root directory?

---

## Support & Contribution

For issues:
1. Check this file first
2. Review README.md
3. Check console errors
4. Test individual modules with integration tests

---

**Happy Resume Analyzing! 🎯**
