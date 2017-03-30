FROM resin/rpi-raspbian:latest

RUN apt-get update -qy && apt-get install -qy \
  python-pip \
  python \
  python-scrollphat
RUN pip install redis
ENTRYPOINT []
WORKDIR /root/

COPY *.py ./

CMD ["python", "display.py", "http://192.168.0.54:9090/"]
