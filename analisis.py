import json
from config import PALABRAS_GRAFICO as PG
import numpy as np
import matplotlib.pyplot as plt


def cargar(tweets='json_tweets/tweets27_08_18-03-58.json',
           speech='json_speech/speech_Telediario-21horas-25_08_18.json'):
    with open(tweets, 'r', encoding='utf-8') as fp:
        DIC_TWETS = json.load(fp)
    with open(speech, 'r', encoding='utf-8') as fp:
        DIC_SPEECH = json.load(fp)
    # print(DIC_SPEECH)
    # print(DIC_TWETS)
    return DIC_TWETS, DIC_SPEECH


# Elimina el elemento TRENDING de los diccionarios de tweets
def extract_trends(dic_tweets):
    lista_trends = []
    for trend in dic_tweets:
        lista_trends.append(dic_tweets[trend]['TRENDING'])
        del dic_tweets[trend]['TRENDING']
    return lista_trends


def genera_tabla(trend, dic_tweets, dic_speech):
    # print(trend)
    # print(dic_tweets)
    tweet_list = sorted(dic_tweets.items(), key=lambda x: x[1], reverse=True)
    # speech_list = sorted(dic_speech.items(), key=lambda x: x[1], reverse=True)
    # tw_palabras = (x[0] for x in tweet_list[:PG])
    # tw_ocurrencias = (x[1] for x in tweet_list[:PG])
    tw_palabras, tw_ocurrencias = map(list, zip(*tweet_list[:PG]))
    sp_ocurrencias = []
    for palabra in tw_palabras:
        if palabra in dic_speech:
            sp_ocurrencias.append(dic_speech[palabra])
        else:
            sp_ocurrencias.append(0)
    datos = [tw_ocurrencias, sp_ocurrencias]
    # print(datos)
    plt.clf()
    X = np.arange(PG)
    plt.title(trend, bbox={"facecolor": "0.8", "pad": 5})
    plt.xlabel('Palabras')
    plt.ylabel('Ocurrencias')
    p1 = plt.bar(X + 0.00, datos[0], color="b", width=0.25)
    p2 = plt.bar(X + 0.25, datos[1], color="g", width=0.25)
    plt.xticks(X + 0.38, tw_palabras, rotation=30)
    plt.legend((p1, p2), ('Twitter', 'Telediario'))
    plt.show()

    return
