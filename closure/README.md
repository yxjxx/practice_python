closure
=======

是一个"内层"的函数, 有一个变量名来指代, 这个变量名对于"外层"包含它的函数而言是本地变量.
make_adder指向一个闭包, make_adder为一个工厂函数.

A closure is nothing terribly complicated: just an "inner" function that refers to names that are local to an "outer" function containing it. 
In pactice, you may often see make_adder referred to as a closure.Calling make_adder a factory function is both accurate and concise; you may also say it's a closure factory to specify it builds return closures, rather than, say, classes or class instances.

===============

[refer in stackoverflow](http://stackoverflow.com/questions/4020419/closures-in-python)

A closure occurs when a function has access to a local variable from an enclosing scope that has finished its execution.

~~~
def make_printer(msg):
    def printer():
        print msg
    return printer

printer = make_printer('Foo!')
printer()
~~~

When make_printer is called, a new frame is put on the stack with the compiled code for the printer function as a constant and the value of msg as a local. It then creates and returns the function. Because the function printer references the msg variable, it is kept alive after the make_printer function has returned.
