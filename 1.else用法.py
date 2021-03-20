"""
if-else是常见的用法，在python中else还可以和for、while一起连用
补充一点
    for循环和while中的break语句不算是正常结束，continue是正常结束
"""


# 计算1～10的累加和
i = 0
sum = 0

while i < 11:  
    sum = sum + i
    i = i + 1
    
    if i == 5:
        break
else:
    print("没有计算完成!!")
print("结果为:{}".format(sum))


i = 0
sum = 0

while i < 11:
    sum = sum + i
    i = i + 1
    
    if i == 5:
        i = i + 2
        continue
else:
    print("结果少计算两个：5，6")
print("结果为:{}".format(sum))

# 总结
# 结果显示了如果在循环中有break语句执行了，那么这个循环应该算是非正常结束
# 那么else语句将不会执行
# 如果是continue语句执行了
# 那么else语句将会执行
