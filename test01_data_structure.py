import math
# 变量
"""
float_t = 0
int_c = 0
print("Enter the number of numbers:")
int_n = int(input())
while int_c < int_n:
    print("Enter number {}:".format(int_c + 1))
    float_t += float(input())
    int_c += 1
print("N = {}, Sum = {}".format(int_n, float_t))
print("Average = {:.2f}".format(float_t/int_n))
"""
# 运算符、类型转换
"""
print("------------------------------------------------------------------------------------")
# 整除
print("整除运算：22 // 12 = {}".format(22 // 12))
# 除法
print("除法运算：22 / 12 = {}".format(22 / 12))
# 取余
print("取余运算：22 % 12 = {}".format(22 % 12))
# 关系运算符 < <= > >= == !=
print("关系运算符：23 > 45 ?", 23 > 45)
# 逻辑运算符 and or not 优先级：A and not B or C 等于 (A and (notB)) or C
print("关系运算可以通过逻辑运算符and和or组合：", 2 > 1 and not 3 > 5 or 4)
# x op= expression 为简写运算的语法形式。其等价于 x = x op expression
a = 12
a += 13
print("a = 12, a += 13, a =", a)
n, N = 2, 100
while n < N:
    print(str(n))
    n *= n
# 类型转换
print("float(string)	字符串 -> 浮点值：float(\"123\") = ", float("123"))
print("int(string)	字符串 -> 整数值：int(\"123\") = ", int("123"))
print("str(integer)	整数值 -> 字符串：str(123) = ", str(123))
print("str(float)	浮点值 -> 字符串：str(123.456) = ", str(123.456))
"""
# 解二次方程
"""
print("\n-------------------------------------------------------------------")
# 计算数列 1/x + 1/(x+1) + 1/(x+2) + ... + 1/n,其中x = 1, n = 10
sum = 0
for i in range(1, 11):
    sum += 1.0 / i
    print("{:2d} {:.4f}".format(i, sum))
# 求解二次方程 quadratic_equation.py
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = b * b - 4 * a * c
if d < 0:
    print("ROOTS are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root1 = ",root1)
    print("Root2 = ",root2)
"""
#  控制流 if-elif-else
"""
print("\n-------------------------------------------------------------------")
x = int(input("Enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Integer")
else:
    print("More")
"""
# while循环
"""
print("\n-------------------------------------------------------------------")
# while循环   斐波那契数列1，1，2，3，4，5，8，13...
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b
print()
# 计算幂级数： e^x = 1 + x + x^2/2! + x^3/3! + ... + x^n/n! (0 < x <1)
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break                          # break可以终止最里面的循环，直接跳出
print("No of Times = {} Sum = {}".format(n, result))
# 打印九九乘法表
print("-" * 70)
i = 1
while i < 10:
    n = i
    while n < 10:
        print("{:5d}".format(n * i), end=' ')
        n += 1
    if i < 9:
        print()
        print(i * "      ", end='')
    i += 1
print()
print("-" * 70)
"""
# 列表
"""
print("-" * 70)
a = [1, 232, 456, 'India', 'Fedora']
print(a)
print(a[0], a[1])
print(a[-1], a[-2])
print(a[:])
print(a[:4])
print(a[1:])
print(a[-5:-1])
"""
# for循环
"""
print("-" * 70)
# 可以在循环后面使用可选的else语句，它将会在循环完毕后执行，除非有break语句终止了循环
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in a[::2]:
    print(x, end=' ')
print("-" * 50)
for n in range(0, 5):
    print(n, end=' ')
else:
    print("bye bye")

# range()函数，生成一个等差数列；range（）函数返回的并不是列表，而是一种可迭代对象
for i in range(5):
    print(i, end=' ')
print()
print(range(1, 15))
print(list(range(1, 15)))
print(list(range(1, 15, 3)))
print(list(range(2, 15, 2)))
# break 跳出并终止循环
# continue 跳过其后的代码回到循环开始处执行
while True:
    i = int(input("Enter an integer: "))
    if i < 0:
        continue
    elif i == 0:
        break
    else:
        print("Square is ", i ** 2)
print("Goodbye")
"""
# 棍子游戏
"""
sticks = 22
print("There are {} sticks, you can take 1-4 number of sticks at a time.".format(sticks))
print("Whoever will take the last stick will loose")
while sticks > 0:
    print("sticks left: ", sticks)
    sticks_taken = int(input("Take sticks(1-4): "))
    if sticks_taken > 4 or sticks_taken < 1 or sticks_taken > sticks:
        print("wrong choice")
        continue
    sticks -= sticks_taken
    if sticks == 0:
        print("You loose")
        break
    computer_taken = 5 - sticks_taken
    if sticks > computer_taken:
        sticks -= computer_taken
        print("Computer took: ", computer_taken)
    elif sticks <= computer_taken:
        sticks = 0
        print("Computer loose")
"""
# 列表
"""
# 列表
a = [1, 23, 45, 567, -789, -2, 45, -2, -2]
a.sort()
a.pop()
print(a)
# 列表推导式:由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。
squares1 = [x**2 for x in range(10)]
squares2 = list(map(lambda x: x**2, range(10)))
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(squares1)
print(squares2)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

a = [1, 2, 3]
z = [x + 1 for x in [x**2 for x in a]]
print(z)
"""
# 元组
"""
# 元组
a = "Fedora", "Shiyanlou", "Kubunbu", "Pardus"
b = 'Fedora1', 'Shiyanlou1', 'Kubuntu1', 'Pardus1'
print(a)
print(b)
print(a[0])
print(b[-1])
for x in a:
    print(x, end=' ')
# del a[0]                 元组是不可变类型，不能在元组内删除、添加、编辑任何值

print("\n", divmod(15, 2))
x, y = divmod(15, 2)
print(f"{x}, {y}")

c = (123)
print(f"c: {type(c)}")
d = (123,)
print(f"d: {type(d)}, len: {len(d)}")
"""
# 集合
"""
# 集合: 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print(a.pop())
print(a.pop())
a.add('f')
print(a)
"""
# 字典
"""
# 字典: 是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。一对大括号 {} 创建一个空字典。
data = {'kushal': 'Federa', 'kart_': 'Debian', 'jace': 'Mac'}
data['parthan'] = 'Ubuntu'
del data['kushal']
print(data)
print(data['kart_'])
dirc = {1: 'one', 2: 'two'}
print(dirc[1])
print('Shiyanlou' in data)
# dict（）可以从包含键值对的元组中创建字典
print(dict((('Indian', 'Delhi'), ('Bangladesh', 'Dhaka'))))
# 遍历字典
for x, y in data.items():
    print(f"{x} uses {y}")
# 给字典中的元素添加数据，并创建默认值
data.setdefault('names', []).append('Ruby')
data.setdefault('names', []).append('Python')
data.setdefault('names', []).append('Ruby')
print(data)
print(data.get('foo', 'not exist'))
# 在遍历列表（或任何序列类型）的同时获得元素索引值
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)
# 同时遍历两个序列类型
a = ['Pradeepto', 'Kushal']
b = ['OpenSUSE', 'Fedora']
for x, y in zip(a, b):
    print(f"{x} uses {y}")
"""
# 判断学生成绩是否达标的程序
"""
n = int(input("Enter the number of  students: "))
data = {}
Subjects = ('Physics', 'Maths', 'Hestory')
for i in range(n):
    name = input(f"Enter the name of the student {i + 1}: ")
    marks = []
    for x in Subjects:
        marks.append(int(input(f"Enter the mark of {x}: ")))
    data[name] = marks
for x, y in data.items():
    print(f"{x}'s total marks is {sum(y)}")
    if(sum(y) < 120):
        print(x, "failed :(")
    else:
        print(x, "passed :)")
"""
# 计算两个nxn矩阵的Hadamard乘积
"""
n = int(input("Enter the value of n: "))
print("Enter values of the Matrix A: ")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values of the Matrix B: ")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(sum(a[i][k] * b[k][j] for k in range(n)))
    c.append(temp)
print("After matrix multiplication")
print("-" * 7 * n)
for x in c :
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)
"""
# 字符串
print("-" * 100)
# '...'  "..."   """..."""或'''...''' 都可以表示字符串
# s1 = "s1: I am Chinese"
# print(s1)
# s2 = 's2: I am Chinese, too'
# print(s2)
# s3 = "s3: Here is a line \
#      split in two lines"
# print(s3)
# s4 = "s4: Here is a line \n split in two lines"
# print(s4)
# s5 = '''s5:
# \
#     Usage: thingy [OPTIONS]
#     -h                                 Display this usage message
#     -H hostname                        Hostname to connect to
#     '''
# print(s5)
# s6 = """s6:
# \
#     Usage: thingy [OPTIONS]
#     -h                                 Display this usage message
#     -H hostname                        Hostname to connect to
#     """
# print(s6)
# print("-" * 80)
# s = "I love you"
# print(s.title())   # 标题版本，单词首字母大写
# print(s.upper())   # 全部大写
# print(s.lower())   # 全部小写
# print(s.swapcase())      # 大小写交换
# st = "123abc4d5f"
# print(st.isalnum())      # 检查所有字符是否只包含字母和数字
# print(st.isalpha())      # 检查所有字符是否只包含字母
# print(st.isascii())
# print(st.isdigit())
# print(st.islower())
# print(st.isupper())
# print(st.istitle())
# st = "123ab c4d5f"
# print(st.isalnum())
# st = "abcdefg"
# print(st.isalpha())
# s = "We all love you"
# # split('字符')分割任意字符，允许有一个参数，用来指定字符串以什么字符分隔（默认为” “）。它返回一个包含所有分割后的字符串的列表
# print(s.split())
# s = "I:am:waiting"
# print(s.split(':'))
# # join()使用指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入，然后连接列表内的字符串元素
# print('-'.join("GNU/Linux is great".split()))
# print('-'.join(["I", "love", "you"]))
# # strip(chars) 剥离字符串首尾中指定的字符，默认剥离掉首位的空格和换行符
# s = "\na bc-"
# print(s.strip())
# print(s.strip('-'))
# print(s.lstrip())
# print(s.rstrip())
# # 搜索字符串里的文本或子字符串
# s = "Faulty for a reason"
# print(s.find("for"))
# print(s.find("fora"))
# print(s.startswith("Fa"))
# print(s.endswith("son"))
# print(s.__len__())
print("-" * 100)
# 回文检查
"""
s = input("Enter a string: ")
z = s[::-1]    # 把输入的字符串s 进行倒序处理形成新的字符串z
if s == z:
    print("The string is a palintrome")
else:
    print("The string is not a palindrome")
"""
# %格式化操作符
"""
print("I am %s, I am %d years old" % ('yt', 4))
# %s 字符串（用 str() 函数进行字符串转换）
# %r 字符串（用 repr() 函数进行字符串转换）
# %d 十进制整数
# %f 浮点数
# %% 字符“%”
s = input("Enter a line: ")
print("The number of words in the line are %d" % (len(s.split())))
"""