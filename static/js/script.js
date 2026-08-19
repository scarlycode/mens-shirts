/* =============================================
   MEN'S SHIRTS — script.js
   Etapa 5 (parte 1): menú móvil + acordeón FAQ
   ============================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* -----------------------------
       1. MENÚ MÓVIL (hamburguesa)
       ----------------------------- */
    const navToggle = document.getElementById("navToggle");
    const navMenu = document.getElementById("navMenu");

    if (navToggle && navMenu) {
        navToggle.addEventListener("click", function () {
            navMenu.classList.toggle("is-open");
        });

        // Cierra el menú automáticamente al hacer clic en un enlace
        // (útil en móvil: evita que el menú se quede abierto tras navegar)
        const navLinks = navMenu.querySelectorAll("a");
        navLinks.forEach(function (link) {
            link.addEventListener("click", function () {
                navMenu.classList.remove("is-open");
            });
        });
    }

    /* -----------------------------
       2. ACORDEÓN FAQ
       ----------------------------- */
    const faqItems = document.querySelectorAll(".faq__item");

    faqItems.forEach(function (item) {
        const pregunta = item.querySelector(".faq__pregunta");
        const respuesta = item.querySelector(".faq__respuesta");

        // Oculta todas las respuestas al cargar la página
        respuesta.style.display = "none";

        pregunta.addEventListener("click", function () {
            const estaAbierta = respuesta.style.display === "block";

            // Cierra todas las respuestas (para que solo una esté abierta a la vez)
            faqItems.forEach(function (otroItem) {
                otroItem.querySelector(".faq__respuesta").style.display = "none";
                otroItem.querySelector(".faq__pregunta").classList.remove("is-active");
            });

            // Si la pregunta clickeada NO estaba abierta, ábrela
            if (!estaAbierta) {
                respuesta.style.display = "block";
                pregunta.classList.add("is-active");
            }
        });
    });

});