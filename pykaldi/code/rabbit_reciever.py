# !pip install wave
# !pip install vosk
# !pip install json
# !pip install pandas
import pika
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json
import pandas as pd

SetLogLevel(0)
if not os.path.exists("vosk-model-small-ru-0.22"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)
    
df_chunks = pd.DataFrame(columns=['mp4_voice_name',
                                  'voices_chunks_stt'])

os.chdir(u'/models/rus_models')
# print(os.getcwd())

def on_message_received(ch, method, properties, body):
    
    audio = str(body)
    audio = audio.replace("b'", "")
    audio = audio.replace("'", "")
#     print(method)
#     print(audio)
#     body_list.append(string_body)

    wf = wave.open(f'{audio}', "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = Model("vosk-model-small-ru-0.22")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    result = ''
    last_n = False

    while True:
        data = wf.readframes(8000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f" {res['text']}"
    print(result)

# #     audio = audio.replace('.wav', '')
# #     audio_dialogue_id = audio.split('-', 2)[0]
# #     audio_dialogue_id = audio_dialogue_id.replace('rtmp_', '')
# #     audio_user_id = audio.split('-', 2)[1]

# #     try:

# #         df_chunks = df_chunks.append({'mp4_voice_name': audio,
# #                                       'dialog_id': audio_dialogue_id,
# #                                       'user_id': audio_user_id,
# #                                       'voices_chunks_stt': result},
# #                                       ignore_index=True)
# #         print(df_chunks)
# #     except Exception:
# #         print('File contains no speech')
# #     print(df_chunks)

    

if __name__ == '__main__':
    credentials = pika.PlainCredentials('creds', 'creds')
    parameters = pika.ConnectionParameters('ip',
                                       5672,
                                       '/',
                                       credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='files_queue')

    channel.basic_consume(queue='files_queue', auto_ack=True,
        on_message_callback=on_message_received)

    print("Starting Consuming")

    channel.start_consuming()
    
    try:
        on_message_received()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
