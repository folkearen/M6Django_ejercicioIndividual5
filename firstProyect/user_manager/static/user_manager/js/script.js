document.addEventListener('DOMContentLoaded', function() {
    // Obtener la URL actual del navegador
    var urlActual = window.location.href;

    // URL de la página a la que deseas redireccionar
    var urlDeseada = "http://127.0.0.1:8000/user/signUp/successful";

    // Verificar si la URL actual coincide con la URL deseada
    if (urlActual === urlDeseada) {
        // Redirigir a otra página después de 7 segundos
        setTimeout(function() {
            window.location.href = "http://127.0.0.1:8000/user/signUp/";
        }, 7000);
    }
});