# 模块是包括 Python 定义和声明的文件。文件名就是模块名加上 .py后缀
import os
# import Requests
import collections
import re

# 返回当前进程的 id
print(os.getpid())
# 返回父进程的 id
print(os.getppid())
# 返回识别操作系统的不同信息，返回一个元组（sysname, nodename, release, version, machine)
# print(os.uname())
# 返回当前工作目录
print(os.getcwd())
# 更改当前目录到path
# os.chdir(path='')

c = collections.Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))
d = collections.Counter('abcdfeaddsvsewvvzafds')
print(d.most_common(3))

# defaultdict() 第一个参数提供了 default_factory 属性的初始值，默认值为 None，default_factory 属性值将作为字典的默认数据类型。所有剩余的参数与字典的构造方法相同，包括关键字参数。
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
q = collections.defaultdict(list)
for k, v in s:
    q[k].append(v)

print(q.items())

# 命名元组有助于对元组每个位置赋予意义，并且让我们的代码有更好的可读性和自文档性。
Point = collections.namedtuple('Point', ['x', 'y'])      # 定义命名元组
p = Point(10, y = 20)      # 创建一个对象
print(p)
print(p.x + p.y)
print(p[0] + p[1])
x, y = p       # 元组拆封
print(x)
print(y)
