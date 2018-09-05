import re
import json
import config


def limpiar_spech(nombre, ruta):
    DICCIONARIO_SPEECH = {}

    # Expresion regular para hacer match solo con los caracteres que nos interesan
    ALFABETO = re.compile('[^\W_]', re.IGNORECASE)

    archivo_origen = open(ruta, 'r', encoding='utf-8')

    lines = archivo_origen.readlines()
    lines = [line.rstrip('\n') for line in lines]
    for i in lines:
        lista = i.strip().split()
        for palabra in lista:
            palabra_orig = palabra
            palabra = palabra.lower()
            if len(palabra) == len(ALFABETO.findall(palabra)) and len(palabra) > 3 and palabra not in config.FILTRO:
                if (palabra in DICCIONARIO_SPEECH):
                    DICCIONARIO_SPEECH[palabra] += 1
                else:
                    if palabra_orig[0].isupper():
                        DICCIONARIO_SPEECH[palabra] = 4
                    else:
                        DICCIONARIO_SPEECH[palabra] = 1

    archivo_origen.close()

    nombre = nombre[:-4]
    jroute = 'json_speech/' + nombre + '.json'
    with open(jroute, 'w', encoding='utf-8') as fp:
        json.dump(DICCIONARIO_SPEECH, fp, indent=4)
    return jroute

# limpiar_spech('speech_Telediario-21horas-25_08_18.txt','raw_speech/speech_Telediario-21horas-25_08_18.txt')
