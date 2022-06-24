#This script does the extraction part
import os
import tarfile
import threading
from decouple import config

class Payload():
    print("Data Extraction in process: \n")
    dir= config("downloadpath")
    s3= config("awscmd")
    urr= config("urr")
    out= config("processed_images_path")
    dir_list= os.listdir("./images/validation")
    def _get(self) -> None:
            pass
            #os.system(s3)
    def _unzip(self) -> None:
            file = tarfile.open(self.urr)
            # extracting file
            file.extractall(self.out)
            file.close()