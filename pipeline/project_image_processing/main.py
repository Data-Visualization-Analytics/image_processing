from extract import Payload
from transform import Mapper
from load import Store
from threading import Thread

if __name__=="__main__":
    Yep = Payload()
    t1=Thread(target=Yep.get())
    t2=Thread(target=Yep.unzip())
    t3=Thread(target=Mapper)
    t4=Thread(target=Store)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
