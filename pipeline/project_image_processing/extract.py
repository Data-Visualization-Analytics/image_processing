#This script does the extraction part
import os
import tarfile
from decouple import config

class Payload():
    print("Data Extraction in process: \n")
    dir= config("downloadpath")
    s3= config("awscmd")
    urr= config("urr")
    out= config("processed_images_path")
    dir_list= os.listdir("./images/")
    def get(self) -> None:
        if os.listdir("./download")==[]:
            os.system(self.s3)
        else:
            print("File already received ...")
    def unzip(self) -> None:
            file = tarfile.open(self.urr)
            # extracting file
            file.extractall(self.out)
            file.close()

if __name__ == "__main__":
    Yep = Payload()
    Yep.get()
    Yep.unzip()