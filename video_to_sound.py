import os
import ntpath


#EL PROGRAMA PUEDE TENER INPUT DE UNA URL

def extraer_sonido(ruta):
    try:
        ruta = '"' + ruta + '"'
        nombre_archivo = ntpath.basename(ruta)[:-4] + 'flac'
        os.system(
            "ffmpeg -y -i " + ruta + " -ar 16000 -ss 00:00:05 -t 01:00:00.0 -ac 1 -q:a 0 -map a sonido/" + nombre_archivo)
        return nombre_archivo

    except Exception as e:
        print('Error en la conversion a sonido del archivo de video: '+e)



#extraer_sonido(ruta)
