"""
列表操作函数
    1.增
        append() 列表结尾追加数据，如果追加的数据是一个序列，那么追加整个序列
        extend() 列表结尾追加数据，如果追加的数据是一个序列，那么会依次增加序列中的数据
        insert() 指定位置新增数据
    2.删
        del() 无返回值
            直接删除列表 del name_list
            可以删除指定下标的数据 del name_list[]
        pop() 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，然后返回这个被删除的数据
        remove() 移除第一个匹配项
        clear() 清空列表，只保留一个空列表
    3.改
        修改指定下标元素 name[0] = 'aaa' 
        逆置 .reverse()
        排序 .sort()
            升序 默认reverse = False
            降序 reverse = True
    4.查
        下标
        .index()
        .count()
        len() 公共方法 统计列表的元素的个数
        判断某个数据是否存在 公共方法
            in 'Tom' in name_list
            not in 'Tome' not in name_list
    5.复制
        .copy()
"""

a1 = ['a', 'b', 'c', 'abc']
a2 = [2, 3]
a3 = ['x', 'y', 'z']
a4 = ['m', 'n']

# 增
a1.append(a2)
a3.extend(a2)
a4.insert(1, a2)
print(a1)
print(a3)
print(a4)

# 删
del(a1[1])
print(a1)
print(a1.pop())
print(a3.remove('y'))
print(a2.clear())

# 改，只能在纯数字或者纯字符串来排序
b = [1, 3, 24, 1, 0, -1]
b.sort()
print(b)
c = ['a', 'd', 'c', 'w']
c.sort(reverse = True)
print(c)

# 查
index = c.index('c')
print(index)
number = c.count('b')
print(number)
print(len(c))

# 复制
d = c.copy()
print(d)
