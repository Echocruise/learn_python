from sys import argv
script,filename = argv
print(f"We're going to erase {filename}.")#erase抹掉
print(f"If you don't want that, hit CTRL-c(^c).")
print("If you do want thar, hit RETURN.")

input("?")
print("Opening the file ...")

target = open(filename,'w')# 参数w为write的缩写
print("Truncating the file. Goodbye!")
target.truncate()#什么作用？Empties the file 清空整个文件的内容
print("Now I'm going ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)#分别写入三行
target.write("\n")#换行？
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()## 关闭文件
