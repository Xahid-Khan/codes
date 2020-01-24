weight = input("Enter weight: ")
#if weight.isnumeric():
    #print("Valid input")
    #pass
#else:
    #print("invalid input")
    #exit("invalid input")

while not weight.isnumeric():
    weight = input("Enter weight: ")

weight_unit = input("Choose unit from Lb or Kg: ")
print("your input weight is ", weight, weight_unit)
#print(" You choose ", weight_unit)
weight_lbs = float(weight) * 2.204
weight_kg = float(weight) * 0.45
# if weight_unit == "kg" or weight_unit == "Kg" or weight_unit == "KG" or weight_unit == "kG" :
# #     print(weight_lbs, " lbs")
# # elif weight_unit == "LB" or weight_unit == "Lb" or weight_unit == "lb" or weight_unit == "lB":
# #     print(weight_kg, " kg")
# # else:
# #     print("Invalid input for unit")
if weight_unit in ["KG", "Kg", "kG", "kg"]:
    print(weight_lbs, " lbs")
elif weight_unit in ["LB", "Lb", "lb", "lB"]:
    print(weight_kg, " kg")
else:
    print("Invalid input for unit")