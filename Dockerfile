FROM ubuntu

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update;apt-get install python3.6 -y; apt-get install python3-pip -y
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update;apt-get install transmission-cli -y

COPY . .

CMD ["python3", "run.py"]