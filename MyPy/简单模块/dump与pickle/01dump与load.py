import json

number = {"username": False, "password": None,
          'tuple': ('a', 'b'),
          'list': [{'occupation': 'doctor'}]
          }
# number = 'username=amy&password=123'
# number = [2, 3, 5, 7, 11, 13]
print(json.dumps(number))
print(json.loads('{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}'))

# # --------保存在文档中--------
# filename = 'number.json'
# with open(filename, 'w', encoding='utf-8') as f_obj:
#     json.dump(number, f_obj, indent=None)      # 0:每个值单独一行，大于0：单独一行并使用该数目空格缩进嵌套数据结构
# # --------从文档中读取---------
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)