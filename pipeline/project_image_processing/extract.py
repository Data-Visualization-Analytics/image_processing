import os
import tarfile
import subprocess
from decouple import config


class Payload:
    def __init__(self):
        print("Data Extraction in process:\n")

        self.aws_cmd = config("awscmd")
        self.output_dir = config("processed_images_path")

        self.download_dir = "/image-processing/download"
        self.validation_dir = "/image-processing/images/validation"
        self.tar_file = f"{self.download_dir}/validation.tar.gz"

        os.makedirs(self.download_dir, exist_ok=True)
        os.makedirs(self.validation_dir, exist_ok=True)

    def get(self) -> None:
        if not os.path.exists(self.tar_file):
            print("Downloading validation dataset...\n")
            subprocess.run(self.aws_cmd, shell=True, check=True)
        else:
            print("File already downloaded...\n")

    def unzip(self) -> None:
        if not os.listdir(self.validation_dir):
            print("Extracting files...\n")
            with tarfile.open(self.tar_file) as tar:
                tar.extractall(self.output_dir)
        else:
            print("Files already extracted.")