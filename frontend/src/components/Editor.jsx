import React, { useState } from 'react';

const Editor = ({ onEvaluate }) => {
  const [text, setText] = useState('');
  const [wordCount, setWordCount] = useState(0);

  const handleTextChange = (e) => {
    const newText = e.target.value;
    setText(newText);
    setWordCount(newText.trim().split(/\s+/).filter(Boolean).length);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onEvaluate(text);
    }
  };

  return (
    <div className="editor-container">
      <form onSubmit={handleSubmit} className="editor-form">
        <div className="editor-header">
          <h2>Write Your Essay</h2>
          <div className="word-count">
            Words: {wordCount}
          </div>
        </div>
        
        <textarea
          className="editor-textarea"
          value={text}
          onChange={handleTextChange}
          placeholder="Enter your essay here..."
          rows="15"
          required
        />
        
        <div className="editor-footer">
          <button 
            type="submit" 
            className="evaluate-button"
            disabled={!text.trim()}
          >
            Evaluate Essay
          </button>
        </div>
      </form>
      
      <div className="editor-tips">
        <h3>Writing Tips</h3>
        <ul>
          <li>Write clear and concise sentences</li>
          <li>Use proper grammar and punctuation</li>
          <li>Organize your ideas logically</li>
          <li>Use transition words to connect ideas</li>
          <li>Proofread your work before submitting</li>
        </ul>
      </div>
    </div>
  );
};

export default Editor; 