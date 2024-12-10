


name="teja"
#print("Hello"+name)

print(name.capitalize()) #--only first letter is capitalized
print(name.find("a"))
print(name.upper()) #--ALL CAPITALS
print(name.lower()) #--All lower
print(name.isdigit()) #--checks is it a number or not
print(name.isalpha()) #Checks it consists of only string letters then the output gives True but if consists of spaces,Numbers,special characters the it returns False                
print(name.count("e"))    
print(name.replace("t","a"))
print(name.strip())#strip(): Removes leading and trailing whitespaces from the string.


Check="New,string"              
string=Check.split(",") #Splits the string into a list of substrings based on a delimiter.
print(Check)


string2=Check.startswith("New") #Checks if the string starts with a specific prefix.outputTrue/False
print(string2)


string3=Check.endswith("string") #Checks if the string ends with a specific suffix
print(string3)


Input=input("Enter the input : ")

Test=Input.replace("Python","java")

print(Test)