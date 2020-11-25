import math
def calculate(x,y,z):
    if z>x+y:
        return False
    if z==0:
        return True
    g=math.gcd(x,y)
    return z%g==0
        
x,y=input("Enter the capacity of two water jugs").split()
x=int(x)
y=int(y)

z=int(input("Entre the litre that has to be measured using two jugs"))
val=calculate(x,y,z)
print(val)
