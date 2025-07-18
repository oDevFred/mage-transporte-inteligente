from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mage Transporte Inteligente - API Ativa"}

@app.get("/onibus")
def listar_onibus():
    # Exemplo estático por enquanto
    return [
        {"id": 1, "linha": "Centro - Fragoso", "localizacao": {"lat": -22.663, "lng": -43.051}},
        {"id": 2, "linha": "Centro - Piabetá", "localizacao": {"lat": -22.655, "lng": -43.045}}
    ]
