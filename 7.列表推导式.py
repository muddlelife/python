"""
推导式
具有python风格的生成式
    列表推导式
        用一个表达式创建一个有规律的列表或控制一个有规律列表
        带有if的列表推导式
        多个for循环实现的列表推导式
    字典推导式
        快速合并列表为字典或提取字典中目标数据
        创建字典
        合并两个列为字典
        提取字典中的目标数据
    集合推导式
        集合有数据去重功能，在工作中使用不高
"""
# 列表推导式
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)
list2 = [(i, j) for i in range(1,3) for j in range(3)]
print(list2)

# 字典推导式
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)
list1 = ['a', 'b', 'c', 'd']
list2 = ['1', '2', '3', '4', '5']
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)
dict3 = {key: value for key, value in dict1.items() if value > 2}
# 集合推导式
tuple1 = {i ** 2 for i in range(5)}
print(tuple1)

