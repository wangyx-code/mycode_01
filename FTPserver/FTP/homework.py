"""
      3. 编写程序求 100000以内质数之和
         编写一个装饰器求 这个过程的时间

         使用4个进程做同样的事情，求时间
         使用10个进程做同样的事情，求时间
"""
import time
def run_time(func):
    def wrapper(*args,**kwargs):
        stime = time.time()
        res = func(*args, **kwargs)
        etime = time.time()
        rtime = etime-stime
        return res,rtime
    return wrapper
@run_time
def count():
    list01 = [2]
    for i in range(3,100000):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            list01.append(i)
    result = sum(list01)
    return result,list01
print(count())
