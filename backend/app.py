from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.evaluation_model import EssayEvaluator
from utils.preprocessor import TextPreprocessor

app = FastAPI(title="English Essay Evaluator API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EssayRequest(BaseModel):
    text: str
    essay_type: str = "general"  # general, academic, creative

class EvaluationResponse(BaseModel):
    overall_score: float
    cefr_level: str
    letter_grade: str
    feedback: dict
    detailed_analysis: dict

@app.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_essay(request: EssayRequest):
    try:
        # Initialize evaluator
        evaluator = EssayEvaluator()
        
        # Preprocess text
        preprocessor = TextPreprocessor()
        processed_text = preprocessor.preprocess(request.text)
        
        # Perform evaluation
        evaluation_results = evaluator.evaluate(processed_text, request.essay_type)
        
        return evaluation_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 