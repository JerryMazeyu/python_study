# 利用condition类建立生产-消费模型，假设B在吃海底捞，
# 而A是服务生，负责帮忙放鱼丸，每次放入2个鱼丸，下入了鱼丸就通知A去吃。
# B需要2秒或者1秒吃掉一个鱼丸，没有鱼丸了就通知A去下进去。

# 需要注意的是，在进行复杂多进程时，最好将每个方法写进一个类，继承threading.Thread即可。
# 其中涉及三种方法：acquire()、release() 两个方法继承了lock。
# wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
# notify(): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。

import threading, time, random
num = 0
con = threading.Condition()
class Consume(threading.Thread):
    def __init__(self):
        super(Consume, self).__init__()
    def run(self):
        time.sleep(1)
        global num
        while True:
            if con.acquire():
                if num > 0:
                    num -= 1
                    print("丸子还有%s个。" % num)
                    con.notify()
                    con.release()
                else:
                    print("没丸子了。")
                    con.wait()
            eat_time = random.randint(1, 2)
            time.sleep(eat_time)

class Produce(threading.Thread):
    def __init__(self):
        super(Produce, self).__init__()
    def run(self):
        global num
        while True:
            if con.acquire():
                if num <= 5:
                    num += 2
                    print("丸子还有%s个。" % num)
                    con.notify()
                    con.release()
                else:
                    print("丸子满了！")
                    con.wait()
            time.sleep(3)

if __name__ == '__main__':
    c = Consume()
    p = Produce()
    p.start()
    c.start()





















# import time, threading, random
# num = 0
# con = threading.Condition()
# def produce():
#     global num  # 鱼丸数量设置为全局变量
#     while True:
#         if con.acquire():
#             if num <= 5:
#                 # for i in range(3):
#                     # con.acquire()  # 进程锁住，丸子数量不变
#                 num += 2
#                 print("锅里还有有%s个鱼丸哦。" % num)
#                 con.notify()  # 通知可以吃鱼丸了
#                 # con.wait()  # 等待A吃掉1个鱼丸
#                 con.release()  # 放开进程，丸子数量可变
#                 time.sleep(1)
#         if num > 5:
#             print("锅里已经有%s个鱼丸了！" % num)
#
# def consume():
#     global num
#     print("im here")
#     while True:
#         if con.acquire():
#             # while True:
#             if num > 0:
#                 eat_time = random.randint(1,2)
#                 # con.acquire()
#                 num -= 1
#                 print("我吃了一个，现在锅里还剩%s个。" % num)
#                 con.notify()
#                 con.release()
#                 time.sleep(eat_time)
#             else:
#                 # con.acquire()
#                 con.wait()
#                 print("锅里没丸子啦！")
#
# th_1 = threading.Thread(target=produce())
# th_2 = threading.Thread(target=consume())
# th_1.start()
# th_2.start()
