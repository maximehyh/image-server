FROM python:3.9.7-bullseye

# Required to use OpenCV in case you eventually need to add it
# RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

# Setting up enviroment
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY src ./src
WORKDIR /app/src
