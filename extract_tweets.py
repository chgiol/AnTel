
import sys
import config
import time

sys.path.append(".")


# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

# IMPORTANTE PONER EN CONSOLA EL COMANDO set PYTHONIOENCODING=utf-8 o bien poner la variable de entorno directamente
def extraer_tweets(ruta='raw_tweets/'):
    import twitter

    numero_trends = config.NUMERO_TRENDS  # Indica el numero de TT's a analizar(1-20)
    numero_tweets = config.NUMERO_TWEETS  # Indica el numero de tweets por trend a obtener(min 1)
    tipo_resultado = config.TIPO_RESULTADO  # Tipo de twueets devieltos. 3 opciones: mixed recent popular

    auth = twitter.oauth.OAuth(config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET,
                               config.CONSUMER_KEY, config.CONSUMER_SECRET)

    fecha = time.strftime("%d_%m_%y-%H-%M", time.gmtime())
    nombre_fichero = 'tweets' + fecha + '.txt'
    ruta = ruta + nombre_fichero
    f = open(ruta, 'w', encoding='utf-8')  # Archivo donde escribir los tweets parseados

    # Initiate the connection to Twitter REST API
    twitter = twitter.Twitter(auth=auth)

    # Devuelve objeto con todos los TTs de españa
    esp_trends = twitter.trends.place(_id=23424950)

    for location in esp_trends:
        for trend in location["trends"][:numero_trends]:
            # print(trend)

            print("-#123#- %s" % trend["name"], file=f)
            print('', file=f)

            # Devuelve un diccionario de dos llaves: metadatos de la busqueda i lista de tweets en forma de diccionarios
            search_results = twitter.search.tweets(q=trend["name"], count=numero_tweets, lang="es",
                                                   result_type=tipo_resultado,
                                                   include_entities=1, tweet_mode="extended")

            statuses = search_results['statuses']  # La chicha
            # metadata = search_results['search_metadata']

            for tweet in statuses:
                print(tweet['full_text'], file=f)

    f.close()
    return nombre_fichero, ruta


'''


  'country': 'Spain',
  'countryCode': 'ES',
  'name': 'Spain',
  'parentid': 1,
  'placeType': {'code': 12, 'name': 'Country'},
  'url': 'http://where.yahooapis.com/v1/place/23424950',
  'woeid': 23424950},
  '''
