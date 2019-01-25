# day 01
    # 整数 浮点数 字符串 List Dictionary Tuple
    
    # Numeber 数字类型（init 整型； long 长整型； float 浮点型； complex 复数 ）
    count = 123
    Float = 1.02
    # String 字符串
    str = 'this\'s the string'
    # List 列表
    arr = [1, 2, 3, 4, 'five']
    # Tuple 元组
    tuple = (1, 2, 3, 4, 'five', 'six', [1, 2, 3, 'hello'])
    tuple2 = ('hello', 'the second tuple')
    # dictionary 字典类型Object
    dict = {}
    # 布尔值 True False
    # 空值None
    
    print(tuple + tuple2)
    print(True, False)
    print(None)
    
---------------------------
    # 数算运算符 + - * / %（取模， 除法余数） **（幂 x的y次方）//（取整， 返回除法后的整数部分，向下取整,只保留整数部分，小数部分不做四舍五入）
    a = 21
    b = 10
    c = 0
    
    # c = a + b
    # print ("1 - c 的值为：", c)
    #
    # c = a - b
    # print ("2 - c 的值为：", c)
    #
    # c = a * b
    # print ("3 - c 的值为：", c)
    #
    # c = a / b
    # print ("4 - c 的值为：", c)
    #
    # c = a % b
    # print ("5 - c 的值为：", c)
    #
    # # 修改变量 a 、b 、c
    # a = 2
    # b = 3
    # c = a**b
    # print ("6 - c 的值为：", c)
    #
    # a = 10
    # b = 5
    # c = a//b
    # print ("7 - c 的值为：", c)
    # 比较（关系）运算符 == 等于，比较是否相等； != 不等于； <> 类似于!= python3已经移除； > 大于； < 小于； >= <=
    
    if  a == b :
        print ("1 - a 等于 b")
    else:
        print ("1 - a 不等于 b")
    
    if  a != b :
        print ("2 - a 不等于 b")
    else:
        print ("2 - a 等于 b")
    
    if  a < b :
        print ("4 - a 小于 b")
    else:
        print ("4 - a 大于等于 b")
    
    if  a > b :
        print ("5 - a 大于 b")
    else:
        print ("5 - a 小于等于 b")
    
    # 修改变量 a 和 b 的值
    # a = 5
    # b = 20
    # if  a <= b :
    #     print ("6 - a 小于等于 b")
    # else:
    #     print ("6 - a 大于  b")
    #
    # if  b >= a :
    #     print ("7 - b 大于等于 a")
    # else:
    #     print ("7 - b 小于 a")
    # 赋值运算符 (= j简单赋值运算符； += 加法赋值运算符 c+=a => c=c+a;  -= 减法赋值运算符； *=乘法赋值运算符)
    #         （/= 除法赋值运算符； %= 取模赋值运算符 **= 幂赋值运算符； //= 取整除赋值运算符）
    
    e = 21
    f = 10
    g = 0
    e +=f
    print(e)
    f -= e
    print(f)
    f *= e
    print(f)
    
    # 位运算符： 是把数字看作二进制来进行计算的，
        # &按位与运算符： 参与运算的两个值，如果两个响应的位都为1， 则改位结果为1，否则为0
        # |按位或运算符： 制药对应的两个二进位有一个为1，结果返回1
        # ^按位异或运算符：对应的两个二进位相异时，结果为1
        # ~按位取反运算符：对数据的每个二进制位取反，即把1变成0， 把0变成类似于-x-1
        # <<左移运算符： 运算数的各二进位全部左移若干位，高位丢弃，地位补0
        # >>右移运算符： 运算书的各二进位全部右移，高位补0，低位丢弃
    
    # 逻辑运算符 (and or not)
        #and x and y 布尔与， 如果x为False， 返回false，否则返回计算y的值
        # or x or y 布尔或 如果x为True，返回x的值，否则返回计算y的值
    #not 布尔非 如果x为True，返回False， 若x为False， 返回true
    # 成员运算符
        # in 如果在指定的序列中找到值，则返回True，否则返回False
        # not in 如果在指定的序列中没有找到值返回True，否则返回False
    list = [1, 2, 3, 4, 5]
    if(1 in list):
        print('OK')
    if(10 not in list):
        print('10 is not in it')
    else:
        print('ok')
    # 身份运算符
        # is 判断两个标识符是不是引用自一个对象
        # is not 判断两个标识符是不是来自不同的对象
    # 运算符优先等级
    # **	                    指数 (最高优先级)
    # ~ + -	                    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
    # * / % //	                乘，除，取模和取整除
    # + -	                    加法减法
    # >> <<	                    右移，左移运算符
    # &	位 'AND'
    # ^ |	                    位运算符
    # <= < > >=	                比较运算符
    # <> == !=	                等于运算符
    # = %= /= //= -= += *= **=	赋值运算符
    # is is not	                身份运算符
    # in not in	                成员运算符
    # and or not	            逻辑运算符
---------
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