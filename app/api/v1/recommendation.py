from fastapi import APIRouter, HTTPException
from typing import List
from app.services.recommendation_service import recommend_drug
from app.models.request import SymptomsRequest

router = APIRouter()

@router.post("/recommend", summary="Recommend a drug based on symptoms", response_description="Recommended drug")
def recommend_drug_endpoint(request: SymptomsRequest):
    """
    Recommend a drug based on provided symptoms.
    
    - **symptoms**: List of symptoms to base the recommendation on.
    """
    try:
        recommendation = recommend_drug(request.symptoms)
        return {"recommendation": recommendation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
