from pydantic import BaseModel

class StressRequest(BaseModel):
    Sleep_Duration: float
    Quality_of_Sleep: float
    Age: int
    Heart_Rate: int
    Daily_Steps: int
    Physical_Activity_Level: float

class StressResponse(BaseModel):
    stress_level: int
