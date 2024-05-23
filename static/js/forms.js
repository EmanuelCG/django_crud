// Manejar envío del formulario modal usando AJAX
$('#myForm').submit(function (e) {
    e.preventDefault() // Evita el envío normal del formulario
    $.ajax({
        type: 'POST',
        url: '', // La URL actual es donde se enviarán los datos del formulario
        data: $(this).serialize(), // Datos del formulario
        success: function (response) {
            // Manejar la respuesta si es necesario
            alert('Datos guardados correctamente.')
            // Otras acciones después de guardar los datos
        },
        error: function (xhr, status, error) {
            // Manejar errores si es necesario
            alert('Error al guardar los datos.')
        }
    })
})

