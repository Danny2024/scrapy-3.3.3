from multiprocessing.dummy import Pool

# 创建线程对象,如果不指定个数就是当前cpu的核数
import time

# 两个线程，三个异步任务
pool = Pool(2)


def task(msg):
    print(msg)

# 回调解决线程池的线程少于需要线程数的问题

# 开三个线程递归,
# 把task放到递归里面执行

def task_callback_1(temp):
    pool.apply_async(task,args=('线程1',),callback=task_callback_1)

def task_callback_2(temp):
    pool.apply_async(task,args=('线程2',),callback=task_callback_2)

def task_callback_3(temp):
    pool.apply_async(task,args=('线程3',),callback=task_callback_3)



pool.apply_async(task,args=('1',),callback=task_callback_1)
pool.apply_async(task,args=('2',),callback=task_callback_2)
pool.apply_async(task,args=('3',),callback=task_callback_3)

time.sleep(10)

