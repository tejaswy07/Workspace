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