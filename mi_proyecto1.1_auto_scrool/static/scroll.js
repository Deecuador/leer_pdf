let scrolling = false;
let scrollInterval;

document.getElementById("scrollButton").addEventListener("click", function() {
  if (!scrolling) {
    scrolling = true;
    this.textContent = "Detener Scroll";

    scrollInterval = setInterval(() => {
      window.scrollBy(0, 1); // Desplaza la página 5px hacia abajo
      if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        clearInterval(scrollInterval);
        scrolling = false;
        this.textContent = "Iniciar Scroll";
      }
    }, 5); // Ajusta la velocidad (más bajo = más rápido)
  } else {
    clearInterval(scrollInterval);
    scrolling = false;
    this.textContent = "Iniciar Scroll";
  }
});
