# Usar una imagen base de Python
FROM python:3.9-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el código de la aplicación al contenedor
COPY . .

# Instalar las dependencias necesarias
RUN pip install Flask Flask-Cors gunicorn

# Exponer el puerto que usará la aplicación
EXPOSE 5000

# Usar Gunicorn para correr la aplicación Flask en modo producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
