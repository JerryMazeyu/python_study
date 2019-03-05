def func_args(pre='xiaoqiang'):
    def w_test_log(func):
        def inner():
            print('...记录日志...visitor is %s' % pre)
            func()
        return inner
    return w_test_log


# 带有参数的修饰器能够起到在运行时，有不同的功能

# 先执行func_args('wangcai')，返回w_test_log函数的引用
# @w_test_log
# 使用@w_test_log对test_log进行修饰
@func_args('wangcai')
def test_log():
    print('this is test log')


test_log()

def decorator(a = "mzy"):  # 修饰器参数层
    print("111")
    def wrap(func):  # 修饰器层
        print("222")
        def inner(b):  # 被修饰参数层
            print("333")
            return a + func(b) + a
        return inner
    print("444")
    return wrap

@decorator("lhq")
def prt(x):
    return x

print(prt("7"))

def decorator_2(func):
    def wrap(x):
        print("hi!")
        return func(x)
    return wrap

@decorator_2
def hi(x):
    return x
print(hi('lhq'))