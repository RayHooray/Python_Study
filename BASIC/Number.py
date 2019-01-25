# python的执行顺序是由上到下依次执行的
# Number数据类型用于存储数值
# 数据类型是不允许改变的，这就意味着如果改变数据类型的值，将重新分配内存空间
num1 = 1
num2 = 10
# del 用于删除一些定义的字段
print(num1)
print(num2)
del num2, num1
import math
import random

# Number支持的数值类型
'''
   int（整型）： 整数
   float （浮点型）： 小数
   complex（复数）： 实部和虚部构成的 
   
   数字类型转换
   complex(x, y) 实部是x，虚部是y
'''
# a = 1 / 2
# b = 4 / 2
# c = 4 // 2
# print(a)
# print(b)
# print(c)
# d = 12//5
# e = 13 // 5
# print(d)
# print(e)

'''
    在整个除法中，/ 总是会返回一个float, 所以可以使用 // 丢弃小数部分
    // 得到得也并不一定是整数类型得数，他与分母分子得数据类型有关
    所有得变量必须先定义并初始化后使用
    不同类型的数混合运算时会将整数转换为浮点数
'''

'''
    数学函数 math：
        abs(x) 返回数字的绝对值
        cell(x) 返回数字的上入整数（向上取整）
        cmp(x, y) x < y 返回 -1； x == y 返回 0； x > y 返回1； python3使用(x > y) - (x < y)
        exp(x) e的x次幂
        fabs(x) 返回数字的绝对值，返回一个浮点数
        floor(x) 返回数字向下取整
        log(x, y) 返回以y为底数的x的对数
        log10(x) 返回以10为底数的x的对数
        max(list) 返回最大数,可以是一个list，也可以是一个序列
        min(list) 返回最小值
        modf(x) 返回两部分，整数和小数，整数部分以浮点数表示,返回的是一个tuple对象
        pow(x, y) 返回 x**y的值
        round(x, n) 返回浮点数，四舍五入的值，n表示保留到小数点后n位
        sqrt(x) 返回数字x的平方根
        pi 数学常量
        e 自然常数
'''
# x = 1
# y = 2
list = [1, 2, 3, 4, 5]
# tup = (1, 2, 3, 4, 5)
# pi = math.pi
#
# # print((x > y) - (x < y))
# # print(math.log(2, 4))
# print(max(list))
#
# print(math.modf(pi)[0])

'''
    随机数函数 random
        choice(seq)从一个序列中，返回一个元素
        randrange(start, stop, step) 
            start: 指定开始位置（值）， 
            stop: 指定结束位置（值） 
            step: 递增基数
        seed([x]) 改变随机数生成seed
        shuffle(lst)	将序列的所有元素随机排序
        uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''

# print(random.choice(list))
# print(random.randrange(1, 100, 2))
random.seed()
print('使用默认种子生成随机数', random.random())
random.seed(10)
print('使用整数种子生成随机数', random.random())
random.seed('hello', 2)
print('使用字符串种子生成随机数', random.random())
random.shuffle(list)
print('随机排序', list)

'''
    三角函数
        acos(x)	返回x的反余弦弧度值。
        asin(x)	返回x的反正弦弧度值。
        atan(x)	返回x的反正切弧度值。
        atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
        cos(x)	返回x的弧度的余弦值。
        hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
        sin(x)	返回的x弧度的正弦值。
        tan(x)	返回x弧度的正切值。
        degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
        radians(x)	将角度转换为弧度
'''