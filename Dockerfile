FROM python:3.8

WORKDIR /SpamBot

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .


CMD ["python","-u", "main.py"]