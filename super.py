# 测试super函数，__init__，以便下一步实现单例模式。

class Parent(object):
    def __init__(self, para_1_from_p):  # 首先执行init函数，传入属性para_1
        self.para_1_from_p = para_1_from_p
        print('im init from parent.')
    def funaP(self, para_2_from_p):
        print(para_2_from_p + self.para_1_from_p + 'im funa from parent.')  # para_2是局部变量
    def _funbP(self):
        print('im funb from parent.')
    def __funcP(self):
        print('im func from parent.')

class Child(Parent):
    def __init__(self, para_1_from_c):
        super(Child, self).__init__(para_1_from_c)  # 传入一个属性进去
        self.para_1_from_p = para_1_from_c
        print('im init from Child.')
    def funaC(self):
        print('im funa from child, para_1_from_c is %s' % self.para_1_from_p)
    def funbC(self):
        print('im funb from child.')

# pp = Parent("Jerry")
# pp.funaP("Ma")
# pp.funbP()
cc = Child("ccc")
cc.funaC()
cc.funbC()
cc.funaP("mini")
cc._funbP()
# cc.__funcP()


# http://www.runoob.com/w3cnote/python-super-detail-intro.html