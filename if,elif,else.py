###########Syntax############
'''if condition1:
    # Code block executed if condition1 is True
elif condition2:
    # Code block executed if condition1 is False and condition2 is True
else:
    # Code block executed if both condition1 and condition2 are False
'''


##Write a program that takes a number as input and prints "Even" if it's an even number, and "Odd" if it's an odd number.

input=int(input("Enter the Number : "))

if input * 2:
    print(f"This is the Even Number {input} ")
elif input % 2 ==0:
    print(f"This is the odd Number {input} ")
else:
    print(f"The condition terminates here")


######################################################

#2.Write a program that takes two numbers as input and prints the larger number.

Number1=int(input("Enter the First Number : "))
Number2=int(input("Enter the Second Number : "))

if Number1>Number2:
    print(f"{Number1} is the largest number ")
elif Number2>Number1:
    print(f"{Number2} is the largest number")
else:
    print(f"end")
    
    
    
    
 ###Need to check 3 rd Program because  of the Logic which I didn't got###  
    
    
#3.Write a program that takes a character as input and prints "Vowel" if it's a vowel (a, e, i, o, u), and "Consonant" otherwise.

Name=input("Enter the Name : ")
vowel=["a","e","i","o","u"]


contains_vowel = any(char in vowel for char in Name) 
contains_consonant = any(char.isalpha() and char not in vowel for char in Name)

#print(contains_vowel)
#print(contains_consonant)

# Output based on the checks
if contains_vowel and contains_consonant:
    print("The given name has both vowels and consonants.")
elif contains_vowel:
    print("The given name has only vowels.")
elif contains_consonant:
    print("The given name has only consonants.")
else:
    print("The given name does not contain valid alphabetic characters.")      

 
    
    
    
    
    
    
    
    