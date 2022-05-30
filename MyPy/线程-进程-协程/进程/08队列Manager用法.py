from multiprocessing import Manager, Pool

def writer(q):
    for i in ['a', 'b', 'c', 'd']:
        print("写入：", i)
        q.put(i)

def reader(q):
    for i in range(q.qsize()):
        print("读取到：", q.get())

if __name__ == '__main__':
    p = Pool(3)
    q = Manager().Queue()
    p.apply(writer, (q,))
    p.apply(reader, (q,))
    p.close()
    p.join()