import sys


class genshinState:
    power = 0
    remainedDailyTask = 4
    state = 0


class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'position (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return position(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return position(self.x-other.x, self.y-other.y)

# 定义一个常量类实现常量的功能
#
# 该类定义了一个方法__setattr()__,和一个异常ConstError, ConstError类继承
# 自类TypeError. 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典
# 中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
# 最后两行代码的作用是把const类注册到sys.modules这个全局字典中。


class const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value
