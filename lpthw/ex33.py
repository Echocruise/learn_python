def fun(n):
  i = 0
  numbers = []
  while i < n:
    print(f"At the top is {i}")
    i +=1
    print("Number now:", numbers)
  print("The numbers:")
  for num in numbers:
      print(num)
nu = int(input("Pleas input a number:"))
fun(nu)
