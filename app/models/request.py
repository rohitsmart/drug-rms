from pydantic import BaseModel
from typing import List

class SymptomsRequest(BaseModel):
    symptoms: List[str]
