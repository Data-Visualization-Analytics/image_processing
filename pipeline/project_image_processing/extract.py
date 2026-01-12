import os
import tarfile
import subprocess
from decouple import config
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is a test log")


class Payload:
    def __init__(self):
        logging.info("Data Extraction in process:\n")

        self.aws_cmd = config("awscmd")
        self.output_dir = config("processed_images_path")

        self.download_dir = "/image-processing/download"
        self.validation_dir = "/image-processing/images/validation"
        self.tar_file = f"{self.download_dir}/validation.tar.gz"

        os.makedirs(self.download_dir, exist_ok=True)
        os.makedirs(self.validation_dir, exist_ok=True)

    def get(self) -> None:
        if not os.path.exists(self.tar_file):
            logging.info("Downloading validation dataset...\n")
            subprocess.run(self.aws_cmd, shell=True, check=True)
        else:
            logging.info("File already downloaded...\n")

    def unzip(self) -> None:
        if not os.listdir(self.validation_dir):
            logging.info("Extracting files...\n")
            with tarfile.open(self.tar_file) as tar:
                tar.extractall(self.output_dir)
        else:
            logging.info("Files already extracted.")