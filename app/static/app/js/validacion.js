$(document).ready(function () {
    $("#contact-formulario").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3

            },
            apellido: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                email: true
            },
            comment: {
                required: true,
            }
        }, messages: {
            nombre: {
                minlength: "El nombre debe contener al menos 3 caracteres"
            },
            apellido: {
                minlength: "El nombre debe contener al menos 3 caracteres"
            },
            email: {
                email: "Debe tener sintaxis de email"

            },
            comment: {
                required: "Debes llenar este campo",
            }
        }
    });
});


const form = document.getElementById("contact-formulario");

form.addEventListener("submit", function (event) {
    // ---> Esto es para que no se caiga la pagina al dar en "Enviar"
    event.preventDefault();
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    var email = $('#email').val();
    var comment = $('#comment').val();

});





// ----------------------------------
//             Chuly
//     GitHub: https://github.com/victoryanezn
//     Discord: chuly2005#0
// ----------------------------------