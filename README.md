# day 01
数据类型

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
运算符

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
Number

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
---
String

    # 字符串类型 String
    
    a = "Hello"
    b = "Python"
    print(a[:6])
    
    '''
    String 运算符
        +	    字符串连接	a + b 输出结果：  HelloPython
        *	    重复输出字符串	a*2 输出结果：HelloHello
        []	    通过索引获取字符串中字符	a[1] 输出结果 e
        [ : ]	    截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
        in	    成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
        not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
        r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 
                原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
        %	    格式字符串
    '''
    
    '''
        字符串格式化
          %c	 格式化字符及其ASCII码
          %s	 格式化字符串
          %d	 格式化整数
          %u	 格式化无符号整型
          %o	 格式化无符号八进制数
          %x	 格式化无符号十六进制数
          %X	 格式化无符号十六进制数（大写）
          %f	 格式化浮点数字，可指定小数点后的精度
          %e	 用科学计数法格式化浮点数
          %E	 作用同%e，用科学计数法格式化浮点数
          %g	 %f和%e的简写
          %G	 %f 和 %E 的简写
          %p	 用十六进制数格式化变量的地址
        
        格式化操作辅助指令
            *	    定义宽度或者小数点精度
            -	    用做左对齐
            +	    在正数前面显示加号( + )
            <sp>	在正数前面显示空格
            #	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
            0	    显示的数字前面填充'0'而不是默认的空格
            %	    '%%'输出一个单一的'%'
            (var)	映射变量(字典参数)
            m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话
    '''
    
    str = "i am %s, i'm %d years old"
    
    tup = ('Ray', 30)
    
    joi = str%tup
    
    print(joi)
    
    '''
        """
            三引号允许一个字符串跨多行，字符串中可以包含换行符，制表符以及其他特殊符号
    '''
    
    para_str = """这是一个多行字符串的实例
    多行字符串可以使用制表符
    TAB ( \t )。
    也可以使用换行符 [ \n ]。
    """
    print (para_str)
    
    """
        capitalize()
        将字符串的第一个字符转换为大写
        
        
        center(width, fillchar)
        返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
        
        
        count(str, beg= 0,end=len(string))
        返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
        
        
        bytes.decode(encoding="utf-8", errors="strict")
        Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
        
        
        encode(encoding='UTF-8',errors='strict')
        以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
        
        
        endswith(suffix, beg=0, end=len(string))
        检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
        
        
        expandtabs(tabsize=8)
        把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
        
        
        find(str, beg=0 end=len(string))
        检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
        
        
        index(str, beg=0, end=len(string))
        跟find()方法一样，只不过如果str不在字符串中会报一个异常.
        
        
        isalnum()
        如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
        
        
        isalpha()
        如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
        
        
        isdigit()
        如果字符串只包含数字则返回 True 否则返回 False..
        
        
        islower()
        如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
        
        
        isnumeric()
        如果字符串中只包含数字字符，则返回 True，否则返回 False
        
        
        isspace()
        如果字符串中只包含空白，则返回 True，否则返回 False.
        
        
        istitle()
        如果字符串是标题化的(见 title())则返回 True，否则返回 False
        
        
        isupper()
        如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
        
        
        join(seq)
        以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
        
        
        len(string)
        返回字符串长度
        
        
        ljust(width[, fillchar])
        返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
        
        
        lower()
        转换字符串中所有大写字符为小写.
        
        
        lstrip()
        截掉字符串左边的空格或指定字符。
        
        
        maketrans()
        创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
        
        
        max(str)
        返回字符串 str 中最大的字母。
        
        
        min(str)
        返回字符串 str 中最小的字母。
        
        
        replace(old, new [, max])
        把将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
        
        
        rfind(str, beg=0,end=len(string))
        类似于 find()函数，不过是从右边开始查找.
        
        
        rindex( str, beg=0, end=len(string))
        类似于 index()，不过是从右边开始.
        
        
        rjust(width,[, fillchar])
        返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
        
        
        rstrip()
        删除字符串字符串末尾的空格.
        
        
        split(str="", num=string.count(str))
        num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
        
        
        splitlines([keepends])
        按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
        
        
        startswith(substr, beg=0,end=len(string))
        检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
        
        
        strip([chars])
        在字符串上执行 lstrip()和 rstrip()
        
        
        swapcase()
        将字符串中大写转换为小写，小写转换为大写
        
        
        title()
        返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
        
        
        translate(table, deletechars="")
        根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
        
        
        upper()
        转换字符串中的小写字母为大写
        
        
        zfill (width)
        返回长度为 width 的字符串，原字符串右对齐，前面填充0
        
        
        isdecimal()
        检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
    """


