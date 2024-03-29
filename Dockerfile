FROM nikolaik/python-nodejs:latest
RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/
COPY . /app
WORKDIR /app
RUN chmod 777 /app
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD ["python3", "main.py"]
