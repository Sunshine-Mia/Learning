import math
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrome(s):
        print("yes")
    else:
        print("no")

def test(a, b=-99):
    if a > b:
        return True
    else:
        return False
print(test(1))
print(test(b = 2, a = 1))

# def f(a, data = []):
#     data.append(a)
#     return data
def f(a, data = None):
    if data is None:
        data = []
    data.append(a)
    return data
print(f(1))
print(f(2))
print(f(3))

# 强制关键字参数
def hello(*, name  = 'User'):
    print("hello,",name)
# hello('ytt')
hello(name = 'ytt')

# 文档字符串
def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.
    :param a: Side a of the triangle
    :param b: Side b of the triangle
    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4,5))

# 高阶函数/仿函数    - 使用一个或多个函数作为参数     - 返回另一个函数作为输出
def high(l):
    return [i.upper() for i in l]

def test2(h, l):
    return h(l)

l = ['python', 'Linux', 'Git']
print(test2(high, l))

# map函数         - 它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果。
lst = [1, 2, 3, 4, 5]
def square(num):
    return num**2


print(list(map(square, lst)))