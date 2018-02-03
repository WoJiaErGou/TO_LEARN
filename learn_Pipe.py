import multiprocessing
import random
import time,os
# random.random()生成0-1随机浮点数
def proc_send(pipe,urls):
    for url in urls:
        print('Process(%s) send: %s' % (os.getpid(),url))
        pipe.send(url)
        time.sleep(random.random())
def proc_recv(pipe):
    while True:
        print('Process(%s) rev:%s'% (os.getpid(),pipe.recv()))
        time.sleep(random.random())
if __name__ == '__main__':
    pipe = multiprocessing.Pipe()   # Pipe方法返回(conn1,conn2),代表一个管道的两个端
    p1 = multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv,args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()