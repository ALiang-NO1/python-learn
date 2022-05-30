"""
家中举办婚姻：
客户端：自己在婚礼前完成所有准备工作，每一项安排都是顶级的。
门面：会务经理与相关人员交涉，人员处理花卉、食物等。、
子系统：提供餐饮、酒店管理和花卉等服务的系统。
"""


class Hotelier:
    def __init__(self):
        print('Arranging the Hotel for Marriage?--')

    def __isAvailable(self):
        print('Is the Hotel free for the event on given day?')
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print('Registered the Booking!\n')


class Florist:
    def __init__(self):
        print('Flower Decoration for the Event?--')

    def setFlowerRequirements(self):
        print('Carnations, Roses and Lilies would be see for Decoration!\n')


class Caterer:
    def __init__(self):
        print('Food Arrangements for the Events--')

    def setCuisine(self):
        print('Chinese &Continental Cuisine to be served!\n')


class Musician:
    def __init__(self):
        print('Musical Arrangments for the Marriage--')

    def setMusicType(self):
        print('Jazz and Classical will be played!\n')


class EventManager:
    def __init__(self):
        print('Event Manager: Let me talk to the folks.\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        self.caterer = Caterer()
        self.caterer.setCuisine()
        self.musician = Musician()
        self.musician.setMusicType()


class You:
    def __init__(self):
        print('You: Whoa! Marriage Arrangments??')

    def askEventManager(self):
        print('You: let`s Contact the Event Manager.\n')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('You: Thanks to Event Manager, all preprations done!')


you = You()
you.askEventManager()
