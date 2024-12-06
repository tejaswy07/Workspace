#1.By using Type we can check what is the datatype of that column 

Given=int("123")
print(type(Given))


#2.Type conversion Float to Int

Floatnumber=3.14
number=int(Floatnumber)
print(type(number))
print(number)#--here the output is obtained as 3 

#3.Convert the boolean True to an integer

Booleanresult=True
Boolean_convert=int(True)

print(Boolean_convert) #--will obtaine the output as 1


Booleanresult2=False
Boolean_convert2=int(False)

print(Boolean_convert2) #--will obtaine the output as 0

#Convert the string "False" to a boolean.

str="False"
Boolean_str=bool(str)

print(Boolean_str) #--The Output returns True because the string is Not empty 