# 用修饰器的方法修饰类，其实就是修饰类的函数，但是因为调用类的时候要先调用__init__，所以__init__被修饰，也就起到了单例模式的作用。

def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)

        return _instance[cls]

    return _singleton

def singleton_1(cls):
    def wrapped(*args, **kargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kargs)
        return cls._instance
    return wrapped



@singleton_1
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1.x)
print(a2.x)

# 1 运行a1 = A(2)
# 2 a = 1
# 3 运行__init__
# 4 被修饰器修饰
# 5 定义一个列表instance
# 6 return内部函数
# 7 调用内部函数 这时候cls代表A(2)的__init__
# 8 判断不在里面，所以运行__init__并将其放在列表中
# 9 如果此时在里面，比如A(3)的__init__（他们的__init__代表着同一个class）这时根本不执行cls 也就不调用了