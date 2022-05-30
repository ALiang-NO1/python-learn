from wxpy import *   # 导入wxpy模块全部发方法

bot = Bot(cache_path=True)      # 登入网页版微信 cache_path = True 是设置缓存，不用每次登入扫码
print('robot运行中')
# one_friend = bot.friends(update=True).search('方雄')[0]     # 获取微信好友‘方雄’，记得后面要加[0]不然会运行出错
two_group = bot.groups(update=True).search('test group')[0]     # 获取微信群‘test group’
one_mp = bot.mps(update=True).search('python学习课吧')[0]     # 获取微信公众号
@bot.register(two_group, msg_types=TEXT)     # 设置修饰器，指定two_group微信群的，只对TEXT文本自动回复
def gain(msg):
    text = msg.text
    if '谢' or '[谢谢]' in text:     # 判断微信群成员发送的消息有没有‘谢’这个字，是的话返回1.png图和不客气[捂脸]
        two_group.send_image('1.png',)
        return '不客气[捂脸]'
    if '求' in text:     # 判断微信群成员发送的消息是否有‘求’这个字，是就转发此消息给python学习课吧这个公众号
        msg.forward(one_mp)
        print('已转发1')
@bot.register(one_mp, msg_types=TEXT)
def mp(msg):
    msg.forward(two_group)      # 转发此消息到two_group微信群
    print('已转发2')
embed()      # 让程序一直运行