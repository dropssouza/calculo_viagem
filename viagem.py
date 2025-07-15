import openrouteservice

# Substitua com sua chave
API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImU4MDk4MjJiZTNlNzQ4MWE4ZmY3ZDdiZjA3NDQ2ZTRjIiwiaCI6Im11cm11cjY0In0="

client = openrouteservice.Client(key=API_KEY)

# Coordenadas (longitude, latitude)
origem = [-46.633309, -23.55052]  # São Paulo
destino = [-43.209587, -22.9035]  # Rio de Janeiro

# Aqui está o segredo: format='json'
rota = client.directions(
    coordinates=[origem, destino],
    profile='driving-car',
    format='json'  # <- isso força o endpoint correto
)

# Pega dados da rota
distancia_metros = rota['routes'][0]['summary']['distance']
tempo_segundos = rota['routes'][0]['summary']['duration']

distancia_km = distancia_metros / 1000
tempo_minutos = tempo_segundos / 60

print(f"Distância: {distancia_km:.2f} km")
print(f"Tempo estimado: {tempo_minutos:.0f} minutos")