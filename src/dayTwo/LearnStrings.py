'''
Created on 21-Jun-2019

@author: Rishi
'''
strvar = "  This, is, test, String   "
print(strvar)
print(strvar[3] + strvar[5])
print(strvar[2:6])
print(len(strvar))
x = len(strvar)
print(strvar[0:x])
print(strvar.strip())
print(strvar.lower())
print(strvar.upper())
print(strvar.replace("T", "J"))
print(strvar.isnumeric())
print(strvar.split(sep=",", maxsplit=2))
intStr = "100"
print(intStr.isnumeric())