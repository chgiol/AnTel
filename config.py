import os

# Directorio de trabajo donde se deposita el archivo de sonido
dir_path = os.path.dirname(os.path.realpath(__file__))
'''IMPORTANTE  Si nunca has ejecutado el programa, asegurate de que en /res NO existe el archivo bucket_exists.txt '''

# Tokens necesarios para la api de TWITTER
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Configuración del archivo extract_tweets.py
NUMERO_TRENDS = 15  # Indica el numero de TT's a analizar(1-20)
NUMERO_TWEETS = 20  # Indica el numero de tweets por trend a obtener(min 1)
TIPO_RESULTADO = "popular"  # Tipo de twueets devieltos. 3 opciones: mixed recent popular

#Numero de palabras que aparecen en los graficos de analisis
PALABRAS_GRAFICO=7
#Lista dee palabras a filtrar en la generacion de ambos ficheros json
FILTRO=['como','luego', 'porque','pues','pero','dado', 'sobre','para','esta', 'entre','ahora','sido','tambien']

#Comando para establecer la variable de entorno del archivo .json de las credenciales de google donde [PATH] es la ruta al archivo

#$env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

#$env:GOOGLE_APPLICATION_CREDENTIALS="C:~\tve-speech-to-text-clave.json"
