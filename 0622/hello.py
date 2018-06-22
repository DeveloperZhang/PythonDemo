# -*- coding: UTF-8 -*-
# 字符串

'''
str = 'Hello world!'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + 'TEST'
'''

# 列表

'''
list = ['runoob',786,2.23,'john',70.2]
tinylist = [123,'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist
'''

# 元组
'''
tuple = ("runoob",786,2.23)
list =['runoob',786,2.23]
tuple[2] = 1000 #错误操作元组不允许更改
list[2] = 1000 #正确
'''

# 字典

dict = {}
dict['one'] = "this is one"
dict[2] = 'this is two'

tinydict = {'name' : 'john','code' : 6743}

print dict['one']
print dict
print tinydict
print tinydict.keys()
print tinydict.values()