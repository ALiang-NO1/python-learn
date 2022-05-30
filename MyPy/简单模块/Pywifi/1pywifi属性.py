from pywifi import *
import time

wifi = PyWiFi()
iface = wifi.interfaces()[0]
print('网卡名：', iface.name())
iface.scan()
print('扫描结果：', iface.scan_results())
print('网络配置信息：', iface.network_profiles()[0])

# 移除配置文件
iface.remove_all_network_profiles()
# 添加配置文件
profile = Profile()
# profile.auth = const.AUTH_ALG_OPEN
# profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.ssid = ''
profile.key = ''
iface.add_network_profile(profile)
iface.connect(profile)
time.sleep(5)

print('网络状态：', iface.status(), type(iface.status()))
iface.disconnect()
print('网络状态：', iface.status())