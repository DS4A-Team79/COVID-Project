FROM python:3.8

LABEL maintainer="Andy Celdo <andyceldo1@gmail.com>"

WORKDIR /COVID-Project

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./ ./

EXPOSE 8050

CMD ["python", "./application.py"]