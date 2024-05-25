# DJANGO CRUD
Desarrollo de crud para edicion de empleados, con ventanas modales, alerts de django y la libreria SweetAlert2: https://sweetalert2.github.io/

## Instalación

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/EmanuelCG/django_crud.git
    ```

2. Crea un entorno virtual para el proyecto:

    ```bash
    cd tu_proyecto
    python -m venv venv
    ```

3. Activa el entorno virtual:

    En Windows:

    ```bash
    venv\Scripts\activate
    ```

    En macOS y Linux:

    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

5. Aplica las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Crea un superusuario para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser
    ```

7. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

8. Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver tu aplicación en funcionamiento.

## Uso

Libre uso ☕

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz tus cambios y commitea tus modificaciones (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Crea una solicitud de extracción en GitHub.

## Licencia

Este proyecto está bajo la Licencia [MIT](https://opensource.org/licenses/MIT). Consulta el archivo `LICENSE` para obtener más detalles.
