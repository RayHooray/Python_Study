# 集合（Set）

# 创建一个空集合
set1 = set()

'''
    集合是一个无序的不重复元素的数列。类似于ES6总的set类型
    可以是用{}或者set()， 但创建空集合时必须使用set()，因为{}代表的是一个空的字典类型
'''

basket = {'apple', 'orange', 'pear', 'banana', 'apple'}
# 主动去重
print(basket)
# 检查元素
print('apple' in basket)
# 两集合的运算
basket2 = {'melon', 'Amazon', 'Tecent', 'DJ', 'apple'}
# 集合2中不包含集合1的元素（查询第二个集合比第一个集合少的元素）
print(basket - basket2)
# 两个集合的并集
print(basket | basket2)
# 两个集合的交集
print(basket & basket2)
# 两个集合交集的补集
print(basket ^ basket2)
'''
    集合的基本操作
        添加元素
            .add(x)     将元素添加到现有的set中，如果set中已经含有该元素，则不进行任何操作
            .update(x)  可以以列表，元组，字典等，插入多个元素
        移除元素
            .remove(x)  参数可以是多个，用于删除一个或者多个元素，若元素不存在，则会报错
            .discard(x) 此方法用于移除元素，若set中不含有x元素，也不会报错
            .pop()      随机移除一个元素，并返回移除元素
        计算集合中元素的个数
            len(set)    计算set集合中元素的个数
        清空集合
            .clear()
        判断元素是否存在于集合之中
            x in set    存在返回True, 不存在返回False
'''

'''
    集合内置其他方法
        difference()	                返回多个集合的差集 类似于set1 ^ set2
        difference_update()             移除集合中的元素，移除元素是在另一个集合中也拥有的
        intersection()                  返回集合的交集
        intersection_update()           删除集合中的元素，删除元素再改集合中并不存在
        isdisjoint()                    判断两个元素是否包含相同元素，有返回True，没有返回False
        issubset()                      判断指定集合是否为该集合的子集
        issuperset()                    判断该集合是否为指定集合的子集
        symmetric_different()           返回两个集合中不重复的元素
        symmertric_different_update()   移除当前集合于指定集合都有的元素，然后再进行合并
        union()                         返回两个集合的并集
'''
set2 = {'hello', 'youxi', 'soga', 'pear', 'banana'}
set3 = {'London', 'Tokoy', 'BJ', 'TJ', 'pear', 'banana'}

print(set2.difference(set3))
set2.difference_update(set3)
print(set2)
