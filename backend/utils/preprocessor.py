import re
import spacy
from typing import List

class TextPreprocessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        
    def preprocess(self, text: str) -> str:
        """
        Preprocess the input text for analysis
        """
        # Clean and normalize text
        cleaned_text = self._clean_text(text)
        
        # Remove extra whitespace
        cleaned_text = self._normalize_whitespace(cleaned_text)
        
        # Fix common formatting issues
        cleaned_text = self._fix_formatting(cleaned_text)
        
        return cleaned_text
        
    def _clean_text(self, text: str) -> str:
        """
        Clean the input text by removing unwanted characters and normalizing
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^a-z0-9\s.,!?;:()\-\'"]', '', text)
        
        # Fix common OCR/typing errors
        text = text.replace('l', 'I')  # Common capitalization error
        text = text.replace('0', 'o')  # Common number/letter confusion
        
        return text
        
    def _normalize_whitespace(self, text: str) -> str:
        """
        Normalize whitespace in the text
        """
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Fix spacing around punctuation
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)
        
        # Ensure proper spacing after punctuation
        text = re.sub(r'([.,!?;:])([a-z])', r'\1 \2', text)
        
        return text.strip()
        
    def _fix_formatting(self, text: str) -> str:
        """
        Fix common formatting issues
        """
        # Fix capitalization at sentence starts
        sentences = self._split_into_sentences(text)
        formatted_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                # Capitalize first letter of sentence
                formatted_sentence = sentence.strip()[0].upper() + sentence.strip()[1:]
                formatted_sentences.append(formatted_sentence)
                
        return ' '.join(formatted_sentences)
        
    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences using spaCy
        """
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents]
        
    def get_word_count(self, text: str) -> int:
        """
        Get accurate word count after preprocessing
        """
        doc = self.nlp(text)
        return len([token for token in doc if not token.is_punct and not token.is_space])
        
    def get_sentence_count(self, text: str) -> int:
        """
        Get accurate sentence count
        """
        doc = self.nlp(text)
        return len(list(doc.sents))
        
    def get_paragraph_count(self, text: str) -> int:
        """
        Get paragraph count
        """
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        return len(paragraphs) 