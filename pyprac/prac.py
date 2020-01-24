# name= input("what is your name? ")
# print("Hi " + name)
# name = input("What is your name? ")
# color = input("what is your favorite color?" )
# print(name + " likes" + color)
# weight_lbs = input("Weight (lbs) ")
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)
course = 'Python for beginners'
# print(course.capitalize())
print(course.replace('P', 'J'))
print('Python' in course)
print(10**2)
x = 10
#x = 10 + 3
x -= 3
print(x)
x = 2.9
print(round(2.9))
import math
print(math.floor(2.9))
is_hot = True
is_cold = True
if is_hot:
    print("It is a hot day. Drink plenty of water. ")
elif is_cold:
    print("It is a cold day. Wear warm cloths. ")
else:
    print("It is a lovely day")
price = 1000000
good_credit = True
if good_credit:
    print(0.1 * price)
else:
    print(0.2 * price)
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
has_high_income = False
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
has_high_income = True
criminal_record = False
if has_high_income and not criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

temperature = 35

if temperature > 30:
    print("It is a hot day.")
elif temperature < 10:
    print("It is a cold day.")
else:
    print("It is not a hot day nor a cold day")

name = "Mohadesa"
if len(name)<3:
    print("Name must be at least 3 characters long.")
elif len(name)>50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!")
weight = input("Weight: ")
print("your input weight is ", weight)
weight_unit = input("(L)bs or (k)g: ")
print(" You choose ", weight_unit)
weight_lbs = float(weight) * 2.204
weight_kg = float(weight) * 0.45
if weight_unit == "k":
    print(weight_lbs, " lbs")
else:
    print(weight_kg, " kg")


