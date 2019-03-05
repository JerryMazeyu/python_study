def makebold(fn):
    print("im here!")
    def wrapped():
        print("im here!!")
        print(fn())
        print(fn(), "hey")
        return "<b>" + fn() + "</b>"
    print("im here!!!")
    return wrapped

def makeitalic(fn):
    print("hi!")
    def wrapped():
        print("hi!!")
        print(fn())
        return "<i>" + fn() + "</i>"
    print("hi!!!")
    return wrapped

@makeitalic
@makebold
def hello():
    return "hello world"

# 运行结果顺序：
# 1 调用内层修饰器makebold 输出 im here!
# 2 定义makebold里面的wrapped 但不调用
# 3 输出 im here!!!
# 4 修饰器是在函数真正调用之前运行 所以现在在makebold修饰后的hello运行前 开始运行makeitalic
# 5 输出 hi!
# 6 定义makeitalic里面的wrapped 但不调用
# 7 输出 hi!!!
# 8 返回的是makeitalic里面的wrapped 因为hello有括号 所以直接调用 输出 hi!!
# 9 调用fn() 这里的fn()是带修饰器的一个hello 也就是makebold里的wrapped
# 10 输出 im here!!
# 11 输出makebold中wrapped里面定义的fn 也就是hello()<hello world>
# 12 输出hello world hey
# 13 返回 <b>hello world</b>
# 14 此时回到makeitalic中的print(fn()) 输出<b>hello world</b>
# 15 返回return "<i>" + fn() + "</i>" 这个时候"<i>" + fn() + "</i>"就是所要的答案
# 16 print(hello()) 输出正确结果