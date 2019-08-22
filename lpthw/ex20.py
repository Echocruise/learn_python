from sys import argv # 倒入argv模块

script, input_file =argv # 两个参数 ex20.py ex20.txt 定义参数

def print_all(f): # 定义函数 读取txt的内容
    print(f.read())

def rewind(f):
    f.seek(0)#file.seek是将文件游标移动到文件的任意位置，然后对文件的当前位置进行操作（增加、删除内容等）
    # help（f.seek）

def print_a_line(line_count, f):
    print(line_count, f.readline())#指定读取第几行的内容


current_file=open(input_file)# 打开 inputfile ex20.txt

print("First let's print the whole file:\n")

print_all(current_file)


print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line= 1
print_a_line(current_line,current_file)
current_line= current_line +1
print_a_line(current_line,current_file)
current_line= current_line +1
print_a_line(current_line,current_file)
