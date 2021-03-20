"""
常用字符串函数分类
    1.查找
        find() 检测某个字串是否在这个字符中，如果在，返回字串开始的下标，否则返回-1
        index() 返回下标
        count() 返回某个字串在字符串中出现的次数
    2.修改
        replace() 替换字符串
        split() 分割字符串
        join() 用一个字符或字串合并成一个大字符串(包括列表)
        修改大小写
            .capitakize() 只有首字母大写，其他全部小写
            .title() 每个单词首字母大写，其他全部小写
            .upper() 小写转大写
            .lower() 大写转小写
        删除空白字符
            lstrip() 删除左侧空白
            rstrip() 删除右侧空白
            strip() 删除两边空白
        设置对齐
            ljust() 返回一个原字符串左对齐，并使用指定字符（默认空格）填充
            rjust() 右对齐
            center() 居中
    3.判断
        stratwith() 检测字符串是否以指定字串开头
        endwith() 检测字符串是否以指定字串结尾
        isalpha() 如果字符串至少有一个字符并且所有字符都是字母返回Ture
        isdigit() 判断都是数字
        isalnum() 判断非空字符串中是数字或字母组合，不包括空格
        isspace() 判断都是空白返回True
"""

str = '   this Is test.txt'

# 1.查找
result = str.find('es')
print(result)

index = str.index('es')  # 如果查找不到则报错
print(index)

number = str.count('s')
print(number)

# 2.修改
print(str.replace('is', 'IS'))
print(str.split(' '))  # 返回是一个列表
print(str.join('abc!'))  # 用str把abc连接起来
print(str.capitalize())
print(str.title())
print(str.upper())
print(str.lower())
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print(str.ljust(20, '!'))
print(str.rjust(20, '*'))
print(str.center(20, '-'))

# 3.判断
print(str.startswith('abc'))  # false
print(str.endswith('this'))  # false
print(str.isalpha())  # false
print(str.isdigit())  # false
print(str.isalnum())  # false
print(str.isspace())  # false
