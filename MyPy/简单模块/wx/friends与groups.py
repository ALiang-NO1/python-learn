from wxpy import *

bot = Bot(cache_path=True, console_qr=1)

# 获取所有好友
friends = bot.friends()

# 遍历输出好友名称
print("---------所有好友---------")
for friend in friends:
    print(friend)

# 找到好友
friend = bot.friends.search('前程')[0]
print(friend)
friend.send("hello world!")

# 获取所有聊天群
groups = bot.groups()

print("---------所有群组-----------")
for group in groups:
    print(group)

# 找到目标群
group = groups.search("测试")[0]

group.send("hello world!")