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
