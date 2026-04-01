FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip

CMD ["python3", "/app/bind_mount/ishappy.py"]