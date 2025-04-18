import React, { useState } from 'react';
import Editor from './components/Editor';
import Results from './components/Results';
import Feedback from './components/Feedback';
import './styles.css';

function App() {
  const [evaluation, setEvaluation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleEvaluate = async (text) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('http://localhost:8000/evaluate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: text,
          essay_type: 'general'
        }),
      });

      if (!response.ok) {
        throw new Error('Evaluation failed');
      }

      const data = await response.json();
      setEvaluation(data);
    } catch (err) {
      setError('Failed to evaluate essay. Please try again.');
      console.error('Evaluation error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>English Essay Evaluator</h1>
        <p>Get instant feedback on your English writing</p>
      </header>

      <main className="app-main">
        <Editor onEvaluate={handleEvaluate} />
        
        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Evaluating your essay...</p>
          </div>
        )}

        {error && (
          <div className="error">
            <p>{error}</p>
          </div>
        )}

        {evaluation && !loading && (
          <div className="results-container">
            <Results evaluation={evaluation} />
            <Feedback evaluation={evaluation} />
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>Powered by AI - English Essay Evaluation System</p>
      </footer>
    </div>
  );
}

export default App; 