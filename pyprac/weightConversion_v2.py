weight = input("Enter weight: ")
while not weight.isnumeric():
    weight = input("Enter weight: ")

weight_unit = input("Choose unit from Lb or Kg: ")
print("your input weight is ", weight, weight_unit)
weight_in_pound = 0
weight_in_kg = 0
if weight_unit in ["KG", "Kg", "kG", "kg"]:
    weight_in_pound = float(weight) * 2.204
    weight_in_kg = weight
    print(weight_in_pound, " lbs")
elif weight_unit in ["LB", "Lb", "lb", "lB"]:
    weight_in_kg = float(weight) * 0.45
    weight_in_pound = weight
    print(weight_in_kg, " kg")
else:
    print("Invalid input for unit")


print(weight_in_pound, weight_in_kg)