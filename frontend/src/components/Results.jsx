import React from 'react';

const Results = ({ evaluation }) => {
  const { overall_score, cefr_level, letter_grade, detailed_analysis } = evaluation;

  const getScoreColor = (score) => {
    if (score >= 0.8) return 'green';
    if (score >= 0.6) return 'orange';
    return 'red';
  };

  const formatScore = (score) => {
    return (score * 100).toFixed(1) + '%';
  };

  return (
    <div className="results">
      <div className="results-header">
        <h2>Evaluation Results</h2>
      </div>

      <div className="overall-score">
        <div className="score-circle" style={{ 
          backgroundColor: getScoreColor(overall_score),
          color: 'white'
        }}>
          <div className="score-value">{formatScore(overall_score)}</div>
          <div className="score-label">Overall Score</div>
        </div>

        <div className="grade-display">
          <div className="grade-item">
            <span className="grade-label">CEFR Level:</span>
            <span className="grade-value">{cefr_level}</span>
          </div>
          <div className="grade-item">
            <span className="grade-label">Letter Grade:</span>
            <span className="grade-value">{letter_grade}</span>
          </div>
        </div>
      </div>

      <div className="component-scores">
        <h3>Component Scores</h3>
        <div className="score-bars">
          <div className="score-bar">
            <div className="bar-label">Grammar</div>
            <div className="bar-container">
              <div 
                className="bar-fill"
                style={{ 
                  width: formatScore(detailed_analysis.grammar.score),
                  backgroundColor: getScoreColor(detailed_analysis.grammar.score)
                }}
              />
            </div>
            <div className="bar-value">{formatScore(detailed_analysis.grammar.score)}</div>
          </div>

          <div className="score-bar">
            <div className="bar-label">Vocabulary</div>
            <div className="bar-container">
              <div 
                className="bar-fill"
                style={{ 
                  width: formatScore(detailed_analysis.vocabulary.score),
                  backgroundColor: getScoreColor(detailed_analysis.vocabulary.score)
                }}
              />
            </div>
            <div className="bar-value">{formatScore(detailed_analysis.vocabulary.score)}</div>
          </div>

          <div className="score-bar">
            <div className="bar-label">Coherence</div>
            <div className="bar-container">
              <div 
                className="bar-fill"
                style={{ 
                  width: formatScore(detailed_analysis.coherence.score),
                  backgroundColor: getScoreColor(detailed_analysis.coherence.score)
                }}
              />
            </div>
            <div className="bar-value">{formatScore(detailed_analysis.coherence.score)}</div>
          </div>
        </div>
      </div>

      <div className="metrics-summary">
        <h3>Detailed Metrics</h3>
        <div className="metrics-grid">
          <div className="metric-item">
            <span className="metric-label">Grammar Errors:</span>
            <span className="metric-value">{detailed_analysis.grammar.feedback.error_count}</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">Unique Words:</span>
            <span className="metric-value">{detailed_analysis.vocabulary.feedback.metrics.unique_words}</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">Paragraphs:</span>
            <span className="metric-value">{detailed_analysis.coherence.feedback.analysis.paragraph_structure.total_paragraphs}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Results; 