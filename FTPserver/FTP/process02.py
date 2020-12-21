"""
包含参数的进程函数
"""
import multiprocessing as mp
from time import sleep

def func01(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")
p1 = mp.Process(target=func01,args=(2,"小泽"))
p2 = mp.Process(target=func01,kwargs={"sec":2,"name":"小泽泽"})
p1.start()
p2.start()
p1.join()
p2.join()

