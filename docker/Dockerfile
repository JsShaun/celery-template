FROM continuumio/miniconda3:4.10.3-alpine

ENV LANG C.UTF-8 
ENV TZ Asia/Shanghai



COPY ./pip/requirements.txt /usr/src/pip/requirements.txt
RUN pip3 install -r /usr/src/pip/requirements.txt


