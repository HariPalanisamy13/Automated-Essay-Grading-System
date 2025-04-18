# English Essay Evaluator

An AI-powered system that automatically analyzes English essays and provides detailed feedback on grammar, vocabulary, and coherence. The system assigns proficiency levels based on CEFR standards and provides specific suggestions for improvement.

## Features

- Grammar analysis and error detection
- Vocabulary richness and complexity assessment
- Text coherence and organization evaluation
- CEFR level (A1-C2) and letter grade assignment
- Detailed feedback and improvement suggestions
- Modern, responsive web interface

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/english-essay-evaluator.git
cd english-essay-evaluator
```

2. Set up the backend:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
# From the project root directory
cd backend
uvicorn app:app --reload
```

2. Start the frontend development server:
```bash
# In a new terminal, from the frontend directory
cd frontend
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter your essay text in the editor
2. Click "Evaluate Essay" to submit
3. View the evaluation results, including:
   - Overall score and grade
   - CEFR proficiency level
   - Component-wise analysis
   - Detailed feedback and suggestions

## Project Structure

```
english-essay-evaluator/
├── backend/
│   ├── app.py                  # Main FastAPI application
│   │   ├── models/
│   │   │   ├── evaluation_model.py # Main evaluation logic
│   │   │   ├── grammar_checker.py  # Grammar analysis module
│   │   │   ├── vocabulary.py       # Vocabulary analysis
│   │   │   └── coherence.py        # Coherence analysis
│   │   ├── utils/
│   │   │   ├── preprocessor.py     # Text cleaning/normalization
│   │   │   └── scoring.py          # Scoring algorithms
│   │   └── config.py               # Configuration settings
│   ├── frontend/
│   │   ├── public/
│   │   │   └── index.html          # Base HTML
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── Editor.jsx      # Essay input component
│   │   │   │   ├── Results.jsx     # Results display
│   │   │   │   └── Feedback.jsx    # Detailed feedback
│   │   │   ├── App.js              # Main app component
│   │   │   └── styles.css          # CSS styles
│   │   └── package.json            # Frontend dependencies
│   ├── requirements.txt            # Python dependencies
│   └── README.md                   # Project documentation
```

## API Endpoints

- `POST /evaluate`: Submit an essay for evaluation
  - Request body: `{ "text": "essay content", "essay_type": "general" }`
  - Response: Evaluation results with scores and feedback

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- spaCy for NLP capabilities
- LanguageTool for grammar checking
- NLTK for vocabulary analysis
- FastAPI for backend framework
- React for frontend framework 