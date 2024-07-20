from pydantic import BaseModel
from typing import List

class Drug(BaseModel):
    name: str
    symptoms: List[str]
