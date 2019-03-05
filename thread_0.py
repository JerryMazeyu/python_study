# https://www.cnblogs.com/tkqasn/p/5700281.html
import threading, time
def wait(secs):
    print("begin " + time.strftime('%H:%M:%S'))
    time.sleep(secs)
    print("end " + time.strftime('%H:%M:%S'))
threads = []
for i in range(4):
    th = threading.Thread(target=wait, args=(5 * (4 - i),))
    threads.append(th)
for j in threads:
    j.setDaemon(True)  # 如果不设置这个就先进行主进程，再进行别的，设置后主进程结束就停止所有分进程
    j.start()
for j in threads:
    j.join(timeout=5)  # 线程timeout可能有延迟
print('finish')