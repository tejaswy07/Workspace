##6 Relational Operators

#Relational operators in Python are used to compare values or expressions.
#They return a Boolean value (True or False) based on the comparison

'''Operator	Description	Example
==	Equal to	         5 == 5 → True
!=	Not equal to	     5 != 3 → True
>	Greater than	     7 > 5 → True
<	Less than	         3 < 8 → True
>=	Greater than or equal to	5 >= 5 → True
<=	Less than or equal to	    4 <= 6 → True '''

x=5
y=7

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


a="hello"
b="hello"

print(a==b)


#1.Example: Comparing integers and floats
test1=5.0 > 4
print(test1)

#2.Example: Comparing strings with different cases
test2= "Hello" == "hello"
print(test2)

#3.Example: Comparing strings
test3="apple" < "banana"
print(test3)

#4.Example: Mixing different types in comparisons
test4= 5 > "3"
print(test4)

