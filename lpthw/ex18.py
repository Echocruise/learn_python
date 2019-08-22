# this one is like your script with argv
def print_two(*args):#函数名为print_two，多个参数的方式可以是*args
# That tells Python to take all the arguments to the function and then put them in args as a list.
    arg1, arg2 = args #因为使用*args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):#这里不用*args而是用arg1,arg2
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")
#this one takes on arguement
def print_none():
    print("I got nothing")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
