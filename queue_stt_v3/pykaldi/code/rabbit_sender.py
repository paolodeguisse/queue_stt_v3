# !pip install pika
# !pip install moviepy
import pika
import os
from moviepy.editor import *

directory = u'/models/rus_models'
files = os.listdir(directory) # имена всех файлов папки в 

# directory_output = u'/models/rus_models'

files.remove('vosk-model-ru-0.22')
files.remove('vosk-model-small-ru-0.22')
# print('\n'.join(files)) # выводим список имен

# Set the connection parameters to connect to rabbit-server1 on port 5672
# on the / virtual host using the username "guest" and password "guest"
credentials = pika.PlainCredentials('creds', 'creds')
parameters = pika.ConnectionParameters('ip',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='files_queue')

for file in files:
    channel.basic_publish(exchange='', routing_key='files_queue', body=file)
    print(file)
connection.close()
