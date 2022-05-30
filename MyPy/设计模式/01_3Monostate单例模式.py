class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b2 = Borg()
b.x = 4
print(f'b.x: {b.x}, b2.x: {b2.x}')


# class Borg:
#     _shared_state = {}
#
#     def __new__(cls, *args, **kwargs):
#         obj = super(Borg, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_state
#         return obj
