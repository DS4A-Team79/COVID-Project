FROM python:3.8
LABEL maintainer="Andy Celdo <andyceldo1@gmail.com>"

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /covid-project
WORKDIR /covid-project
COPY ./ ./

EXPOSE 8050
CMD ["python", "./application.py"]