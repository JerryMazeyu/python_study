# 这个模块显示了类的继承顺序。

class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3

class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4

class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5

#下列代码输出什么结果呢
d = D()
d.add(2)
print(d.n)

# 1.调用D，print('self is {0} @D.add'.format(self))
# 2.执行到super，调用B，执行print('self is {0} @B.add'.format(self))
#   执行到super，调用C
# 3.执行print('self is {0} @C.add'.format(self))
#   执行到super，调用A
#   print('self is {0} @A.add'.format(self))
#   self.n+=2,now self.n=7
# 4.回到C,self.n+=4,now self.n=11
# 5.回到B，self.n+=3,now self.n=14
# 6.回到D，self.n+=5,now self.n=19