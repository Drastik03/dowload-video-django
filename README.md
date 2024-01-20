# DOWLOAD-VIDEO-DJANGO

Este proyecto descarga videos de calidad de la plataforma youtube de manera rapida... Posteriormente se quiere implementar para las demas plataformas.
## Instalación

1. Crea y activa un entorno virtual (asegúrate de tener `virtualenv` instalado):

    ```bash
    # Instala virtualenv si aún no lo tienes
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate  # Para sistemas basados en Unix
    # o
    .\venv\Scripts\activate  # Para sistemas basados en Windows
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
3. Aplica las migraciones:

    ```bash
    python manage.py migrate
    ```

## Configuración

Asegúrate de configurar adecuadamente tu archivo `settings.py` con los valores correctos para la base de datos, claves secretas, etc.

## Uso

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
