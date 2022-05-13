# Rabbitmq + Pykaldi

# About project
Представлена реализация ML speech-to-text инструмента API VOSK (KALDI) вместе с RabbitMQ, а также хранилищем AWS S3.

# Start
Зайти на хост и сделать git clone репозитория:
```
git clone https://github.com/paolodeguisse/queue_stt_v2.git
```
Запускаем контейнеры:
```
cd queue_stt_v2
docker-compose build
docker-compose up
docker run -it -p 9000:9000 queue_stt_v2_pykaldi /bin/bash
jupyter notebook --no-browser --ip=* --port=9000 --allow-root
```
Получаем токен для юпитера:
```
http://host:9000/?token=your_token
```

