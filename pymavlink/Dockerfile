FROM python:3.9-slim-bullseye

#WORKDIR /pymavlink/

RUN apt-get update && pip install pymavlink
RUN pip install pyserial

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:Vinter2023' | chpasswd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo Port 1996 >> /etc/ssh/sshd_config
EXPOSE 1996
#EXPOSE 22

#RUN apt-get -y install wget gpg
#RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
#RUN install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
#RUN sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
#RUN rm -f packages.microsoft.gpg
#RUN apt-get -y install apt-transport-https
#RUN apt-get update && apt-get -y install code

RUN apt-get update && apt-get -y install curl

CMD ["/usr/sbin/sshd", "-D"]
