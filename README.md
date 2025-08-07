# 🚗 Calculadora de Viagem

Este projeto é uma calculadora de viagem que estima a **distância**, o **tempo de percurso** e o **custo total** de combustível entre duas cidades. O cálculo é feito com base no consumo médio do veículo e no preço atual do combustível.

---

## 🖥️ Tecnologias Utilizadas

- HTML, CSS e JavaScript (Frontend)
- FastAPI com Python (Backend)
- OpenRouteService API (Geocodificação e rotas)

---

## 💡 Como Funciona
### 1. O usuário informa:
- Origem e destino (ex: "São Paulo, SP");
- Consumo médio (km/L);
- Preço do combustível (R$/L).

### 2. O frontend envia uma requisição POST para o backend com os dados a serem calculados.

### 3. O backend:

- Usa a OpenRouteService para calcular a rota entre origem e destino;
- Calcula distância, tempo de viagem e custo com combustível;
- Retorna os dados para o frontend.

## 🚀 Futuras Melhorias
- Mapa interativo com a rota;
- Validação de cidades inválidas;
- Calculo estimado já com pedágios inclusos;
- Hospedagem em domínio próprio.

---

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.🤝
