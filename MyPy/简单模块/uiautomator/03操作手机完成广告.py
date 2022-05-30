import uiautomator2 as u2
import time

"""
ResourceId定位: d(resourceId=“com.miui.home:id/icon_title”).click()
Text定位 d(text=u"音乐").click()
Description定位 d(description="…").click()
ClassName定位 d(className=“android.widget.TextView”).click()
"""
d = u2.connect('550b1ae3')
print('连接成功')

if not d.info['screenOn']:  # 息屏状态下解锁
    print('正在解锁')
    d.screen_on()
    d.swipe(510, 2000, 510, 300)
    if d(description="8"):
        for i in range(6):
            d(description="8").click()

d.app_start('com.zhongyishuxiang.android')   # 启动应用
print('打开博蓝共享')
d.click(965, 101)   # 点击跳过

def view_ad():
    d.click(963, 2260)  # 点击“我的”

    for i in range(3):
        d.click(538, 818)   # 点击“任务中心”
        d.click(524, 700)  # 点击“去完成”
        time.sleep(3)  # 等待广告加载
        d.click(818, 301)  # 关闭广告声音
        time.sleep(30)  # 等待广告结束
        d.click(97, 302)  # 关闭广告
        time.sleep(1)
        d.click(110, 190)   # 再次关闭广告
        d.click(100, 182)   # 点击返回键到“我的”
    d.click(538, 818)  # 点击“任务中心”
    d.click(2530, 952)  # 点击”待领取“
    d.click(948, 168)   # 点击“一键领取”

view_ad()
d.click(100, 182)  # 点击返回键到“任务中心”
d.click(100, 182)  # 点击返回键到“我的”
d.click(1019, 171)  # 点击设置
d.click(595, 1000)  # 点击退出登入
d.click(531, 494)   # 点击登入圆按钮
print('正在切换账号')
if input() != '':
    exit(0)
d.click(596, 1110)  # 点击登入方按钮
view_ad()   # 换个账号后再来
d.app_stop('com.zhongyishuxiang.android')    # 关闭应用

# ----------------陌嗨星球--------------
d.app_start('cn.hemayoudao.mohai')
print('打开陌嗨星球')
time.sleep(8)   # 等待软件启动
d.click(988, 166)   # 点击跳过开机广告
time.sleep(4)   # 等待缓冲
d.click(982, 2254)  # 点击“个人中心"
time.sleep(1)
d.click(621, 1090)  # 点击“陌嗨乐园”
if input() != '':
    exit(0)
d.click(699, 339)   # 点击“获取能量”
time.sleep(1)

def auto_ad(x):
    d.click(x, 1115)  # 点击第一个广告
    time.sleep(3)   # 等待广告加载
    d.click(848, 292)   # 关闭声音
    time.sleep(30)
    d.click(97, 302)  # 关闭广告
    time.sleep(1)
    d.click(110, 190)  # 再次关闭广告
for x in [231, 386, 543, 708, 880]:
    auto_ad(x)
d.app_stop('cn.hemayoudao.mohai')   # 关闭软件