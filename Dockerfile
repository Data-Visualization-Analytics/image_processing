FROM python:3.10.5-slim as builder

RUN pip3 --no-cache-dir install --upgrade awscli

WORKDIR /image-processing

COPY requirements.txt .
COPY ./pipeline ./pipeline
COPY ./.env ./.env

#comment below line to download data from s3 source again and run pipeline
#COPY ./download ./download
RUN mkdir -p ./images/grayscale ./images/validation ./download
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python","pipeline/project_image_processing/extract.py","pipeline/project_image_processing/transform.py","pipeline/project_image_processing/load.py"]