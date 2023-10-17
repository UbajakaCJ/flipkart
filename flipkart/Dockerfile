# FROM ubuntu:22.04

# RUN apt update \
#     && apt install -y htop python3-dev \
#     && apt install python3-pip pip wget

# COPY . src/

# RUN /bin/bash -c "cd src \
#     && python3-pip install -r requirements.txt"

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ml_scripts/ .

CMD python store_data.py && python etl_process.py && python train_model.py && python inference.py

