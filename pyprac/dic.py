"""
Python dictionaries
"""

# information is stored in the list is [age, height, weight]
d = {"ahsan": [35, 5.9, 75],
     "mohad": [24, 5.5, 50],
     "moein": [5, 3, 20],
     "ayath": [1, 1.5, 12]
     }
print(d)
d["simin"] = [14, 5, 60]
d.update({"simin": [14, 5, 60]})
print(d)
age = d["mohad"][0]
print(age)
for keys, values in d.items():
    print(values, keys)
d["ayath"] = [2]
d.update("ayath")
# Exercises

# 1 Store mohad age in a variable and print it to screen
# 2 Add simin info to the dictionary
# 3 create a new dictionary with the same keys as d but different content i.e occupation
# 4 Update ayath's height to 2 from 1.5
# 5 Write a for loop to print all the keys and values in d
