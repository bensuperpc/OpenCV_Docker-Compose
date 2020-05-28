FROM python:3
LABEL Name=dockerop Version=0.0.1

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD OpenCV_CAM.py OpenCV_CAM.py

CMD python3 OpenCV_CAM.py
