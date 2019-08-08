'''
Created on 21-Jun-2019

@author: Rishi
'''
from builtins import str
x= 100
y= 200
z= 300

#Simple operators
print("Addition : " + str(x+y))
print("Subtract : " + str(y-x))
print("Devision : " + str(y / x))
print("Multiplication : " + str(x * y))
print("Modulus : " + str(x % y))

#Comparision
print("Greater than x>y :: " + str(x>y))
print("Less than x<y :: " + str(x<y))
print("Greater than and equals to x>=y :: " + str(x >= y))
print("Less than and equals x<=y :: " + str(x <= y))
print("Not equals :: (x!= y) " + str(x != y))
print("Equals to :: (x == y) " + str(x == y))

#Logical
boolOne = x < y
boolTwo = y < z

'''
& AND 
T    T    T
F    T    F
T    F    F
F    F    F
'''
print("Logical AND " + str(boolOne & boolTwo))

'''
| OR 
T    T    T
F    T    T
T    F    T
F    F    F
'''
print("Logical OR " + str(boolOne | boolTwo))



