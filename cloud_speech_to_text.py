import io
import os
import config
import gcloud_snipets
from pathlib import Path
import ntpath
import time

# Imports the Google Cloud client library
from google.cloud import speech

from google.cloud.speech import enums
from google.cloud.speech import types


# Instantiates a client
# client = speech.SpeechClient()

def subir_sonido(ruta):
    my_file = Path("res/bucket_exists.txt")
    nombre_archivo = ntpath.basename(ruta)

    if (my_file.is_file()):
        gcloud_snipets.upload_blob('tve-bucket', ruta, nombre_archivo[:-5])

        url = gcloud_snipets.generate_signed_url('tve-bucket', nombre_archivo[:-5])
        original_uri = 'gs://tve-bucket/' + nombre_archivo[:-5]

        # gcloud_snipets.list_blobs('tve-bucket')
    else:
        # Creamos el bucket
        gcloud_snipets.create_bucket('tve-bucket')
        # Creamos el archivo para no volver a crear el bucket
        aux = open("res/bucket_exists.txt", "w+")
        aux.close()

        gcloud_snipets.upload_blob('tve-bucket', ruta, nombre_archivo[:-5])

        url = gcloud_snipets.generate_signed_url('tve-bucket', nombre_archivo[:-5])
        original_uri='gs://tve-bucket/'+nombre_archivo[:-5]

        # gcloud_snipets.list_blobs('tve-bucket')
    return url, original_uri


def transcribe_gcs(gcs_uri='gs://tve-bucket/Telediario-21horas-25_08_18'):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    # Instantiates a client
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='es-ES')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result()  # timeout=90

    # Creamos archivo donde guardar el speech
    nombre_fichero = 'speech_' + ntpath.basename(gcs_uri) + '.txt'
    ruta = 'raw_speech/' + nombre_fichero
    f = open(ruta, 'w', encoding='utf-8')

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(result.alternatives[0].transcript, file=f)
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        print('Confidence: {}'.format(result.alternatives[0].confidence))
    f.close()
    return nombre_fichero, ruta

# transcribe_gcs('gs://tve-bucket/sonido_subido2')  # las Uris con este formato-> gs://bucket_name/object_name


