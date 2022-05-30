import random as t

# 创建单词序列
words = ("easy", "difficult", "answer", "continue")
zi = ("容易", "困难", "回答", "继续")
hanzi = {"easy": "容易", "difficult": "困难", "answer": "回答", "continue": "继续", "blue": "蓝色"}
yin = {"容易": "easy", "困难": "difficult", "回答": "answer", "继续": "continue", "蓝色": "blue"}
def jiemian(): 
    print("""
                     欢迎来到背单词
        根据English回答汉语或者根据汉语回答English
        -------------------------------------------
                    1.English——>汉语
                    
                    2.汉语——>English
                    
                    3.单词列表
                    
                    4.退出系统
""")

def yyihan():   # English——>汉语
    n = 0
    m = 0
    su = 0
    iscontinue = "y"
    while iscontinue == "y" or iscontinue == "Y": 
        word = t.choice(words)
        print("随机生成在单词: ")
        print("------>   "+word)
        guess = input("输入汉语: ").strip()   # 防止用户误操作录入空白
        while guess != hanzi[word]:
            print("对不起，不正确。")
            n = n+1
            print('\n——>正确率：%.2f' % (m/(n+m)))
            guess = input("继续输入：").strip()
        if guess == hanzi[word]: 
             print("真棒！答对了！！")
             m = m+1
             print('\n——>正确率：%.2f'%(m/(n+m)))
        iscontinue = input("是否继续（Y/N）：")
        
# 汉语——>English

def hanyiy(): 
    n = 0
    m = 0
    su = 0
    iscontinue = "y"
    while iscontinue == "y" or iscontinue == "Y": 
        hz = t.choice(zi)
        print("随机生成在汉语: ")
        print("------>   "+hz)
        guess = input("输入Ehglish: ").strip()
        while guess != yin[hz]: 
            print("对不起，不正确。")
            n = n+1
            print('\n——>正确率：%.2f'%(m/(n+m)))
            guess = input("继续输入：").strip()
        if guess == yin[hz]: 
            print("真棒！答对了！！")
            m = m+1
            print('\n——>正确率：%.2f'%(m/(n+m)))
        iscontinue = input("是否继续（Y/N）：")

def lib(): 
    print("************************")
    print("\n")
    for i in range(len(words)):
        print(words[i], "   ", zi[i], "\n")
    print("\n")
    print("************************")
    a = input("输入 1 背诵单词结束——>: ")


while True: 
    jiemian()
    a = int(input("选择需要进行的操作（1、2、3、4）："))
    if(a == 1): 
        yyihan()
    elif a == 2: 
        hanyiy()
    elif a == 3: 
        lib()
    elif a == 4: 
        exit()
    else: 
        print("输入格式错误，重新输入！！")