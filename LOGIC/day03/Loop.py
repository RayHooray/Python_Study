# 循环语句

'''
    python中的循环语句
        python中的循环语句有for 和 while
'''

'''
    # while 循环语句
        while 判断条件:
            语句
    # while语句也可以配合else来使用     
'''
# num = int(input('请输入数字：'))
# counter = 1
# sum1 = 0
#
# while counter <= num:
#     sum1 += counter
#     counter += 1
#
# print('1到 %d 之和为：%d' %(num, sum1))

'''
    无限循环
        可以通过设置条件表达式永远为true，来实现无限循环
'''

# con = float(input('请输入一个数字'))
# while con < 5:
#     print(con, '小于5')
# else:
#     print(con, '大于5')

'''
    for 语句循环
        一般格式
            for variable in sequence:
                statement
            else:
                statement
'''
sites = ['apple', 'banana', 'pear', 'orange', 'melon']

for site in sites:
    if site == 'orange':
        print('后面是西瓜')
        break
    print(site)
else:
    print('没有数据可以遍历')
print('遍历结束')
'''
    range()函数，range函数会生成一个数字序列，参数为num，
                一共可以接收三个参数：
                    一个参数时，以0开始，参数代表要生成序列的元素的个数
                    两个参数时，第一个参数表示起始位置，第二个参数代表生成序列元素不大于该参数的值
                    三个参数时，第三个参数表示步长，类似于等差数列的差值
'''

'''
    break语句主要用于跳出for和while语句
        如果在循环语句中使用了break语句，对应的else语句快将不会执行
    continue
        跳过当前循环单元，继续执行其他单元语句
    pass
        空语句，是为了保持程序结构完整心，类似于占位符
'''
