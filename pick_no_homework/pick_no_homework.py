#-*- coding: UTF-8 -*- 
# unicode_literals 把所有的字符串转成unicode
from __future__ import unicode_literals
import os,re,sys

# 设置默认编码是utf-8，不然处理不了中文
reload(sys)
sys.setdefaultencoding('utf-8')

name_list = [u"张三",u"李四",u"王大锤"]
# print isinstance(name_list[0],unicode)  #检测name_list[0]是否是unicode编码。
# print name_list[0]

path = "C://homework"
file_list = os.listdir(path)
# print "file_list : ";
# print file_list

for i in range(len(file_list)):
    # 用正则匹配2或3个汉字
    myname = re.findall(ur".*?([\u4e00-\u9fa5]{2,3}).*?",file_list[i])
    # print myname[0]
    if myname[0] in name_list:
        name_list.pop( name_list.index(myname[0]) )
    
print "no_homework_list : ";
for j in range(len(name_list)):
    print name_list[j]
