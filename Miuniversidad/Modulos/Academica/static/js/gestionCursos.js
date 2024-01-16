const btnEliminacion=document.querySelectorAll(".btnEliminacion");
const $formularioCurso=document.getElementById('formularioCurso');
const $txtNombre=document.getElementById('txtNombre');
const $txtDocente=document.getElementById('txtDocente');

(function () {
    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Confirma la eliminación?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });
})();

(function formulario () {
    $formularioCurso.addEventListener('submit', function formulario (e) {
        let nombre = String($txtNombre.value).trim();
        let docente = String($txtDocente.value).trim();
        if ((nombre.length === 0) || (docente.length === 0)){
            alert("Los campos no pueden estar vacios.");
            e.preventDefault();
        }
    });
})();

