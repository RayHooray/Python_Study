# 条件控制语句是通过一条或者多条执行结果，来决定执行的代码块

'''
    if 语句，关键字（if - elif - else）
        if condition_1:
            statement_block_1
        elif condition_2:
            statement_block_2
        else:
            statement_block_3
'''

# num = 1
# num2 = 0
# if num:
#     print('1 - if 表达式条件为true')
#     print(num)
#
# if num2:
#     print('0 - if 表达式条件为 true')
#     print(num2)
# elif ~num2:
#     print('0 - if取反后为true')
#     print('取反', num2, end=',')
# else:
#     print('bye bye')

print('狗年龄计算器')

age = int(input('请输入狗的年龄：'))
print("")

if age < 0:
    print('狗还没出生呢')
elif age == 1:
    print('相当于人的14岁')
elif age == 2:
    print('相当于人的22岁')
elif age > 2:
    n = 22 + (age - 2)*5
    print('相当于人类年龄的%d岁' %n)

### 退出
input('点击enter退出')
'''
    if语句的嵌套
        if 表达式1:
            语句
            if 表达式2:
                语句
            elif 表达式3:
                语句
            else:
                语句
        elif 表达式4:
                语句
        else:
            语句
'''
