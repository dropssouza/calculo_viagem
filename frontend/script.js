async function calcular() {
  const origem = document.getElementById("origem").value;
  const destino = document.getElementById("destino").value;
  const consumo = parseFloat(document.getElementById("consumo").value);
  const preco = parseFloat(document.getElementById("preco").value);

  let botao_calcular = document.querySelector(".botao");
  botao_calcular.classList.remove("clicado");
  setTimeout(function () {
    botao_calcular.classList.add("clicado");
  }, 100);

  const response = await fetch("https://api-viagem.onrender.com/calcular", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      origem,
      destino,
      consumo,
      preco_combustivel: preco,
    }),
  });

  const data = await response.json();

  document.getElementById("resultado").innerHTML = `
    <p>Distância: ${data.distancia_km} km</p>
    <p>Tempo estimado: ${data.tempo_estimado}</p>
    <p>Gasto estimado: R$ ${data.custo_total.toFixed(2)}</p>
  `;
}
