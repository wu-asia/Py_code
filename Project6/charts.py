import json

data = [{"name": "乌昂", "age": 11},{"name": "lisi", "age": 12}, {"name":"wangwu", "age":16}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))

print(json_str)

d = {"姓名": "张三", "年龄": 20}
json_str1 = json.dumps(d)
print(type(json_str1))
print(type(d))

l = json.loads(json_str1)
print(type(l))
print(l)