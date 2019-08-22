filename = input("What's your filename? :")
txt = open(filename)#通过open打开文件
print(f"Here's your file {filename}:")#输出你这是你的文件
print(txt.read())#阅读文件内容，同时输出内容
print("Type the filename again:")#再一次打开文件
file_agin = input(">")#文件名通过input输入
txt_again = open(file_agin)#打开文件
print(txt_again.read())#输出文件内容
