# 这个模块主要进行测试Rlock和lock的方法

import threading
import time

gl_num = 0
lock = threading.RLock()

def lockfun(timeout):  # 参数层、修饰器层、函数参数层
    def wrapped(fun):
        def inner(*args, **kwargs):
            print("using decorator.")
            lock.acquire(timeout)
            fun(*args, **kwargs)
            lock.release()
            print("finished decorate.")
        return inner
    return wrapped


@lockfun(2)
def show(arg):
    print("start")
    global gl_num
    time.sleep(1)
    gl_num += 1
    print(gl_num)

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')
