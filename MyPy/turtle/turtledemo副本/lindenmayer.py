from turtle import *


def replace(seq, replacementRules, n):
    # ("b--f--b--f", {"b": "b+f+b--f--b+f+b"}, 3)
    for i in range(n):  # 将 b 替换为 b+f+b--f--b+f+b，替换3次，返回替换的最后结果
        newseq = ""
        for element in seq:
            newseq = newseq + replacementRules.get(element, element)
        seq = newseq
    return seq


def draw(commands, rules):
    # commands: b+f+b--f--b+f+b+f+b+f+b--f--b+f+b--f-- * 11
    # rules: {"-": r, "+": l, "f": f, "b": "f+f+f--f--f+f+f"}
    for b in commands:  # 通过符号 - + f 分别调用 r() l() f()，右转45，左转45，前进7.5
        try:
            rules[b]()
        except TypeError:  # 遇到 b 索引报错: 将f+f+f--f--f+f+f作为符号嵌套函数
            try:
                draw(rules[b], rules)
            except:
                pass


def main():
    ################################
    # Example 1: Snake kolam
    ################################

    def r():
        right(45)

    def l():
        left(45)

    def f():
        forward(7.5)

    snake_rules = {"-": r, "+": l, "f": f, "b": "f+f+f--f--f+f+f"}
    snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacementRules, 3)

    reset()
    speed(3)
    tracer(1, 0)
    ht()
    up()
    backward(195)
    down()
    draw(drawing, snake_rules)

    input('Stopped!  Press Enter key to start:')
    delay(3000)

    ################################
    # Example 2: Anklets of Krishna
    ################################

    def A():  # 用红笔画半径10的1/4的圆
        color("red")
        circle(10, 90)

    from math import sqrt

    def B():  # 黑笔前进3.5，画半径3.5的圆，前进3.5
        color("black")
        l = 5 / sqrt(2)
        forward(l)
        circle(l, 270)
        forward(l)

    def F():  # 绿笔前进10
        color("green")
        forward(10)

    krishna_rules = {"a": A, "b": B, "f": F}
    krishna_replacementRules = {"a": "afbfa", "b": "afbfbfbfa"}
    krishna_start = "fbfbfbfb"

    reset()
    speed(0)
    tracer(3, 0)
    ht()
    left(45)
    drawing = replace(krishna_start, krishna_replacementRules, 3)
    draw(drawing, krishna_rules)
    tracer(1)
    return "Done!"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
