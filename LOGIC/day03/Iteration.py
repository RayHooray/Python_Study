# 迭代式访问集合元素的一种方式，迭代器可以记住遍的位置的对象
# 迭代器对象从集合的第一个元素开始访问，知道所有元素被访问完毕，只能向前不能后退
# python中迭代器有两个基本方法: iter() 和 next()

# List = [1, 2, 3, 4]
# it = iter(List)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 使用for进行迭代
# for x in it:
#     print(x, end=',')

# 使用next()函数
# import sys
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit('Done')

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


