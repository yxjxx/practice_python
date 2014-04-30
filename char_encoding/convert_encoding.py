#coding:utf-8

# 打印中文的unicode编码
print(repr(u'中文'))

# 打印unicode对应的中文
print(u'\u4e2d\u6587'.encode('utf-8'))

