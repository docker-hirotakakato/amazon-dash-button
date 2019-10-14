FROM alpine:latest

RUN apk add --no-cache curl scapy tcpdump

COPY amazon-dash-button.py /

ENTRYPOINT ["/amazon-dash-button.py"]
