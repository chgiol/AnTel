import tkinter as tk
import time
import os
import ntpath
from tkinter.filedialog import askopenfilename
from descarga_video import comprobar, descarga_vid
from extract_tweets import extraer_tweets
from limpieza_tweets import limpiar
from video_to_sound import extraer_sonido
from cloud_speech_to_text import subir_sonido, transcribe_gcs
from limpieza_speech import limpiar_spech
from analisis import cargar, extract_trends, genera_tabla


def analisis_auto():
    aut = tk.Tk(className=' Análisis automático')
    aut.geometry('400x300')
    aut.iconbitmap('res/icon2.ico')
    aut.configure(background='#a1dbcd')
    w = tk.Label(aut, text="Buscando y descargando ultima retransmision disponible del telediario de RTVE")
    w.grid(row=0, column=1, padx=10, pady=10)
    aut.update_idletasks()
    aut.update()
    try:
        link, fecha = comprobar()
        ruta_video = descarga_vid(link, fecha)
        w = tk.Label(aut, text="VÍDEO DESCARGADO", height=2)
        w.grid(row=1, column=0, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
    except:
        w = tk.Label(aut, text="Error en la obtencion del video", height=5, fg="red")
        w.grid(row=1, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        aut.mainloop()
    try:
        w = tk.Label(aut, text="Obteniendo ficheros de tweets")
        w.grid(row=2, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        nombre_fichero, ruta = extraer_tweets()
        jroute_tweets = limpiar(nombre_fichero, ruta)

    except:
        w = tk.Label(aut, text="Error en la obtencion de los tweets", height=5, fg="red")
        w.grid(row=2, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        aut.mainloop()
    try:
        w = tk.Label(aut, text="Extrayendo audio a partir del telediario")
        w.grid(row=3, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        archivo_flac = extraer_sonido(ruta_video)
        w = tk.Label(aut, text="Realizando speech to text y obteniendo ficheros")
        w.grid(row=4, column=0, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        url, original_uri = subir_sonido('sonido/' + archivo_flac)
        nombre_texto, ruta_texto = transcribe_gcs(original_uri)
        jroute_speech = limpiar_spech(nombre_texto, ruta_texto)

    except:
        w = tk.Label(aut, text="Error en la conversión audio a texto del telediario", height=5, fg="red")
        w.grid(row=4, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        aut.mainloop()
    try:
        w = tk.Label(aut, text="Generando análisis")
        w.grid(row=5, column=1, padx=0, pady=10)
        aut.update_idletasks()
        aut.update()
        dic_tweets, dic_speech = cargar(jroute_tweets, jroute_speech)
        trends = extract_trends(dic_tweets)
        aup = tk.Tk(className=' Resultados Análisis')
        aup.geometry('400x800')
        aup.iconbitmap('res/icon2.ico')
        aup.configure(background='#a1dbcd')
        for i in range(len(trends)):
            w = tk.Label(aup, text=trends[i])
            w.grid(row=i, column=0, padx=0, pady=10)
            b = tk.Button(aup, text="Resultado",
                          command=lambda i=i: genera_tabla(trends[i], dic_tweets[str(i + 1)], dic_speech))
            b.grid(row=i, column=2, padx=0, pady=10)
            aup.update_idletasks()
            aup.update()
        aup.mainloop()

    except:
        w = tk.Label(aut, text="Error en la generación de los archivos de analisis", height=5, fg="red")
        w.grid(row=2, column=1, padx=0, pady=10, columnspan=2)
        aut.update_idletasks()
        aut.update()
        aut.mainloop()


    return


def descarga_video():  # Busca la retransmision mas reciente de RTVE
    sec = tk.Tk(className=' Descarga')
    sec.geometry('400x300')
    sec.iconbitmap('res/icon2.ico')
    sec.configure(background='#a1dbcd')
    w = tk.Label(sec, text="Buscando ultima retransmision disponible del telediario de RTVE")
    w.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    sec.update_idletasks()
    sec.update()

    link, fecha = comprobar()
    # fecha = 'ewew'
    # link='http://techslides.com/demos/sample-videos/small.mp4'
    if (link != 0):
        def si_butt():
            w = tk.Label(sec, text="Descargando en /videos...(esto puede durar un rato)")
            w.grid(row=4, column=1, padx=0, pady=10, columnspan=2)
            sec.update_idletasks()
            sec.update()
            try:
                descarga_vid(link, fecha)
                w = tk.Label(sec, text="VÍDEO DESCARGADO", height=5)
                w.grid(row=5, column=1, padx=0, pady=10, columnspan=2)
                sec.update_idletasks()
                sec.update()
            except Exception as e:
                print(e)
                w = tk.Label(sec, text="Error en la descarga", bg='red')
                w.grid(row=5, column=1, padx=0, pady=10, columnspan=2)
                sec.update_idletasks()
                sec.update()

        w = tk.Label(sec, text="Se ha encontrado: " + fecha)
        w.grid(row=1, column=1, padx=0, pady=10, columnspan=2)
        w = tk.Label(sec, text="Descargar vídeo?")
        w.grid(row=2, column=1, padx=0, pady=10, columnspan=2)
        b2 = tk.Button(sec, text="Si", command=si_butt)
        b2.grid(row=3, column=1, padx=10, pady=10)
        b3 = tk.Button(sec, text="No", command=lambda: sec.destroy())
        b3.grid(row=3, column=2, padx=0, pady=10)
        sec.mainloop()
    else:
        w = tk.Entry(sec, text="Ha habido un problema con la busqueda")
        w.grid(row=4, column=1, padx=0, pady=10)
        time.sleep(5)
        sec.destroy()
    return


def obtener_tweets():
    try:
        twe = tk.Tk(className=' Obtener tweets')
        twe.geometry('400x300')
        twe.iconbitmap('res/icon2.ico')
        twe.configure(background='#a1dbcd')
        print('Extrayendo....')
        w = tk.Label(twe, text="Descargando tweets...")
        w.grid(row=0, column=0, padx=0, pady=10)
        twe.update_idletasks()
        twe.update()
        # nombre_fichero = 'lololol'
        # ruta = 'yeyye'
        nombre_fichero, ruta = extraer_tweets()
        w2 = tk.Label(twe, text="Fichero de texto en: " + ruta)
        w2.grid(row=1, column=0, padx=0, pady=10)
        twe.update_idletasks()
        twe.update()
        w3 = tk.Label(twe, text="Limpiando tweets y generando json...")
        w3.grid(row=2, column=0, padx=0, pady=10)
        twe.update_idletasks()
        twe.update()
        jroute = limpiar(nombre_fichero, ruta)
        w4 = tk.Label(twe, text="Fichero json en: " + jroute)
        w4.grid(row=3, column=0, padx=0, pady=10)
        twe.mainloop()
    except Exception as e:
        print(e)
        w = tk.Label(twe, text="Error en la obtencion de los tweets", bg='red')
        w.grid(row=5, column=1, padx=0, pady=10, columnspan=2)
        twe.mainloop()
    return


def obtener_audio():
    aud = tk.Tk(className=' Obtener archivos de speech')
    aud.geometry('400x300')
    aud.iconbitmap('res/icon2.ico')
    aud.configure(background='#a1dbcd')
    w = tk.Label(aud, text="Selecciona un archivo de vídeo (formato .mp4) para extraer")
    w.grid(row=0, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    time.sleep(1)

    filename = askopenfilename(parent=aud, initialdir=ntpath.abspath("videos").replace("\\", "/"),
                               title="Selecciona el archivo MP4",
                               filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    w = tk.Label(aud, text="Extrayendo audio con ffmpeg...")
    w.grid(row=1, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    archivo_flac = extraer_sonido(filename)
    w = tk.Label(aud, text="Subiendo archivo a Google Cloud para su analisis...")
    w.grid(row=2, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    url, original_uri = subir_sonido('sonido/' + archivo_flac)
    w = tk.Label(aud, text="Archivo subido, analizando...(esto puede tardar un rato)")
    w.grid(row=3, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    nombre_texto, ruta_texto = transcribe_gcs(original_uri)
    #print(archivo_flac)
    #print(nombre_texto, ruta_texto)
    w = tk.Label(aud, text="Archivo de texto en " + ruta_texto)
    w.grid(row=4, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    w = tk.Label(aud, text="Generando archivo JSON a partir del texto...")
    w.grid(row=5, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    ruta_json = limpiar_spech(nombre_texto, ruta_texto)
    w = tk.Label(aud, text="Archivo generado en " + ruta_json)
    w.grid(row=6, column=0, padx=0, pady=10)
    aud.update_idletasks()
    aud.update()
    return


def analisis_personalizado():
    aup = tk.Tk(className=' Análisis personalizado')
    aup.geometry('400x300')
    aup.iconbitmap('res/icon2.ico')
    aup.configure(background='#a1dbcd')
    w = tk.Label(aup, text="Selecciona el fichero JSON con los tweets")
    w.grid(row=0, column=0, padx=0, pady=10)
    aup.update_idletasks()
    aup.update()
    time.sleep(1)

    json_tweets = askopenfilename(parent=aup, initialdir=ntpath.abspath("json_tweets").replace("\\", "/"),
                                  title="Selecciona el archivo JSON",
                                  filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    w = tk.Label(aup, text="Selecciona el fichero JSON perteneciente al telediario")
    w.grid(row=0, column=0, padx=0, pady=10)
    aup.update_idletasks()
    aup.update()
    time.sleep(1)

    json_speech = askopenfilename(parent=aup, initialdir=ntpath.abspath("json_speech").replace("\\", "/"),
                                  title="Selecciona el archivo JSON",
                                  filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    dic_tweets, dic_speech = cargar(json_tweets, json_speech)
    trends = extract_trends(dic_tweets)
    #print(dic_tweets)
    #print(dic_speech)
    #print(trends)
    aup.destroy()
    aup = tk.Tk(className=' Resultados Análisis')
    aup.geometry('400x800')
    aup.iconbitmap('res/icon2.ico')
    aup.configure(background='#a1dbcd')
    for i in range(len(trends)):
        w = tk.Label(aup, text=trends[i])
        w.grid(row=i, column=0, padx=0, pady=10)
        b = tk.Button(aup, text="Resultado",
                      command=lambda i=i: genera_tabla(trends[i], dic_tweets[str(i + 1)], dic_speech))
        b.grid(row=i, column=2, padx=0, pady=10)
        aup.update_idletasks()
        aup.update()

    aup.mainloop()

    return


def exit():
    tk._exit(0)


def main():
    top = tk.Tk(className=' Herramienta de Análisis de Telediarios Españoles')
    top.geometry('450x300')
    top.iconbitmap('res/icon2.ico')
    top.configure(background='#a1dbcd')

    b1 = tk.Button(top, text="Análisis Automático", command=analisis_auto, fg='#383a39', bg="#21dbc1")
    b1.grid(row=0, column=1, padx=160, pady=10)

    b2 = tk.Button(top, text="Descargar Vídeo", command=descarga_video)
    b2.grid(row=1, column=1, pady=10)

    b3 = tk.Button(top, text="Obtener Tweets", command=obtener_tweets)
    b3.grid(row=2, column=1, pady=10)

    b4 = tk.Button(top, text="Obtener Audio", command=obtener_audio)
    b4.grid(row=3, column=1, pady=10)

    b5 = tk.Button(top, text="Análisis Personalizado", command=analisis_personalizado)
    b5.grid(row=4, column=1, pady=10)

    b6 = tk.Button(top, text="Salir", command=exit)
    b6.grid(row=5, column=1, pady=10)

    top.mainloop()


if __name__ == "__main__":
    main()

