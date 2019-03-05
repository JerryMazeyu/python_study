# 类方法是一种在类中但对类进行交互的方法，不同于实例方法，类方法第一个参数是cls。

class Singleton(object):

    def __init__(self, x):
        self.x = x

    @classmethod
    def instance(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            print("im here")
            # cls._instance = Singleton(*args, **kargs)
            cls._instance = object.__new__(cls)
        else:
            print("im here!!")
            # print(cls._instance)
            # print(getattr(cls, "_instance"))
        return cls._instance

a1 = Singleton.instance(2)
a2 = Singleton.instance(4)
print(a1 is a2)  # True
print(a2)  # 2
print(a2.x)  # 依旧是 2
