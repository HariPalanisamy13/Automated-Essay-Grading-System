import language_tool_python
import spacy
from typing import Tuple, Dict, List

class GrammarChecker:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.nlp = spacy.load('en_core_web_sm')

    def analyze(self, text: str) -> Tuple[float, Dict]:
        """
        Analyze text for grammatical correctness and return score and feedback
        """
        # Get grammar errors
        matches = self.tool.check(text)
        
        # Calculate basic metrics
        doc = self.nlp(text)
        sentences = list(doc.sents)
        words = [token.text for token in doc if not token.is_punct]
        
        # Calculate error rate
        error_rate = len(matches) / len(words) if words else 1
        grammar_score = max(0, 1 - error_rate)
        
        # Analyze sentence structure
        structure_feedback = self._analyze_sentence_structure(sentences)
        
        # Generate detailed feedback
        feedback = {
            "error_count": len(matches),
            "error_details": self._get_error_details(matches),
            "sentence_structure": structure_feedback,
            "suggestions": self._generate_suggestions(matches, structure_feedback)
        }
        
        return grammar_score, feedback

    def _analyze_sentence_structure(self, sentences: List[spacy.tokens.span.Span]) -> Dict:
        """
        Analyze sentence structure variety and complexity
        """
        structure_analysis = {
            "total_sentences": len(sentences),
            "avg_length": sum(len(sent) for sent in sentences) / len(sentences) if sentences else 0,
            "structure_types": {
                "simple": 0,
                "compound": 0,
                "complex": 0
            }
        }
        
        for sent in sentences:
            # Count clauses
            clause_count = sum(1 for token in sent if token.dep_ == "mark")
            
            if clause_count == 0:
                structure_analysis["structure_types"]["simple"] += 1
            elif clause_count == 1:
                structure_analysis["structure_types"]["compound"] += 1
            else:
                structure_analysis["structure_types"]["complex"] += 1
        
        return structure_analysis

    def _get_error_details(self, matches: List) -> List[Dict]:
        """
        Extract detailed information about grammar errors
        """
        error_details = []
        for match in matches:
            error_details.append({
                "message": match.message,
                "rule_id": match.ruleId,
                "context": match.context,
                "offset": match.offset,
                "length": match.errorLength
            })
        return error_details

    def _generate_suggestions(self, matches: List, structure_analysis: Dict) -> List[str]:
        """
        Generate specific suggestions for improvement
        """
        suggestions = []
        
        # Add suggestions based on error patterns
        error_types = set(match.ruleId for match in matches)
        if "TOO_LONG_SENTENCE" in error_types:
            suggestions.append("Consider breaking down long sentences into shorter ones")
        if "UPPERCASE_SENTENCE_START" in error_types:
            suggestions.append("Ensure all sentences start with a capital letter")
        
        # Add suggestions based on sentence structure
        if structure_analysis["structure_types"]["simple"] > structure_analysis["structure_types"]["complex"]:
            suggestions.append("Try using more complex sentence structures to improve writing style")
        
        return suggestions 