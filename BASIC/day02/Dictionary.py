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
