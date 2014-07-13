#coding=utf-8
#global 只是使函数内定义的变量在函数外可以访问了
#函数外定义的变量在函数内可以直接使用,前提是你没有在函数内声明同名的变量
sub = ['a', 'b', 'c']
mystr = "hello"
def getJoin():
    return '.'.join(sub)

def print_str():
    return mystr

def can_not_change_mystr():
    mystr = "can not change mystr"

def change_mystr():
    global mystr
    mystr = "global hello"


print(getJoin())  #a.b.c
print( print_str() )  #hello

can_not_change_mystr()
print mystr  #hello

change_mystr()
print mystr  #global hello
