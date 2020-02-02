import sys

def numSum(a, b):
    c = a + b
    return c

fname, num1, num2 = sys.argv 
print(type(num1), type(float(num1)))
no = numSum(num1, num2)
print(no)
print(fname)
print(sys.argv)

    

