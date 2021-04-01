"""
公共方法就是公共操作，不管是列表、字符串、元组、集合、字典都可以操作的方法
    1.运算符（没有集合）
        + ：字符串、列表、元组
        * ：字符串、列表、元组
        in ：字符串、列表、元组、字典
        not in ：字符串、列表、元组、字典
        注意：在字典中默认判断的是key的存在
    2.len()
    3.del 或者 del()
    4.默认针对的是键
        max()
        min()
    5.range()
    6.enumerate() 用于将一个可遍历的数据对象（如列表，元组或字符串）组合成一个人索引序列，同时列出数据和数据下标，一般用在for循环中，返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，第一个数据为原迭代对象的数据
    7.容器类型转换
        将某个序列转换成元组 tuple(序列)
        将某个序列转换成列表 list(序列)
        将某个序列转换为集合 set(序列)
"""

# 运算符
str1 = 'abc'
str2 = 'xyz'
print(str1 + str2)
print(str1 * 3)
print('a' in str1)

# len()
list1 = [1, 2, 3, 4]
print(len(list1))

# del 或者 del()
tuple1 = (1,2,3)
del tuple1

# max() min()
set1 = {1, 2, 4, 6}
print(max(set1))
print(min(set1))

# range()
for i in set1:
    print(i)

# enumerate()
dict1={'a': 1, 'b': 2, 'c': 3}
for i, j in enumerate(dict1):  # 默认输出的是key值
    print(i, j)

# 容器类型转换
print(tuple(dict1))  # 默认是key值
print(list(str1))
print(set(list1))
