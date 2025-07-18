from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_onibus():
    return [
        {"id": 1, "linha": "Centro - Fragoso", "localizacao": {"lat": -22.663, "lng": -43.051}},
        {"id": 2, "linha": "Centro - Piabetá", "localizacao": {"lat": -22.655, "lng": -43.045}}
    ]
