"""
递归函数
    递归：自己调用自己，必须要有出口
匿名函数
    lambda表达式
        说明
            1.如果一个函数有一个返回值，并且只有一句话代码，可以用lambda简化
            2.lambda参数列表：表达式（必须要有返回值）
            lambda表达式的参数可有可无，函数的参合苏在lambda表达式中完全适用
            lambda表达式能够接收任何数据的参数但只能返回一个表达式的值
        参数形式
            1.无参数
                fn1 = lambda: 100
            2.一个参数
                fn1 = lambda a: a
            3.默认参数
                fn1 = lambda a, b, c = 100: a + b + c
            4.可变参数 *args
                fn1 = lambda *args: args  # 返回的是元组
            5.可变关键字参数 *kwargs
                fn1 = lambda **kwagrs: kwargs  # 返回的是字典
        带判断的lambda
            fn1 = lambda a, b: a if a > b else b
"""
# 递归函数
def num_sum(a):
    if a == 1:
        return 2
    else:
        return a - num_sum(a - 1)
            
print(num_sum(99))

# 匿名函数
fn1 = lambda: 100
fn2 = lambda a: a
fn3 = lambda a, b, c = 100: a + b + c
fn4 = lambda *args: args
fn5 = lambda **kwargs: kwargs
print(fn1())
print(fn2(100))
print(fn3(1, 2))
print(fn4(1, 2, 3, 4))
print(fn5(a = 100, b = 1000, c = 10))
fn6 = lambda a, b: a if a > b else b
print(fn6(2, 4))
