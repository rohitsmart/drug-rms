from typing import List
from app.models.drug import Drug

# Dummy data for demonstration
drugs = [
    Drug(name="DrugA", symptoms=["headache", "fever"]),
    Drug(name="DrugB", symptoms=["cough", "sore throat"]),
    Drug(name="DrugC", symptoms=["nausea", "vomiting"]),
]

def recommend_drug(symptoms: List[str]) -> str:
    for drug in drugs:
        if all(symptom in drug.symptoms for symptom in symptoms):
            return drug.name
    return "No suitable drug found"
