FROM python:3-slim
WORKDIR /code
COPY requirements.txt .
RUN apt update && apt install -y build-essential
RUN mkdir log; pip3 install -r requirements.txt

COPY csp_reporter.py ./

EXPOSE 6000
CMD python csp_reporter.py
