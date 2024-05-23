$(document).ready(function () {
    $('#editar-empleado').click(function () {
        var empleadoId = $(this).data('id');

        $.ajax({
            type: 'GET',
            url: `editar/${empleadoId}/`,
            success: function (response) {
                $('#id_nombre').val(response.nombre);
                $('#id_apellido_paterno').val(response.apellido_paterno);
                $('#id_apellido_materno').val(response.apellido_materno);
                $('#id_doc_identidad').val(response.doc_identidad);
                $('#id_correo').val(response.correo);
                $('#id_telefono').val(response.telefono);
                $('#id_area').val(response.area);
                $('#id_cargo').val(response.cargo);
            },
            error: function (xhr, status, error) {
                console.error('Error al obtener los datos del empleado', error);
            }

        });
    });
});
