import demjson

"""
encode	将 Python 对象编码为 JSON 字符串表示。
decode	将 JSON 编码的字符串解码为 Python 对象。
"""
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = demjson.encode(data)
print("python对象转JSON：", json)

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = demjson.decode(json)
print("JSON转python对象：", text)