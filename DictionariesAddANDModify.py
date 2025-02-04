# Example: Dictionary methods
student = {
    "name": "Teja",
    "age": 28,
    "major": "Computer Science",
    "gpa": 3.8
}

# Get keys and values
keys = student.keys()
values = student.values()

print(keys)   # Output: dict_keys(['name', 'age', 'major', 'gpa'])
print(values) # Output: dict_values(['Teja', 28, 'Computer Science', 3.8])

#Check if a key exists in the dictionary

if "major" in keys:
    print("yes")
else:
    print("no")
    

# Remove a key-value pair from the dictionary

remove=student.pop("age")

print("removed value" ,remove)
print(student)  


#1Question: Given the initial dictionary employee as {"name": "Deepika", "age": 28}, modify the value of the key "age" to 35.
#Expected Input: employee = {"name": "Deepika", "age": 28}
#Expected Output: {"name": "Deepika", "age": 27}

Dic2={
    "PersonName":"Deepika",
    "age":"28"
}

Dic2["age"]="27"


print(Dic2)


#Question: Add a new key-value pair to the dictionary fruits, where the key is "orange" and the value is 3.
#Expected Input: fruits = {"apple": 5, "banana": 7}
#Expected Output: {"apple": 5, "banana": 7, "orange": 3}


fruits={
    "apple": 5,
    "banana": 7
}

fruits["orange"]=3
print(fruits)


#Question: Given the dictionary inventory, remove the key "sugar" and its associated value from the dictionary.
#Expected Input: inventory = {"apple": 10, "banana": 15, "sugar": 2}
#Expected Output: {"apple": 10, "banana": 15}


inventory = {"apple": 10, "banana": 15, "sugar": 2}

inventory.pop("sugar") # Remove a key-value pair from the dictionary

print(inventory)










