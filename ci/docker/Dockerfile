FROM debian:stable

RUN \
   apt update -y && \
   apt install -y wget git

COPY frkl-name /usr/bin/frkl-name

RUN \
   chmod +x /usr/bin/frkl-name
