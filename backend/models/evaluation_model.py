from .grammar_checker import GrammarChecker
from .vocabulary import VocabularyAnalyzer
from .coherence import CoherenceAnalyzer
from utils.scoring import ScoreCalculator

class EssayEvaluator:
    def __init__(self):
        self.grammar_checker = GrammarChecker()
        self.vocabulary_analyzer = VocabularyAnalyzer()
        self.coherence_analyzer = CoherenceAnalyzer()
        self.score_calculator = ScoreCalculator()

    def evaluate(self, text: str, essay_type: str = "general") -> dict:
        """
        Evaluate an essay and return comprehensive analysis
        """
        # Perform individual analyses
        grammar_score, grammar_feedback = self.grammar_checker.analyze(text)
        vocab_score, vocab_feedback = self.vocabulary_analyzer.analyze(text)
        coherence_score, coherence_feedback = self.coherence_analyzer.analyze(text)

        # Calculate overall score and grades
        overall_score = self.score_calculator.calculate_overall_score(
            grammar_score, vocab_score, coherence_score
        )
        
        cefr_level = self.score_calculator.get_cefr_level(overall_score)
        letter_grade = self.score_calculator.get_letter_grade(overall_score)

        # Compile detailed analysis
        detailed_analysis = {
            "grammar": {
                "score": grammar_score,
                "feedback": grammar_feedback
            },
            "vocabulary": {
                "score": vocab_score,
                "feedback": vocab_feedback
            },
            "coherence": {
                "score": coherence_score,
                "feedback": coherence_feedback
            }
        }

        # Generate overall feedback
        feedback = self._generate_feedback(detailed_analysis)

        return {
            "overall_score": overall_score,
            "cefr_level": cefr_level,
            "letter_grade": letter_grade,
            "feedback": feedback,
            "detailed_analysis": detailed_analysis
        }

    def _generate_feedback(self, analysis: dict) -> dict:
        """
        Generate comprehensive feedback based on detailed analysis
        """
        strengths = []
        improvements = []

        # Analyze grammar feedback
        if analysis["grammar"]["score"] >= 0.8:
            strengths.append("Strong grammatical foundation")
        elif analysis["grammar"]["score"] < 0.6:
            improvements.append("Focus on improving grammar accuracy")

        # Analyze vocabulary feedback
        if analysis["vocabulary"]["score"] >= 0.8:
            strengths.append("Rich and varied vocabulary")
        elif analysis["vocabulary"]["score"] < 0.6:
            improvements.append("Work on expanding vocabulary range")

        # Analyze coherence feedback
        if analysis["coherence"]["score"] >= 0.8:
            strengths.append("Excellent text organization and flow")
        elif analysis["coherence"]["score"] < 0.6:
            improvements.append("Improve paragraph structure and transitions")

        return {
            "strengths": strengths,
            "areas_for_improvement": improvements,
            "recommendations": self._generate_recommendations(analysis)
        }

    def _generate_recommendations(self, analysis: dict) -> list:
        """
        Generate specific recommendations based on analysis
        """
        recommendations = []
        
        # Add recommendations based on scores
        if analysis["grammar"]["score"] < 0.7:
            recommendations.append("Review basic grammar rules and practice sentence structure")
        
        if analysis["vocabulary"]["score"] < 0.7:
            recommendations.append("Read more diverse materials to expand vocabulary")
        
        if analysis["coherence"]["score"] < 0.7:
            recommendations.append("Practice writing with clear topic sentences and logical transitions")

        return recommendations 