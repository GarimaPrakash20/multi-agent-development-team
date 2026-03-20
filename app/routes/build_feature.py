from fastapi import APIRouter
from pydantic import BaseModel

from app.orchestrator.agent_controller import build_feature

router = APIRouter()


class FeatureRequest(BaseModel):
    request: str


@router.post("/build-feature")
def build(request: FeatureRequest):
    result = build_feature(request.request)
    return result
