
FROM python:3.7

RUN mkdir /app 
WORKDIR /app
ADD . /app

RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["python service.py"]

