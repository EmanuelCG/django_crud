setTimeout(function () {
    $('#message').fadeOut('slow')
}, 4000)

document.getElementById('eliminarEmpleadoForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita el envío del formulario por defecto

    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción no se puede deshacer.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminarlo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Si el usuario confirma, envía el formulario
            this.submit();
        }
    });
});