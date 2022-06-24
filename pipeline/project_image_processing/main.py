"Flow for the image processing pipeline"
from threading import Thread
import extract,transform, load

if __name__ == "__main__":
    Yep = extract.Payload()
    thread = Thread(target = Yep._get())
    thread2 = Thread(target = Yep._unzip())
    thread.start()
    thread.join()
    thread2.start()
    transform.Mapper()
    print('Finished')
