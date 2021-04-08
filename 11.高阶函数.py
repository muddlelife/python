"""
高阶函数
    把函数作为参数输入，函数式编程就是这种高度抽象的编程范式
    体验高阶函数
        abs(-10)  求绝对值
        round(1.2)  四舍五入
    特点
        函数式编程大量使用函数，减少了代码的重复，因此程序比较端，开发速度比较快
    python内置高阶函数
        map(函数名, 序列)  将传入的函数变量作用到序列的每个元素中，并将结果组成新的列表（python2）/迭代器（python3）返回
        reduce（func, 序列）
            必须导入模块functools
            func函数必须要有两个参数，每次func计算的结果继续和序列的下一个元素做函数计算
        filter(func, 序列)
            用与过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转换为列表，可以用list()来转换
"""

# 高阶函数
print(abs(-10))
print(round(1.2))

# 内置高阶函数
a = map(round, [1, 2.2, 3.5])
import functools
def two_and(a, b):
    return a + b
b =functools.reduce(two_and, [1, 2, 3])
print(b)
def is_single(a):
    return a % 2 == 1
c = filter(is_single, [1, 2, 3])
print(c)
print(type(c))
print(list(c))
print(type(list(c)))
