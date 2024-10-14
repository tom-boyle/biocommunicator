from pydantic import BaseModel

class SignalInput(BaseModel):
    signal_data: list[float]
    signal_type: str  # Type of signal, e.g., "plant" or "animal"