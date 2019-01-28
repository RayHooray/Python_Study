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
