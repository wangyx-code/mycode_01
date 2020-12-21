"""
将一个文件拆分为两部分
要求拆分过程同步执行
"""
from multiprocessing import Process
import os

size01 = os.path.getsize("test01.txt")
file01 = open("test01.txt", "r")

def split01():
    # file01 = open("test01.txt", "r")
    file02 = open("split01.txt", "w")
    size02 = size01 // 2
    while size02 >= 5:
        data = file01.read(5)
        file02.write(data)
        size02 -= 5
    else:
        data = file01.read(size02)
        file02.write(data)


def split02():
    # file01 = open("test01.txt", "r")
    size02 = size01 // 2
    file01.seek(size02, 0)
    file02 = open("split02.txt", "w")
    while True:
        data = file01.read(5)
        if not data:
            break
        file02.write(data)


p1 = Process(target=split01)
p2 = Process(target=split02)
p1.start()
p2.start()
p1.join()
p2.join()
