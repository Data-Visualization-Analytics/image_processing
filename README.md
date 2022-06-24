# image_processing<br />
ETL pipeline for image processing<br />

Steps to execute:<br />
1> Install Docker <br />

2> Clone the git repo <br />

#If you want to run and check it in local machine<br />
3> Check if ./downlads and ./images folder are there if not create them <br />

4> ```docker build -t pipeline-new``` <br />

5> Create a docker volume i.e. images-vol <br />

#This volume can be used as our output for the grayscale images<br />
6> ```docker run -d --name test -v image-vol:/image-processing/images/grayscale pipeline:latest``` <br />

7> If you want to change the path you can edit the same in .env file<br />

8> ```docker run pipeline-new``` <br />

#To see the processed files in local <br />

9> ```docker cp <container_id>:path local_path``` <br />
