from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openrouteservice

app = FastAPI()

# Permitir chamadas do frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Durante testes pode deixar assim
    allow_methods=["*"],
    allow_headers=["*"],
)

# Substitua com sua chave
API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImU4MDk4MjJiZTNlNzQ4MWE4ZmY3ZDdiZjA3NDQ2ZTRjIiwiaCI6Im11cm11cjY0In0="

client = openrouteservice.Client(key=API_KEY)

class ViagemRequest(BaseModel):
    origem: str
    destino: str
    consumo: float  # km por litro
    preco_combustivel: float  # R$/litro


@app.post("/calcular")
def calcular_viagem(data: ViagemRequest):
    # Geocodificar
    coord_origem = client.pelias_search(data.origem)['features'][0]['geometry']['coordinates']
    coord_destino = client.pelias_search(data.destino)['features'][0]['geometry']['coordinates']

    rota = client.directions(
    coordinates=[coord_origem, coord_destino],
    profile='driving-car',
    format='json'
    )

    distancia_km = rota['routes'][0]['summary']['distance'] / 1000
    tempo_minutos = int(rota['routes'][0]['summary']['duration'] / 60)
    horas = tempo_minutos // 60
    minutos = tempo_minutos % 60

    # Calcular custo
    litros = distancia_km / data.consumo
    custo = litros * data.preco_combustivel

    return {
        "distancia_km": round(distancia_km, 2),
        "tempo_estimado": f"{horas}h {minutos}min",
        "custo_total": round(custo, 2)
    }

