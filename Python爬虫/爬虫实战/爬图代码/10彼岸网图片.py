import requests
import os
import threadpool
from lxml import etree

"""
home_url:http://pic.netbian.com
http://pic.netbian.com/tupian/21953.html    变化数字
http://pic.netbian.com/e/search/result/?searchid=14     搜索id

http://pic.netbian.com/uploads/allimg/201113/003901-160519914172f9.jpg
/uploads/allimg/201113/003901-1605199141caf8.jpg

/uploads/allimg/201112/000443-16051106836aa6.jpg
/uploads/allimg/201112/000443-1605110683c5af.jpg
"""