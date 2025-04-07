##Avoid nested conditional statments make it simpler always!
##In order to maintain the code and read the code avoid complex nested conditions prefer as simple as possible
##These Nested statments are preferabble when the program is in complex state  

x = 10
y = 20

if x > 5:
    print("x is greater than 5")
    if y > 15:
        print("y is also greater than 15")
    else:
        print("y is not greater than 15")
else:
    print("x is not greater than 5")
    
    
#########################################################


a = 10
b = 5

if a > 5:
    if b > 5:
        print("Both a and b are greater than 5")
    elif b == 5:
        print("a is greater than 5 and b is equal to 5")
    else:
        print("a is greater than 5 but b is less than 5")
else:
    print("a is not greater than 5") 
    
########################################################      

#3.Check if a given number num is positive, negative, or zero. 

Number=int(input("Enter the Number : "))

if Number==0:
    print("Number is Zero")
elif Number>0:
        print("Number is Positive")
else:
        print("Number is Negative") 


#############################################################

#4.Determine the type of a given number `num`: even or odd, and whether it is positive or negative.

check = int(input("Enter the number: "))

if check > 0:
    if check % 2 == 0:
        print("The number is Positive and it is Even")
    else:
        print("The number is Positive and it is Odd")
elif check < 0:
    if check % 2 == 0:
        print("The number is Negative and it is Even")
    else:
        print("The number is Negative and it is Odd")
else:
    print("The number is Zero")