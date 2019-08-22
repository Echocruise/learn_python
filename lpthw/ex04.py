cars = 100 # 有100辆车
space_in_a_car = 4.0 #每辆车载人4
drivers =30 #司机30人
passengers =90 #乘客90人
cars_not_driven =cars - drivers #计算司机开的车
cars_driven = drivers  #有司机开的车
carpool_capacity = cars_driven * space_in_a_car #总共能装多少人
average_passengers_per_car = passengers /cars_driven #平均每辆车装多少人
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven,"empty cars today")
print("We can transport", carpool_capacity,"people today")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car")
