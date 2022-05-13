FROM pykaldi/pykaldi as pykaldi_img_1
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install python3-pip -y && \
    apt-get install python3-venv -y && \
    apt-get install python3.8 -y
    
RUN ln -sf /usr/bin/python3.8 /usr/bin/python3
RUN ln -sf /usr/bin/python3.8 /usr/bin/python
RUN python -m pip install --upgrade pip
    
    
RUN apt-get install libpq-dev -y && \
    apt-get install libpq5 -y && \
    apt-get install awscli -y && \
    apt-get install git -y && \
    apt install ffmpeg -y && \
    pip3 install pika && \
    pip3 install moviepy && \
    pip3 install wave && \
    pip3 install vosk && \
    pip3 install pandas && \
    pip install psycopg2-binary && \
    pip install jupyterlab
            

RUN mkdir -p /models/rus_models
RUN chdir /models/rus_models && \
    wget https://alphacephei.com/kaldi/models/vosk-model-ru-0.22.zip && \
    unzip vosk-model-ru-0.22.zip && \
    rm vosk-model-ru-0.22.zip && \
    wget https://alphacephei.com/kaldi/models/vosk-model-small-ru-0.22.zip && \
    unzip vosk-model-small-ru-0.22.zip && \
    rm vosk-model-small-ru-0.22.zip



FROM pykaldi/pykaldi as pykaldi_img_2
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install python3-pip -y && \
    apt-get install python3-venv -y && \
    apt-get install python3.8 -y
    
RUN ln -sf /usr/bin/python3.8 /usr/bin/python3
RUN ln -sf /usr/bin/python3.8 /usr/bin/python
RUN python -m pip install --upgrade pip
    
    
RUN apt-get install libpq-dev -y && \
    apt-get install libpq5 -y && \
    apt-get install awscli -y && \
    apt-get install git -y && \
    apt install ffmpeg -y && \
    pip3 install pika && \
    pip3 install moviepy && \
    pip3 install wave && \
    pip3 install vosk && \
    pip3 install pandas && \
    pip install psycopg2-binary && \
    pip install jupyterlab
            

RUN mkdir -p /models/rus_models
RUN chdir /models/rus_models && \
    wget https://alphacephei.com/kaldi/models/vosk-model-ru-0.22.zip && \
    unzip vosk-model-ru-0.22.zip && \
    rm vosk-model-ru-0.22.zip && \
    wget https://alphacephei.com/kaldi/models/vosk-model-small-ru-0.22.zip && \
    unzip vosk-model-small-ru-0.22.zip && \
    rm vosk-model-small-ru-0.22.zip
