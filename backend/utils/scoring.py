from typing import Dict, Tuple

class ScoreCalculator:
    def __init__(self):
        # CEFR level thresholds
        self.cefr_thresholds = {
            'C2': 0.9,  # Mastery
            'C1': 0.8,  # Advanced
            'B2': 0.7,  # Upper Intermediate
            'B1': 0.6,  # Intermediate
            'A2': 0.5,  # Elementary
            'A1': 0.4   # Basic
        }
        
        # Letter grade thresholds
        self.grade_thresholds = {
            'A': 0.9,
            'B': 0.8,
            'C': 0.7,
            'D': 0.6,
            'F': 0.0
        }

    def calculate_overall_score(self, grammar_score: float, 
                             vocabulary_score: float, 
                             coherence_score: float) -> float:
        """
        Calculate the overall score based on component scores
        """
        # Weighted average of component scores
        weights = {
            'grammar': 0.4,
            'vocabulary': 0.3,
            'coherence': 0.3
        }
        
        overall_score = (
            grammar_score * weights['grammar'] +
            vocabulary_score * weights['vocabulary'] +
            coherence_score * weights['coherence']
        )
        
        return round(overall_score, 2)

    def get_cefr_level(self, score: float) -> str:
        """
        Convert numerical score to CEFR level
        """
        for level, threshold in sorted(self.cefr_thresholds.items(), 
                                    key=lambda x: x[1], reverse=True):
            if score >= threshold:
                return level
        return 'A1'  # Default to basic level if score is very low

    def get_letter_grade(self, score: float) -> str:
        """
        Convert numerical score to letter grade
        """
        for grade, threshold in sorted(self.grade_thresholds.items(), 
                                    key=lambda x: x[1], reverse=True):
            if score >= threshold:
                return grade
        return 'F'

    def get_detailed_grade_breakdown(self, scores: Dict[str, float]) -> Dict:
        """
        Generate detailed grade breakdown with component scores
        """
        return {
            'overall': {
                'score': self.calculate_overall_score(
                    scores['grammar'],
                    scores['vocabulary'],
                    scores['coherence']
                ),
                'cefr_level': self.get_cefr_level(
                    self.calculate_overall_score(
                        scores['grammar'],
                        scores['vocabulary'],
                        scores['coherence']
                    )
                ),
                'letter_grade': self.get_letter_grade(
                    self.calculate_overall_score(
                        scores['grammar'],
                        scores['vocabulary'],
                        scores['coherence']
                    )
                )
            },
            'components': {
                'grammar': {
                    'score': scores['grammar'],
                    'cefr_level': self.get_cefr_level(scores['grammar']),
                    'letter_grade': self.get_letter_grade(scores['grammar'])
                },
                'vocabulary': {
                    'score': scores['vocabulary'],
                    'cefr_level': self.get_cefr_level(scores['vocabulary']),
                    'letter_grade': self.get_letter_grade(scores['vocabulary'])
                },
                'coherence': {
                    'score': scores['coherence'],
                    'cefr_level': self.get_cefr_level(scores['coherence']),
                    'letter_grade': self.get_letter_grade(scores['coherence'])
                }
            }
        } 