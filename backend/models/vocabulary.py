import nltk
from nltk.corpus import wordnet
from typing import Tuple, Dict, List
import spacy
from collections import Counter

class VocabularyAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        # Download required NLTK data
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')
        
        # CEFR level vocabulary lists (simplified version)
        self.cefr_levels = {
            'A1': set(),  # Basic vocabulary
            'A2': set(),  # Elementary vocabulary
            'B1': set(),  # Intermediate vocabulary
            'B2': set(),  # Upper intermediate vocabulary
            'C1': set(),  # Advanced vocabulary
            'C2': set()   # Mastery vocabulary
        }

    def analyze(self, text: str) -> Tuple[float, Dict]:
        """
        Analyze vocabulary usage and return score and feedback
        """
        doc = self.nlp(text)
        
        # Extract words and their properties
        words = [token.text.lower() for token in doc if token.is_alpha]
        unique_words = set(words)
        
        # Calculate basic metrics
        total_words = len(words)
        unique_word_count = len(unique_words)
        
        # Calculate vocabulary density
        vocabulary_density = unique_word_count / total_words if total_words > 0 else 0
        
        # Analyze word complexity
        complexity_score = self._analyze_word_complexity(words)
        
        # Calculate overall vocabulary score
        vocabulary_score = (vocabulary_density * 0.4 + complexity_score * 0.6)
        
        # Generate feedback
        feedback = {
            "metrics": {
                "total_words": total_words,
                "unique_words": unique_word_count,
                "vocabulary_density": vocabulary_density,
                "complexity_score": complexity_score
            },
            "word_analysis": self._analyze_word_usage(words),
            "suggestions": self._generate_suggestions(words, vocabulary_score)
        }
        
        return vocabulary_score, feedback

    def _analyze_word_complexity(self, words: List[str]) -> float:
        """
        Analyze the complexity of words used
        """
        complexity_scores = []
        
        for word in words:
            # Get word synsets
            synsets = wordnet.synsets(word)
            if not synsets:
                continue
                
            # Calculate complexity based on:
            # 1. Number of syllables
            # 2. Number of synsets (meanings)
            # 3. Word length
            syllable_count = self._count_syllables(word)
            synset_count = len(synsets)
            length_score = min(len(word) / 12, 1.0)  # Normalize length
            
            # Combine scores
            word_complexity = (syllable_count * 0.3 + synset_count * 0.4 + length_score * 0.3)
            complexity_scores.append(word_complexity)
        
        return sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0

    def _count_syllables(self, word: str) -> int:
        """
        Count the number of syllables in a word
        """
        count = 0
        vowels = 'aeiouy'
        word = word.lower()
        
        if word[0] in vowels:
            count += 1
            
        for index in range(1, len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count += 1
                
        if word.endswith('e'):
            count -= 1
            
        if count == 0:
            count = 1
            
        return count

    def _analyze_word_usage(self, words: List[str]) -> Dict:
        """
        Analyze patterns in word usage
        """
        word_freq = Counter(words)
        
        # Find most common words
        common_words = word_freq.most_common(10)
        
        # Analyze word variety
        word_variety = {
            "high_frequency_words": [word for word, count in common_words if count > 3],
            "unique_word_ratio": len(set(words)) / len(words) if words else 0
        }
        
        return word_variety

    def _generate_suggestions(self, words: List[str], vocabulary_score: float) -> List[str]:
        """
        Generate suggestions for vocabulary improvement
        """
        suggestions = []
        
        if vocabulary_score < 0.6:
            suggestions.append("Try using more diverse vocabulary")
            suggestions.append("Consider using synonyms to avoid repetition")
        
        # Analyze word variety
        unique_words = set(words)
        if len(unique_words) / len(words) < 0.5:
            suggestions.append("Work on expanding your vocabulary range")
        
        return suggestions 