FROM python:latest

WORKDIR /opt/test
COPY test.py ./

CMD ["python", "./test.py"]
