import emoji
import re
import json
import config


def limpiar(nombre, ruta):
    # Diccionario con las palabras de los tweets formato-> {tt1:{palabra:nº apariciones,...},...}
    DICCIONARIO_TWITTER = {}

    # Expresion regular para hacer match solo con los caracteres que nos interesan
    ALFABETO = re.compile('[^\W_]', re.IGNORECASE)

    # Elimina emogis de un string
    def extract_emojis(linea):
        return ''.join(c for c in linea if c not in emoji.UNICODE_EMOJI)


    archivo_origen = open(ruta, 'r', encoding='utf-8')

    lines = archivo_origen.readlines()
    lines = [line.rstrip('\n') for line in lines]
    tt_numero = 0
    for i in lines:
        if i.startswith('-#123#-'):
            tt = 'tt' + str(tt_numero)
            tt_numero += 1
            # print(tt)
            DICCIONARIO_TWITTER[tt_numero] = {}
            DICCIONARIO_TWITTER[tt_numero]['TRENDING'] = i[8:]
        lista = i.strip().split()

        for palabra in lista:
            palabra = palabra.lower()
            for ch in ['&', '#', '!', '?', '.', ',', '(', ')']:
                if ch in palabra:
                    palabra = palabra.replace(ch, '')

            if len(palabra) == len(ALFABETO.findall(palabra)) > 3 and palabra not in config.FILTRO:
                if palabra in DICCIONARIO_TWITTER[tt_numero]:
                    DICCIONARIO_TWITTER[tt_numero][palabra] += 1
                else:
                    DICCIONARIO_TWITTER[tt_numero][palabra] = 1
    # print(DICCIONARIO_TWITTER['tt1'])
    # print(DICCIONARIO_TWITTER['tt2'])
    # print(DICCIONARIO_TWITTER['tt3'])
    #
    # for i in range(1, 16):
    #     print(DICCIONARIO_TWITTER['tt' + str(i)].pop('TRENDING'))
    #     print(i)
    #     print(sorted(((v, k) for k, v in DICCIONARIO_TWITTER['tt' + str(i)].items()), reverse=True))

    archivo_origen.close()
    nombre = nombre[:-4]
    jroute = 'json_tweets/' + nombre + '.json'
    with open(jroute, 'w', encoding='utf-8') as fp:
        json.dump(DICCIONARIO_TWITTER, fp, indent=4)
    return jroute
    # with open('json_tweets/data.json', 'r', encoding='utf-8') as fp:
    #     data = json.load(fp)
