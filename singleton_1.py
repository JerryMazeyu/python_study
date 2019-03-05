# 单例模式参考：https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_0
# 用模块生成单例模式
class Single(object):
    def __init__(self, a):
        print("it is Single __init__.")
        self.a = a
    def foo(self, b):
        print("%s is self.a" % self.a)
        print("%s is b" % b)
single_1 = Single("mzymzymzy")

# 在别的模块中引用其即可
# from singleton_1 import single_1
# print(id(single_1))
# single_1.foo("bbbbb")