"""方法的动态性"""

class Person:
    def work(self):
        print('努力工作！')

def play_game(a):
    print('{0}在玩游戏'.format(a))

Person.play = play_game

p = Person()
p.work()