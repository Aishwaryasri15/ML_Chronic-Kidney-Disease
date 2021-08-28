const fila = document.querySelector(".contenedor-carrusel");
const pelicula = document.querySelectorAll(".pelicula");

const flechaIzquierda = document.getElementById("flecha-izquierda");
const flechaDerecha = document.getElementById("flecha-derecha");

/* ----- ----- EventListener para la flecha derecha ----- ----- */
flechaDerecha.addEventListener("click", () => {
  fila.scrollLeft += fila.offsetWidth;

  const indicadorActivo = document.querySelector(".indicadores .activo");
  if (indicadorActivo.nextSibling) {
    indicadorActivo.nextSibling.classList.add("activo");
    indicadorActivo.classList.remove("activo");
  }
});

/* ----- ----- EventListener para la flecha izquierda ----- ----- */
flechaIzquierda.addEventListener("click", () => {
  fila.scrollLeft -= fila.offsetWidth;

  const indicadorActivo = document.querySelector(".indicadores .activo");
  if (indicadorActivo.previousSibling) {
    indicadorActivo.previousSibling.classList.add("activo");
    indicadorActivo.classList.remove("activo");
  }
});

/* ----- ----- Paginación ----- ----- */
const numeroPaginas = Math.ceil(pelicula.length / 5);
for (let i = 0; i < numeroPaginas; i++) {
  const indicador = document.createElement("button");

  if (i === 0) {
    indicador.classList.add("activo");
  }

  document.querySelector(".indicadores").appendChild(indicador);
  indicador.addEventListener("click", (e) => {
    fila.scrollLeft = i * fila.offsetWidth;

    document.querySelector(".indicadores .activo").classList.remove("activo");
    e.target.classList.add("activo");
  });
}

/* ----- ----- Hover ----- ----- */
pelicula.forEach((peli) => {
  peli.addEventListener("mouseenter", (e) => {
    const elemento = e.currentTarget;
    setTimeout(() => {
      pelicula.forEach((peli) => peli.classList.remove("hover"));
      elemento.classList.add("hover");
    }, 300);
  });
});
fila.addEventListener("mouseleave", () => {
  pelicula.forEach((peli) => peli.classList.remove("hover"));
});
