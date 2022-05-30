def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] consuming %s' % n)
        r = '%d, 200 OK' % n

def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Producer] producing %s' % n)
        r = c.send(n)
        print('[Producer] Consumer return: %s' % r)
    c.close()

c = consumer()
producer(c)