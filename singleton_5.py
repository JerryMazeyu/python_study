# 利用__new__方法实现单例模式。
import threading
class Singleton(object):
    lock = threading.RLock()
    def __init__(self, x):
        self.x = x
        print(self.x)
    def __new__(cls, *args, **kwargs):
        with Singleton.lock:  # 这个写法很有东西，在能获取锁的时候获取锁，执行之后释放锁
            if hasattr(cls, '_instance'):  # 这句判断是否有实例
                print("im here!")
                pass
            else:
                print("im here!!!")
                cls._instance = object.__new__(cls)  # 如果没有，此类的实例运行object的new方法创建实例，这里的cls指Singleton
        return cls._instance  # cls._instance指这个类的这个实例。

a = Singleton(2)
b = Singleton(3)
print(a.x)
print(b.x)
