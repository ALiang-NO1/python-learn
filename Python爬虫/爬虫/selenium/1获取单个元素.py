from selenium import webdriver
from selenium.webdriver.common.by import By

# 声明浏览器对象
# 禁止打开网页
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# chrome_driver = r"D:/chromedriver.exe"
driver = webdriver.Chrome(options=options)     # driver = webdriver.Firefox() IEexecutable_path=chrome_driver, options=options

# 访问页面
driver.get("http://www.baidu.com")

# 通过id查找
element = driver.find_element_by_id("kw")     # 输入框input的id:kw
print(element.tag_name)

# 通过name查找
element = driver.find_element_by_name("wd")     # 输入框的id:name:kw
print(element.tag_name)

# 通过xpath查找
element = driver.find_element_by_xpath('//*[@id="kw"]')
print(element.tag_name)

# 通过另一种方式查找
element = driver.find_element(By.ID, "kw")
print(element.tag_name)
