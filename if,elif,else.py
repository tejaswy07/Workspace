###########Syntax############
'''if condition1:
    # Code block executed if condition1 is True
elif condition2:
    # Code block executed if condition1 is False and condition2 is True
else:
    # Code block executed if both condition1 and condition2 are False
'''


##Write a program that takes a number as input and prints "Even" if it's an even number, and "Odd" if it's an odd number.

Check=int(input("Enter the Number : "))


if Check % 2 ==0:
    print(f"This is the even Number {Check} ")
else:
    print(f"This is odd number")


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



if Name in vowel:
     print("vowel")
else:
     print("Not vowel")    
    
    
    
    
    
    
    
    