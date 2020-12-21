"""
进程模块使用  基础示例
"""
import multiprocessing as mp
from time import sleep

# 进程执行函数
def func1(a,b):
    print(f'运行第{a}个进程')
    sleep(2)
    print(f"结束第{b}个进程")

def func2(a,b):
    print(f'运行第{a}个进程')
    sleep(3)
    print(f"结束第{b}个进程")

# 实例化进程对象
p1 = mp.Process(target = func1,args=(1,1))
p2 = mp.Process(target=func2,args=(2,2))
# 启动进程
p1.start()
p2.start()
# 阻塞等待
p1.join()
p2.join()

