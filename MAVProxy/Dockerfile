FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get -y install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame
RUN pip3 install PyYAML mavproxy --user
RUN echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc

WORKDIR /root/

ENTRYPOINT [".local/bin/mavproxy.py"]
CMD ["--master=/dev/ttyACM0"]
