# try...except 处理异常：一个空的 except 语句能捕获任何异常。异常是一种 类
# try 语句还有另一个可选的 finally 子句，目的在于定义在任何情况下都一定要执行的功能。在真实场景的应用程序中，finally 子句用于释放外部资源（文件或网络连接之类的），无论它们的使用过程中是否出错。
# def get_number():
#     number = float(input("Enter a float number: "))
#     return number
#
# while True:
#     try:
#         print(get_number())
#     except ValueError:
#         print("You entered a wrong value.")

try:
    raise KeyboardInterrupt
except ValueError:
    print("Value error！")
finally:
    print("Goodbye, world!")


# raise 抛出异常
# raise ValueError("A value error happened.")

try:
    raise InterruptedError("...")
except InterruptedError:
    print("123")

# with语句是try-finally块的简写