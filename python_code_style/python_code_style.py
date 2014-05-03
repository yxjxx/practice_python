# 函数名全部用小写,多个单词中间以下划线分隔
def function_name(arg1,arg2,...):
    # do something
    pass

# 类名首字母大写,其余使用驼峰命名法,不要用到下划线,括号内是
# 父类名,很多类继承了object类
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

# 在 = += == < > != <= in,not in, is, is not等符号两边都留一个空格
if 4 not in range(4) && 3 != 4:
    print('Use space correctly!')

# print语句使用括号,因为python3中print是作为函数的.先习惯
# 减少将来可能会有的代码迁移中的工作.
print("Hello world!")

# 有节制的使用行内注释,行内注释会在代码修改之后变的混乱不堪.
x = x + 1  # Increment x
