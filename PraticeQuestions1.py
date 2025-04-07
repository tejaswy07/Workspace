#1. Declare two variables `a` and `b`, assign integer values to them, and print their sum.
    #- **Expected Output:** The sum of `a` and `b`'''
    
a= 3
b= 5
    
print(a+b)

#3. Define a variable `pi` and assign the value of π (pi) to it. Print the value of `pi`.
    #- **Expected Output:** The value of π (pi), e.g., 3.14159.
    
a=3.14

print(a)


#4. Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type.
    #- **Expected Input:** "True" or "False"
    #- **Expected Output:** The data type of the converted boolean.
    
is_raining="Enter True or False :  "

print(bool(is_raining))


#5. Create a string variable `sentence` containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times.
    #- **Expected Input:** A number (e.g., "3")
    #- **Expected Output:** The sentence repeated the specified number of times.
    
sentence=int(input("Enter your Favourate Number : "))  

if sentence > 0:
    print(sentence) 
    
'''
If I use the below code using while loop I will stuck in the loop 

sentence=int(input("Enter your Favourate Number : "))  

while sentence > 0:
    print(sentence) 

'''

#6 x raised to the power of y.

# Input the base (x) and exponent (y)
x = float(input("Enter the base (x): "))
y = float(input("Enter the exponent (y): "))

# Calculate power using pow()
result = pow(x, y)
# Can be done this way as well result = x ** y

# Display the result
print(f"{x} raised to the power of {y} is {result}")
print(result)

 