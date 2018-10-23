# ！user/bin/env python
#---encoding utf-8---
#  author:xudong   time:2018/8/29

import requests
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Lock
import multiprocessing
import time
class MyProcess(Process):
    def __init__(self,loop,lock):
        Process.__init__(self)
        self.loop=loop
        self.lock=lock

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid:'+str(self.pid)+'LoopCount:'+str(count))

if __name__=="__main__":
    lock=Lock()
    for i in range(10,15):
        p=MyProcess(i,lock)
        p.daemon=True
        p.start()
        p.join()
    print("main process ended")