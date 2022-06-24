#This script does the extraction part
import os
import tarfile
from decouple import config

class Payload:
    print("Data Extraction in process: \n")
    dir= config("downloadpath")
    s3= config("awscmd")
    urr= config("urr")
    out= config("processed_images_path")
    def get(self) -> None:
        if os.listdir("./download")==[]:
            os.system(self.s3)
        else:
            print("\n File already received ...\n")
    def unzip(self) -> None:
        if os.listdir("./images/validation")==[]:
                file = tarfile.open(self.urr)
                # extracting file
                file.extractall(self.out)
                file.close()
        else:
            print("\nfiles already unzipped...\n")
