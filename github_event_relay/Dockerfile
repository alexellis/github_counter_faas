FROM resin/rpi-raspbian:latest

RUN apt-get update -qy && apt-get install -qy \
  python-pip \
  python \
  python-scrollphat
RUN pip install requests

ENTRYPOINT []
WORKDIR /root/

ADD https://github.com/alexellis/faas/releases/download/v0.5-alpha/fwatchdog-armhf /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

ENV fprocess "python ./handler.py"
COPY *.py ./

CMD [ "/usr/bin/fwatchdog"]
