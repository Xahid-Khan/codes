l = []
for line in open("age.txt"):
    li=line.strip()
    if not li.startswith("#"):
        l.append(li)
        print(li)
def sort_tuple(rows):
    """
    First process rows with dob from day, month year format to age in years format
    then sort the processed rows.
    """
    #processed rows
    prows = []
    #loop for processing dob to age
    for row in rows:
        fName, lName, dob = row.split(" ")
        dob_dmy = dob.split("/")
        age = (2020 - int(dob_dmy[2])) + (1 - int(dob_dmy[1]))/12 + (24 - int(dob_dmy[0]))/365
        prows.append(
            (fName, lName, age)
        )
        
    #print (tup)
    for k in range(0, len(prows)):
        for j in range(0, len(prows)-k-1):
            if (prows[j][2]>prows[j+1][2]):
                temp = prows[j]  
                prows[j]= prows[j + 1]  
                prows[j + 1]= temp
    return prows   
import sys       
ageSorted = sort_tuple(l)
# if sys.argv[1].lower() == "a":
#     print(ageSorted)
# elif sys.argv[1].lower() == "d":
#     ageSorted.reverse()
#     print(ageSorted)
# else:
#     print("Invalid option. Choose 'a' for ascending and 'd' for descending order")
# print(sys.argv, type(sys.argv))
if len(sys.argv) == 1:
    print(ageSorted)
elif sys.argv[1].lower() == "a":
    print(ageSorted)
elif sys.argv[1].lower() == "d":
    ageSorted.reverse()
    print(ageSorted)
else:
    print("Invalid option. Choose 'a' for ascending and 'd' for descending order")


