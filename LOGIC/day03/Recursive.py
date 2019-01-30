# 递归函数
'''
    在函数内部可以调用其他函数，如果一个函数在内部调用自身，这个函数就称为递归函数
'''
#  阶乘函数
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)

a = fact(100)

print(a)
'''
    使用递归函数要放置栈溢出
'''
