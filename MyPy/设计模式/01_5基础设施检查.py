class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append('Server1')
        self._servers.append('Server2')
        self._servers.append('Server3')
        self._servers.append('Server4')

    def changeServer(self):
        self._servers.pop()
        self._servers.append('Server5')


hc = HealthCheck()
hc2 = HealthCheck()
hc.addServer()
print('Check health(1)...')
for i in range(4):
    print('Checking:', hc._servers[i])
    hc2.changeServer()
print('Check health(2)...')
for i in range(4):
    print('Checking', hc2._servers[i])
