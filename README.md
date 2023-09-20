# Weather App

Este es un proyecto de una aplicación de pronóstico del clima construida en Python utilizando la librería Tkinter para la interfaz gráfica de usuario. La aplicación permite a los usuarios buscar el clima actual de una ciudad específica y proporciona información detallada sobre la temperatura, la condición climática, la humedad, la probabilidad de lluvia y la velocidad del viento.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `tkinter`: La biblioteca estándar de Python para crear interfaces gráficas de usuario.
- `os`: Utilizada para gestionar rutas de archivos y directorios.
- `datetime`: Para trabajar con fechas y horas.
- `pytz`: Para manejar zonas horarias.
- `requests`: Para realizar solicitudes HTTP a una API de pronóstico del clima.
- `PIL`: La biblioteca Python Imaging Library para trabajar con imágenes.
- `geopy`: Utilizada para geocodificar la ubicación ingresada por el usuario.
- `timezonefinder`: Para determinar la zona horaria de la ubicación.
- `googletrans`: Para traducir las condiciones climáticas del inglés al español.

## Uso

1. Ejecuta el archivo Python `weather_app.py`.
2. La ventana de la aplicación se abrirá, y verás un campo de búsqueda en la parte superior.
3. Ingresa el nombre de la ciudad para la cual deseas obtener el pronóstico del clima y presiona el botón de búsqueda.
4. La aplicación mostrará información actualizada sobre el clima en esa ciudad, incluyendo la temperatura, la condición climática, la humedad, la probabilidad de lluvia y la velocidad del viento.

## Características

- **Búsqueda de Ciudades**: Permite a los usuarios ingresar el nombre de la ciudad de su interés.
- **Zona Horaria Local**: Muestra la hora local de la ciudad seleccionada.
- **Detalles del Clima**: Proporciona detalles como temperatura, humedad, probabilidad de lluvia y velocidad del viento.
- **Traducción**: Traduce automáticamente la condición climática del inglés al español.
- **Interfaz de Usuario Gráfica**: Ofrece una interfaz gráfica fácil de usar.

## Capturas de Pantalla

![Captura de Pantalla 1](screenshots/screenshot1.png)
![Captura de Pantalla 2](screenshots/screenshot2.png)

## Notas

- Asegúrate de tener una conexión a Internet activa para que la aplicación pueda obtener datos de pronóstico del clima.
- La información sobre el clima se actualiza en tiempo real.
- La aplicación está diseñada para funcionar con una clave de API de OpenWeatherMap. Asegúrate de obtener tu propia clave API y reemplazarla en la variable `api` dentro del código.
- La precisión de los datos del clima depende de la disponibilidad y calidad de los datos proporcionados por la API de OpenWeatherMap.

¡Disfruta de tu experiencia de pronóstico del clima con la Weather App!
