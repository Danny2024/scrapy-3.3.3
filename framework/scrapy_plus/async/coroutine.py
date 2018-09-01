from gevent.pool import Pool as BasicPool
# 打猴子补丁
from gevent import monkey
monkey.patch_all()


"""
实现自己的协程池
目的:让这个协程池和线程池又一样的接口,一样的异步回调函数，采用适配模式
"""
class Pool(BasicPool):

    # 这个方法就和线程池中的异步方法完全一样
    def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
        # 调用父类的协程池中的异步方法
        super().apply_async(func,args=args,kwds=kwds,callback=callback)

    def close(self):
        """未来即使调用这个函数页不会报错"""
        pass

