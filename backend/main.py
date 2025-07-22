import os
import openrouteservice
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

#PERMITINDO CHAMADAS DO FRONTEND
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#PEGANDO API KEY DO AMBIENTE
ORS_API_KEY = os.getenv("ORS_API_KEY")
client = openrouteservice.Client(key=ORS_API_KEY)

class ViagemRequest(BaseModel):
    origem: str
    destino: str
    consumo: float 
    preco_combustivel: float 


@app.post("/calcular")
def calcular_viagem(data: ViagemRequest):
    #GEOCODIFICADOR
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


    litros = distancia_km / data.consumo
    custo = litros * data.preco_combustivel

    return {
        "distancia_km": round(distancia_km, 2),
        "tempo_estimado": f"{horas}h {minutos}min",
        "custo_total": round(custo, 2)
    }

