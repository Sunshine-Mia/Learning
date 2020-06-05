import os
import sys

# open(file,mode,encoding='UTF-8')打开文件
"""
第一个参数是文件路径或文件名，第二个是文件的打开模式
"r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
"w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
"a"，以追加模式打开，写入到文件中的任何数据将自动添加到末尾
"""


# fobj = open("C:\\Users\\Admin\\Desktop\\Temp\\test.txt", 'r', encoding= 'UTF-8')
# print(fobj)

# read(size)文件读取        size没有指定或指定为负数，就会读取并返回整个文件
# print(fobj.readline())              # 每次读取第一行
# print(fobj.readlines())             # 读取所有行到一个列表中
# print(fobj.read(10))                # 读取文件

# close()关闭文件
# fobj.close()

# write()写入文件
# fobj.write('I Love You\n')
# fobj.write("I love you!\n")
# fobj.write('123456\n')
# print(fobj.read())
# fobj.close()

"""
def parse_file(path):
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i, line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()
    return spaces, tabs, i + 1


def main(path):
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print(f"Spaces {spaces}. Tabs {tabs}. Lines {lines}")
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
"""

with open("C:\\Users\\Admin\\Desktop\\Temp\\test.txt") as fobj:
    for line in fobj:
        print(line, end='')
