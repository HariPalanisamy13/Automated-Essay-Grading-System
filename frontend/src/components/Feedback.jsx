import React from 'react';

const Feedback = ({ evaluation }) => {
  const { feedback, detailed_analysis } = evaluation;

  return (
    <div className="feedback">
      <div className="feedback-header">
        <h2>Detailed Feedback</h2>
      </div>

      <div className="feedback-sections">
        <section className="feedback-section">
          <h3>Strengths</h3>
          {feedback.strengths.length > 0 ? (
            <ul className="strengths-list">
              {feedback.strengths.map((strength, index) => (
                <li key={index} className="strength-item">
                  <span className="check-icon">✓</span>
                  {strength}
                </li>
              ))}
            </ul>
          ) : (
            <p className="no-feedback">No specific strengths identified.</p>
          )}
        </section>

        <section className="feedback-section">
          <h3>Areas for Improvement</h3>
          {feedback.areas_for_improvement.length > 0 ? (
            <ul className="improvements-list">
              {feedback.areas_for_improvement.map((area, index) => (
                <li key={index} className="improvement-item">
                  <span className="arrow-icon">→</span>
                  {area}
                </li>
              ))}
            </ul>
          ) : (
            <p className="no-feedback">No specific areas for improvement identified.</p>
          )}
        </section>

        <section className="feedback-section">
          <h3>Recommendations</h3>
          <ul className="recommendations-list">
            {feedback.recommendations.map((recommendation, index) => (
              <li key={index} className="recommendation-item">
                <span className="bullet-icon">•</span>
                {recommendation}
              </li>
            ))}
          </ul>
        </section>

        <section className="feedback-section">
          <h3>Detailed Analysis</h3>
          <div className="detailed-analysis">
            <div className="analysis-item">
              <h4>Grammar Analysis</h4>
              <ul>
                {detailed_analysis.grammar.feedback.suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>

            <div className="analysis-item">
              <h4>Vocabulary Analysis</h4>
              <ul>
                {detailed_analysis.vocabulary.feedback.suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>

            <div className="analysis-item">
              <h4>Coherence Analysis</h4>
              <ul>
                {detailed_analysis.coherence.feedback.suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>
          </div>
        </section>
      </div>

      <div className="feedback-footer">
        <p className="feedback-note">
          Note: This feedback is generated automatically based on linguistic analysis.
          Consider consulting with a human editor for comprehensive review.
        </p>
      </div>
    </div>
  );
};

export default Feedback; 