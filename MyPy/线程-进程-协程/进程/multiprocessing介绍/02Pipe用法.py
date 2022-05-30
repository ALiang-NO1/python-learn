import multiprocessing as mp

"""
Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。
我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。
"""
def pc1(pipe):
    pipe.send('hello')
    print('process1 rec: %s' % pipe.recv())

def pc2(pipe):
    print('process2 rec: %s' % pipe.recv())
    pipe.send('hello, too')

pipe = mp.Pipe()
if __name__ == '__main__':
    # Pass an end of the pipe to process 1
    p1 = mp.Process(target=pc1, args=(pipe[0],))
    # Pass an end of the pipe to process 2
    p2 = mp.Process(target=pc2, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p1.join()