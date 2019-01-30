# python内置了很多函数，可以直接调用

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         print(x)
#         return x
#     else:
#         print(-x)
#         return -x

'''
    def 函数名（参数列表）:
        函数体
'''

# my_abs(-100)

# 空函数
def nop():
    pass

'''
    pass
        pass语句什么都不做，可以用来作为占位符
        可以用到其他语句里
'''

# def area(width, height):
#     if not isinstance(width, (int, float)):
#         raise TypeError('type error')
#     elif not isinstance(height, (int, float)):
#         raise TypeError('type error')
#     print(width * height)
#     return
#
# def print_welcome(name):
#     if not isinstance(name, (str)):
#         raise TypeError('bad type')
#     print('Welcome %s' %(name))
#
# print_welcome('Ray')
#
# area(10, 20)
'''
    函数的参数
        位置参数
            def test(x):
                return x * x
            这里的x就是一个位置参数，位置参数是在调用函数传入参数时，必须按照位置顺序依次传入
        默认参数
            def test(x, n=2):
                s = 1
                while n > 0
                    n -= 1
                    s *= x
                return s
            此处n是一个默认参数，默认值被设定为2， 默认参数可以简化调用，设置默认参数需注意：
                1. 必选参数在前，默认参数在后，默认参数一般也是位置参数
                2. 如何设置默认参数
                    当阿还是农户有多个参数时，把变化大的参数方前面，变化小的参数放在后面，，变化小的参数可以设置为默认参数
                3. 默认参数必须指向不变的对象，如tuple 
        可变参数
            def calc(*num):
                sum = 0
                for n in num:
                    sum += num*num
                return sum
            定义可变参数，要在参数前加*，接收到一个tuple，自动将多个参数组装成一个tuple
            调用该函数时，可以传入任意个参数，包括0个
            *表示把一个list或者tuple对象的所有元素作为可变参数传入进去
        关键字参数
            关键字参数，允许传入任意个含有参数名的参数
            关键字参数在函数内部自动组装成一个dict
            def person(name, age, **kw):
                print('name:', name, 'age:', age, 'other:',  kw)
        命名关键字参数
            关键字参数，函数的调用者可以传入任意不受限制的关键字参数
            至于需要传入哪些，需要函数内部通过对kw检查
'''
def person(name, age, **kw):
    print(name, age, kw)

person('XJ', 20)

'''
    函数参数的组合
        在python中定义函数，可以用各种参数进行组合
            顺序必须是一定的： 必选参数， 默认参数， 可变参数， 命名关键字参数， 关键字参数    
'''

# 希望关键字中含有某些参数
def person2(name, age, **kw):
    if 'city' in kw:
        print(kw['city'])
    if 'job' in kw:
        print(kw['job'])
    print(name, age, kw)

person2('Ray', 30, city='BJ', job='IT')

# 限制命名关键字参数
'''
    若要限制命名关键字参数，只接收我们需要的字段，可以使用如下方法,此时仅仅能传入两个关键字参数
'''
def person3(name, age, *, city, job):
    print(name, age, city, job)

person3('Ray', 30, city='BJ', job='IT')
'''
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数，将不需要分隔符*
'''
def person4(name, age, *info, city, job):
    print(name, age, info, city, job)


person4('GD', 20, 'hello', 'youxi', 'see you', city='BJ', job='IT')

# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

