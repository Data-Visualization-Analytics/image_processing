FROM python:3.10.5-slim

WORKDIR /image-processing

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/* \

RUN pip3 --no-cache-dir install --upgrade awscli

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

CMD ["python","-u","pipeline/project_image_processing/main.py"]