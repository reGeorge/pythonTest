'''
代码是由主进程里面的主线程从上到下执行的,
我们在主线程里面又创建了两个子进程，子进
程里面也是子线程在干活，这个子进程在主进
程里面
'''
import multiprocessing
from multiprocessing import Process
import time
 
def f0(a1):
	name1 = input('name')
    time.sleep(3)
    print(a1)


li = []
 
def f1(i):
    li.append(i)
    print('你好',li)
 
if __name__ =='__main__':#进程不能共用内存
    for i in range(10):
        p = Process(target=f1,args=(i,))
        p.start()    

# if __name__ == '__main__':#windows下必须加这句
 
#     t = multiprocessing.Process(target=f0,args=(12,))
#     t.daemon=True#将daemon设置为True，则主线程不比等待子进程，主线程结束则所有结束
#     t.start()
 
#     t2 = multiprocessing.Process(target=f0, args=(13,))
#     t2.daemon = False
#     t2.start()
 
#     print('end')#默认情况下等待所有子进程结束，主进程才结束

