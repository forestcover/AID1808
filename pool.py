from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()
# 创建进程池

pool = Pool(processes = 3)

result = []
#  向进程池添加事件
for i in range(10):
    msg = "hello %d"%i
    # 异步执行
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r) #　存储函数时间对象
    #　同步执行，＝逐个执行
    # pool.apply(func = worker,args = (msg,))
    
# 关闭进程池
pool.close()
# 回收进程池
pool.join()
for i in result:
    # 获取进程时间函数返回值
    print(i.get())