-----
#day 02
List

    # 列表List
    
    list = [1, 2, 'hello', [222, 333], (1, 2, 3, 4), {'a': 'hello'}]
    print(list)
    '''
        列表（序列）
            每个元素都会分配一个index值，作为索引，从0开始；
            python有6个序列的内置类型 列表 元组 字符串 Unicode字符串 buffer对象 xrange对象
            序列可进行的操作，调取索引值，切片，加， 乘 检查成员 长度 最大最小元素
    '''
    
    # 删除列表index值位2的元素
    del list[2]
    print(list)
    
    '''
        Python列表脚本操作符
            len(list) 类似与js中的length
            + 连接两个字符串 类似与js中的join
            *num 重复， num表示要重复的次数
            in 检查元素是否存在与某以list列表中，返回True或False(n in list)
            for x in list: 迭代遍历 js： for(let i = 0; i < list.length; i++) {}
    '''
    
    '''
        Python列表的截取与拼接
        [start:end]     切片，从start处到end处（不包括end）
    '''
    
    '''
        列表函数
            len(list) 列表元素个数
            max(list) 返回列表元素的最大值
            min(list) 返回列表元素的最小值、
            list(seq) 将元组转换成列表
        列表方法
            list.append(obj) 在末尾添加新的对象 js：push
            list.count(obj) 统计某个元素在列表中出现的次数
            list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（新列表扩展原来的列表）
            list.index(obj) 在列表中找出某个值第一个匹配项的索引值
            list.insert(index, obj) 在列表索引index处插入obj
            list.pop([index=-1]) 移除列表中的一个元素（默认是最后一个元素）， 并返回该元素的值
            list.remove(obj) 移除列表中的obj的第一个匹配项,如果没有，则会报错
            list.reverse() 反向排列
            list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序
            list.clear() 清空列表
            list.copy() 复制列表， 将原列表内元素复制，比重新生成一个新的列表
    '''
    list2 = [1, 2, 3, 4]
    list2.remove(2)
    print(list2)
    list3 = [1, 1, 2, 3, 4, 5, 2, 3, 4, 5]
    list3.sort()
    print(list3)
----
Tuple
    
    # 元组 Tuple
    tup = ('helo', 'hola', 'bojor')
    
    '''
    
        不同之处
            元组的元素是不能修改的
            元组中只包含有一个元素的时候，需要在元素后面添加逗号，否则会被当作运算符使用
            获取元组中的元素，只需要通过索引来访问
            元组中的值不可以修改，但是可以进行组合 通过 +
            元组中的元素是不允许修改和删除的，所以只能通过del删除整个元组
            
            
    '''
    print(type(tup))
    
    '''
        元组运算符
            len(tuple)      计算元组中元素的个数
            +               连接
            *               复制
            in              检查某一元素是否存在与元组中，存在True， 不存在False
            for x in tuple  迭代
    '''
    
    '''
        元组的索引， 截取
        [num]           索引
        [start : end]   截取。start和end表示索引值，表示从start索引到end(截取数量)进行截取
                            若start或end没有传值，则表示从开始0（或结尾len - 1）
    '''
    tuple1 = ('gifille', 'Oudy', 'John', 'Lisa')
    
    print(tuple1[:3])
    print(tuple1[1:])
    
    '''
        元组中的内置函数
            len(tuple)      计算元组中元素的个数
            max(tuple)      返回元组中元素的最大值
            min(tuple)      返回元组中元素的最小值
            tuple(seq)      将一个序列转换成一个元组
    '''
---
Dictionary

    # 字典是另一种容器模型，且可以存储任意类型的对象
    dictionary = {"Lucus": "hello", "num": 1, "list": [], "tup": (1, 2)}
    
    '''
        字典类型是由 key value 组成，每一个元素的key值必须是唯一的，value可以不唯一
    '''
    
    '''
        字典操作：
    '''
    dic = {"Name": "Charls", "Age": 30, "gender": "male"}
    
    print(dic)
    # 修改
    # 更新
    dic["Age"] = 28
    print(dic)
    #添加
    dic["Home"] = "British"
    print(dic)
    #删除，可以删除一个属性，清空属性，也可以删除整个字典
    del dic["gender"]
    print(dic)
    dic.clear()
    print(dic)
    del dic
    # print(dic)
    '''
        字典键（key）的特性
            1。允许同一个键出现两次，若同一个键出现两次，后一个键的值将覆盖前一个键的值
            2。key必须是不可变值，所以可以用数字，字符串甚至元组充当，单不可以使用list
    '''
    dic2 = {(1, 2, 3): 'hello', 1: 'youxi', 'str': 'soga', 1: "hehe"}
    print(dic2[(1, 2, 3)])
    print(dic2[1])
    
    '''
        字典内置函数
            len(dict)       计算字典内，元素的个数，即键的总数
            str(dict)       输出字典，以可打印的字符，类似与js的toString
            type(variable)  返回变量类型，如果是字典类型，就返回字典类型
    '''
    
    '''
        字典内置方法
            .clear()                    删除字典内的所有元素，保留变量指针
            .copy()                     返回一个字典的浅复制
            .fromkeys()                 创建一个新的字典，以序列seq中的元组作为字典的键， val为字典所有对应的初始值
            .get(key，default)          返回指定键的值，如果不存在，则返回default
            key in dict                 查询字典dict里的key，存在返回True，否则返回False
            .items                      以列表形式返回可遍历的元素数组
            .keys()                     返回一个迭代器， 可以使用list()来转换成列表Object.keys(obj)
            .setDefault(key, default)   类似于get()，饭如果不存在的换，将为其赋值为default值
            .update(other dict)         将一个dict中的值更新到另一个dict中
            .pop()                      删除字典中给定的key所对应的值，并返回这个值，key值必须给定，否则返回设定的default值
            .popitem()                  随机返回并删除字典中的一对键值对（删除末尾），并返回这个键值对
            .values()                   返回一个迭代器，可以使用list()转换成列表
    '''
    seq = ('name', 'age', 'gender')
    List = ('Ray', 28, 'male')
    dic = dict.fromkeys(seq, List)
    print(dic)
    print(dic.get('job', False))
    dict1 = {'name': 'Ray', 'age': 30, 'gender': 'male'}
    print(dict1.items())
    print(dict1.keys())

