FROM ubuntu:latest
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev libpq-dev
COPY . /app
RUN pip install -r setup.txt
EXPOSE 8080
CMD ["python3", "main.py"]
