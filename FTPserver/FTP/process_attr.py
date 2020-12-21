from multiprocessing import Process
from time import sleep
def func1():
    print(f'运行第个进程')
    sleep(2)
    print(f"结束第个进程")
p = Process(target=func1,daemon=True)
p.start()
print(p.name)
print(p.pid)
print(p.is_alive())
print(p.daemon)
p.join()