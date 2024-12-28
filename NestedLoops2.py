#First example 
n = 5

# Outer loop for rows
for i in range(n):
    # Inner loop for columns
    for j in range(7):
        print("*", end="")  # Print star without a newline
    print()  # Move to the next line after each row
    
#Second example


for x in range(1, 6):
    for y in range(1, 6):  
     print(x*y, end="  ")
    print() 
    
    
# Number of rows for the triangle
n = 5

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(j)


# Example: Equality and inequality comparison
string1 = "hello"
string2 = "Hello"

if string1 == string2:
    print("Both strings are equal.")
else:
    print("The strings are not equal.")

if string1 != string2:
    print("The strings are not equal.")
else:
    print("Both strings are equal.")
            
            
# Example: Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "orange"]

# Creating a mixed-type list
mixed_list = [1, "apple", True, 3.14]   

print(numbers,fruits,mixed_list)         
print(fruits[0])  # Output: "apple"
print(fruits[2])    

fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits) 

# Example: List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = list1 * 3
print(repeated_list) 



# Example: List methods
fruits = ["apple", "banana", "orange"]

# Adding elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Sorting elements
fruits.sort()
print(fruits)  # Output: ['apple', 'grape', 'orange']



student = {
    "name": "Teja",
    "age": 28,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student["name"])  # Output: "Dodagatta Nihar"
print(student["gpa"])   # Output: 3.8


def greet():
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!


def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Alice")  # Output: Hello, Alice!



def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Tejaswy")  # Output: Hello, Alice!



def add_numbers(a, b):
    return a + b

# Calling the function and storing the result in a variable
result = add_numbers(3, 5)
print(result)  # Output: 8


