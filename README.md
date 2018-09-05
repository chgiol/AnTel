# AnTel
Programa para el análisis de la relevancia social de los temas tratados en los informativos de televisión de RTVE


Para la correcta instalación de este proyecto se primeramente obtener todos sus archivos desde el repositorio en el que se encuentra. Para esto puede clonarse usando la consola de Github sin necesidad de acceder a la web o bien mediante la web con la opción ‘Download Zip’ lo cual requerirá la descompresión del archivo descargado.
Para la instalación de las diferentes bibliotecas de las que hace uso el programa, se ha proporcionado un fichero ‘requirements.txt’ que contiene todas las necesarias con sus versiones correspondientes. Para realizar la instalación de todas estas bibliotecas de forma fácil se puede usar el gestor de paquetes de Python Pip. Para esto basta con tener el gestor instalado, situarse en la carpeta donde se encuentre ‘requirements.txt’ y ejecutar el comando:

> pip install -r requirements.txt
 
El programa requiere que el usuario registre una cuenta de desarrollo de Twitter, para ello hay que dirigirse a su página para desarroladores  rellenar el formulario de registro y una vez completado dirigirse a la sección Keys and Access Tokens y copiar las llaves correspondientes en el fichero config.py del programa en formato string.
Para el uso de los servicios de Google se requiere una cuenta de desarrollador y para esta cuenta es necesario el uso de una tarjeta de crédito. Teniendo esto en cuenta hay que dirigirse a la pagina de registro de desarrolladores de Google  y una vez efectuado el registro dar permisos a las API de Google Cloud y Google Speech desde el panel de control de la página. Luego hay que dirigirse a la sección de credenciales  y descargar el fichero JSON que las contiene.
La ruta a este archivo debe especificarse en el registro de variables del sistema, esto puede hacerse con el comando:
>set GOOGLE_APPLICATION_CREDENTIALS = [ruta al archivo]
  
Si nos encontramos en un entorno Windows hay que especificar el set de caracteres de Python con el comando:
>set Python_encoding = utf-8
 
Finalmente hay que descargar el programa Ffmpeg para ello hay que dirigirse a su página oficial  descargar el programa y descomprimir el archivo. Finalmente hay que añadir la ruta del ejecutable principal de este programa a la variable ‘Path’ del sistema en el que se vaya a ejecutar la herramienta.
Con esto el programa está listo para usarse.
