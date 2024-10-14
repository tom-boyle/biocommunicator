from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_model import interpret_bio_signal

class SignalInput(BaseModel):
    signal_data: list[float]
    signal_type: str

router = APIRouter()

@router.post("/interpret_signal")
def interpret_signal(input: SignalInput):
    try:
        prediction = interpret_bio_signal(input.signal_data)
        return {"signal_type": input.signal_type, "prediction": prediction}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
