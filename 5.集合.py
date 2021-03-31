"""
集合
    特点
        拥有自动去重功能，集合中数据不能重复
        集合没有顺序，不支持下标
    操作
        创建集合
            s1 = {10, 20, 40}
            s4 = set()
            注意，如果用字符串的话，会分成单个字符，且没有顺序
        增加数据
            add()
            update()  增加的是序列
        删除数据
            remove()  若数据不存在则会报错
            discard()  若数据不存在不会报错
            pop()  随机删除某个数据，并返回这个数据
        查找数据
            in  判断数据在集合序列
            not in  判断数据不在集合序列
"""
# 创建集合

s1 = {10, 20, 40}
s2 = set('abcd') 
print(s1)
print(s2)

# 增加数据
s1.add('abc')
s2.update([1,2,3])
print(s1)
print(s2)

# 删除
s1.remove(20)
s2.discard('a')

# 查找数据
print('a' in s1)
print('b' not in s2)
