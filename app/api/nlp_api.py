from fastapi import APIRouter, Form
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

from app.nlp import nlp_service

router = APIRouter()

class TextRequest(BaseModel):
    text: str

class TokenResponse(BaseModel):
    text: str
    lemma: str
    pos: str
    tag: str
    dep: str
    is_stop: bool
    is_alpha: bool
    is_punct: bool

class NLPResponse(BaseModel):
    tokens: List[TokenResponse]
    sentences: List[str]
    text: str

@router.post("/process", response_model=NLPResponse)
async def process_text(request: TextRequest) -> Dict[str, Any]:
    """
    Process text and return tokens with POS data
    """
    return nlp_service.process_text(request.text)

@router.post("/process-form")
async def process_text_form(text: str = Form(...)) -> Dict[str, Any]:
    """
    Process text submitted via form and return tokens with POS data
    """
    return nlp_service.process_text(text)
