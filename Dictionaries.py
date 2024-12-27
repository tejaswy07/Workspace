#Dictionaries are meant to sttore key-value pairs.

#You can create a dictionary by enclosing key-value pairs in curly braces.

student = {
    "name": "Teja",
    "age": 28,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student)
print(student["gpa"]) #You can access values in a dictionary using keys.

#Question: Create an empty dictionary.
#Expected Output: {}

empty={}
print(empty)



#Question1: Create a dictionary to store the age of two people, "John" and "Alice." John is 25 years old, and Alice is 30 years old.
#Expected Output: {"John": 25, "Alice": 30}

Dic={
    "name1":"john",
    "age1":"25",
    "name2":"Alice",
    "age2":"30"
}

print(Dic)


#Question: Access the value associated with the key "city" from the given dictionary.
#Expected Input: Dictionary: {"name": "Alice", "city": "New York", "age": 30}
#Expected Output: "New York"

Dic2={
   "Person1":"Alice",
   "City":"New York",
   "age":"28"
}

print(Dic2["City"])


#Question: Access the value associated with the key "phone" from the given dictionary. If the key does not exist, return "Not available."
#Expected Input: Dictionary: {"name": "Eve", "age": 27}
#Expected Output: "Not available"

test={
   "name": "Tez",
   "age": 28 
}

if "phone" in test:
    print("Available")
else:
    print("Not Availabe")    