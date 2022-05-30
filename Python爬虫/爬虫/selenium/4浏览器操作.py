from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 声明浏览器对象
chrome_driver = r"D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# 设置隐式等待时间，单位为秒
driver.implicitly_wait(10)  # 默认等待时间为 0。隐式等待是对整个页面进行等待。需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可

# 访问页面
driver.get("https://www.baidu.com/")

# 设置搜索关键词
element = driver.find_element_by_id("kw")
element.send_keys("Selenium", Keys.ENTER)   # 在搜索框输入 “Selenium” 关键字，再回车查询

# 页面右边的"相关术语"
element2 = driver.find_element_by_class_name("opr-recommends-merge-p")
print(element2)