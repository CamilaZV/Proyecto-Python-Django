const $formularioEstudiante=document.getElementById('formularioEstudiante');
const $txtNombre2=document.getElementById('txtNombre2');
const $txtApellido=document.getElementById('txtApellido');

(function formu() {
    $formularioEstudiante.addEventListener('submit', function formu(e) {
        let nombre2 = String($txtNombre2.value).trim();
        let apellido = String($txtApellido.value).trim();
        if ((nombre2.length === 0) || (apellido.length === 0)){
            alert("Los campos no pueden estar vacios.");
            e.preventDefault();
        }
    });
})();