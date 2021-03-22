"""
元组
    特点：元组里面的数据不能删除、修改、添加
    定义元组：使用小括号，数据可以是不同的数
    查找
        1.按下标查找
        2.index()
        3.count()
        4.len()
    修改
        元组中里面有列表，修改列表中的数据是可以的，但是建议不要修改
字典
    特点：字典中数据以键值对的形式存在，与数据顺序没有关系，不支持下标
    创建字典
       1.dict1 = {}
       2.dict2 = dict()  建议用这种形式
    函数
        1.增
        2.删除
            del
                del(dict1) 删除字典
                del dict['name']
            clear 清空字典
        3.改
        4.查
            .get(key, 默认值) 如果当前查找的不存在返回第二个参数，省略第二个参数的时候，返回None
            .keys() 查看字典中所有的key，返回的是可迭代对象
            .values() 查找字典中所有值，返回的是可迭代对象
            .items() 返回的是可迭代对象，元组第一个是键，第二个是值
        5.字典的循环遍历
            遍历字典的key
                for key in dict1.keys()
            遍历字典的value
                for value in dict1.values()
            遍历字典的键值对
                for item in dict1.items() 打印元组
            遍历字典的键值对拆包
                for key,value in dict1.items()
"""
# 元组
t1 = (1, 2, 4, 6)
print(t1[3])
print(t1.index(2))
print(t1.count(2))
print(len(t1))

# 字典
# 增
dict1 = dict()
dict1['name'] = 'tom'
dict1['sex'] = 'boy'
print(dict1)

# 删除
# del dict1
del(dict1['name'])
print(dict1)

# 查
dict2 = {'name': 'jack', 'sex': 'boy', 'birth': 'Jun'}
for key in dict2.keys():
    print(key)

for value in dict2.values():
    print(value)

for item in dict2.items():
    print(item)

for key, value in dict2.items():
    print(key, value)
