import spacy
from typing import Tuple, Dict, List
import numpy as np
from collections import defaultdict

class CoherenceAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.transition_words = {
            'addition': ['furthermore', 'moreover', 'also', 'besides', 'in addition'],
            'contrast': ['however', 'nevertheless', 'on the other hand', 'conversely'],
            'cause_effect': ['therefore', 'thus', 'consequently', 'as a result'],
            'sequence': ['first', 'second', 'finally', 'next', 'then'],
            'summary': ['in conclusion', 'to summarize', 'overall', 'in brief']
        }

    def analyze(self, text: str) -> Tuple[float, Dict]:
        """
        Analyze text coherence and return score and feedback
        """
        doc = self.nlp(text)
        paragraphs = self._split_into_paragraphs(text)
        
        # Calculate various coherence metrics
        transition_score = self._analyze_transitions(doc)
        paragraph_score = self._analyze_paragraphs(paragraphs)
        topic_consistency = self._analyze_topic_consistency(doc)
        
        # Calculate overall coherence score
        coherence_score = (transition_score * 0.3 + 
                         paragraph_score * 0.4 + 
                         topic_consistency * 0.3)
        
        # Generate feedback
        feedback = {
            "metrics": {
                "transition_score": transition_score,
                "paragraph_score": paragraph_score,
                "topic_consistency": topic_consistency
            },
            "analysis": {
                "transitions": self._analyze_transition_usage(doc),
                "paragraph_structure": self._analyze_paragraph_structure(paragraphs),
                "topic_flow": self._analyze_topic_flow(doc)
            },
            "suggestions": self._generate_suggestions(
                transition_score, paragraph_score, topic_consistency
            )
        }
        
        return coherence_score, feedback

    def _split_into_paragraphs(self, text: str) -> List[str]:
        """
        Split text into paragraphs
        """
        return [p.strip() for p in text.split('\n\n') if p.strip()]

    def _analyze_transitions(self, doc: spacy.tokens.Doc) -> float:
        """
        Analyze the use of transition words and phrases
        """
        transition_count = 0
        total_sentences = len(list(doc.sents))
        
        for token in doc:
            if token.text.lower() in [word for words in self.transition_words.values() for word in words]:
                transition_count += 1
        
        # Normalize score
        transition_score = min(transition_count / (total_sentences * 0.5), 1.0)
        return transition_score

    def _analyze_paragraphs(self, paragraphs: List[str]) -> float:
        """
        Analyze paragraph structure and organization
        """
        if not paragraphs:
            return 0.0
            
        scores = []
        for para in paragraphs:
            # Analyze paragraph length
            length_score = min(len(para.split()) / 100, 1.0)
            
            # Analyze paragraph structure
            doc = self.nlp(para)
            has_topic_sentence = any(token.dep_ == "nsubj" for token in doc[:5])
            
            # Calculate paragraph score
            para_score = (length_score * 0.4 + float(has_topic_sentence) * 0.6)
            scores.append(para_score)
            
        return sum(scores) / len(scores)

    def _analyze_topic_consistency(self, doc: spacy.tokens.Doc) -> float:
        """
        Analyze topic consistency throughout the text
        """
        # Extract main topics (nouns) from each sentence
        sentence_topics = []
        for sent in doc.sents:
            topics = [token.text for token in sent if token.pos_ == "NOUN"]
            if topics:
                sentence_topics.append(topics)
        
        if not sentence_topics:
            return 0.0
            
        # Calculate topic overlap between consecutive sentences
        topic_overlap = []
        for i in range(len(sentence_topics) - 1):
            overlap = len(set(sentence_topics[i]) & set(sentence_topics[i + 1]))
            total = len(set(sentence_topics[i] + sentence_topics[i + 1]))
            topic_overlap.append(overlap / total if total > 0 else 0)
            
        return sum(topic_overlap) / len(topic_overlap) if topic_overlap else 0.0

    def _analyze_transition_usage(self, doc: spacy.tokens.Doc) -> Dict:
        """
        Analyze the types and frequency of transitions used
        """
        transition_usage = defaultdict(int)
        
        for category, words in self.transition_words.items():
            for word in words:
                count = sum(1 for token in doc if token.text.lower() == word)
                transition_usage[category] += count
                
        return dict(transition_usage)

    def _analyze_paragraph_structure(self, paragraphs: List[str]) -> Dict:
        """
        Analyze the structure of paragraphs
        """
        structure_analysis = {
            "total_paragraphs": len(paragraphs),
            "avg_length": sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0,
            "length_variation": np.std([len(p.split()) for p in paragraphs]) if paragraphs else 0
        }
        
        return structure_analysis

    def _analyze_topic_flow(self, doc: spacy.tokens.Doc) -> Dict:
        """
        Analyze how topics flow through the text
        """
        topic_flow = {
            "main_topics": [],
            "topic_shifts": 0
        }
        
        prev_topics = set()
        for sent in doc.sents:
            current_topics = set(token.text for token in sent if token.pos_ == "NOUN")
            if current_topics and prev_topics:
                if not (current_topics & prev_topics):
                    topic_flow["topic_shifts"] += 1
            prev_topics = current_topics
            
        return topic_flow

    def _generate_suggestions(self, transition_score: float, 
                            paragraph_score: float, 
                            topic_consistency: float) -> List[str]:
        """
        Generate suggestions for improving coherence
        """
        suggestions = []
        
        if transition_score < 0.6:
            suggestions.append("Use more transition words to connect ideas")
            suggestions.append("Consider adding words like 'however', 'therefore', 'furthermore'")
            
        if paragraph_score < 0.6:
            suggestions.append("Ensure each paragraph has a clear topic sentence")
            suggestions.append("Maintain consistent paragraph lengths")
            
        if topic_consistency < 0.6:
            suggestions.append("Work on maintaining better topic flow between sentences")
            suggestions.append("Ensure ideas are logically connected")
            
        return suggestions 