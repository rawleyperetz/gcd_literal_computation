#we will need the floor function
import math

def gcd_val(firstnumber, secondnumber):
    if firstnumber < secondnumber:
        firstnumber, secondnumber = secondnumber, firstnumber 
    number = []
    number.append(firstnumber)
    number.append(secondnumber)
    quotient = math.floor(firstnumber/secondnumber)
    remainder = firstnumber - (secondnumber * quotient)
    number.append(remainder)
    print(firstnumber, '=', secondnumber, '*', quotient, '+', remainder)
    r = remainder
    j = 1
    while r > 1:
        a = number[j]
        b = number[j+1]
        q = math.floor(a/b)
        if q == 1:
            break
        else:
            r = a - (b*q)
            number.append(r)
            print(a, '=', b, '*', q, '+', r)
            j = j + 1

print(gcd_val(30,7))
print(gcd_val(7,30))
#into an array because we will need it to iterate
'''number = []

#the two number needed
firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))

#numbers are added to the number array
number.append(firstnumber)
number.append(secondnumber)

#returns the quotient
quotient = math.floor(firstnumber/secondnumber)

#returns the remainder and appends the remainder
remainder = firstnumber - (secondnumber * quotient)
number.append(remainder)

print(firstnumber, '=', secondnumber, '*', quotient, '+', remainder)

r = remainder
j = 1
while r > 0:
    a = number[j]
    b = number[j+1]
    q = math.floor(a/b)
    if q == 0:
        break
    else:
        r = a - (b*q)
        number.append(r)
        print(a, '=', b, '*', q, '+', r)
        j = j + 1'''
    
