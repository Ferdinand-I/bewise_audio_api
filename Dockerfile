FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y ffmpeg libavcodec-extra

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./audio_api .