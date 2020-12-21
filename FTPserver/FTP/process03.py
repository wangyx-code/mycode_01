"""
多个子进程
"""
from multiprocessing import Process
import os,sys
import time
def func01():
    time.sleep(3)
    print("小泽一号")
    print(os.getpid(),"------",os.getppid())
def func02():
    time.sleep(2)
    print("小泽二号")
    print(os.getpid(),"------",os.getppid())
def func03():
    time.sleep(4)
    sys.exit("小泽四号")
    print("小泽三号")
    print(os.getpid(),"------",os.getppid())
list01 = []
for item in [func01,func02,func03]:
    p = Process(target=item)
    list01.append(p)
    p.start()
[item.join() for item in list01]


