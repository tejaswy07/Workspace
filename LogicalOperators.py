#AND/OR/NOT These are the Logical Operators


x=5.7
y=20

Test1=(x>y) and (x==y)
print(Test1)

Test2=(x>1) and (y>10)
print(Test2)

Test3=(x>3) or (y>20)
print(Test3)


#Example: Using "not" operator with an expression

x=10
y=5

print(not(x > y and "car" != "car")) #--The inside condition is False but applying the NOT operater the result flips to True

print(not (2 < 5 and (7 > 3 or "hello" == "world")))