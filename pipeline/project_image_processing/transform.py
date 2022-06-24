#This script does the processing part
from os import listdir
from PIL import Image
from decouple import config

class Mapper():
    print("Data transformation in process: \n")
    directory = config("processed_images_path")

    fnames = list(fname for fname in listdir(directory) if fname.endswith('.jpg'))
    
    batchsize = 500
    l_index, r_index = 0, batchsize
    batch = fnames[l_index:r_index]

    def batchFunc(file: str):
        if(file.find("._")==-1):
            img = Image.open('./images/validation/'+file)
            imgGray = img.convert('L')
            imgGray.save('./images/grayscale/'+file)
            print(imgGray)

    while batch:
        for i in batch:
            batchFunc(i) 
        l_index, r_index = r_index, r_index + batchsize
        batch = fnames[l_index:r_index]
