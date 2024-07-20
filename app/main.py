from fastapi import FastAPI
from app.api.v1.recommendation import router as recommendation_router

app = FastAPI(
    title="Drug Recommendation API",
    description="API for recommending drugs based on symptoms",
    version="1.0.0"
)

app.include_router(recommendation_router, prefix="/api/v1", tags=["recommendation"])
