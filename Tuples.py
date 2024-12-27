# tuples are immutable once create we cannot add or remove


fruits = ("apple", "banana", "orange")
coordinates = (3.14, 2.71)

print(fruits[0])
print(fruits[1])

#1.Example
Person=("Teja","28","London")
name,age,city=Person

print(name)
print(age)
print(city)

#Tuples support various built-in functions like len(), min(), and max()

Num=(1,2,3,4,5)
print(len(Num))
print(max(Num))
print(min(Num))


#Create a tuple containing three elements: 'apple', 5, and True.
#Expected Input: No input required.
#Expected Output: ('apple', 5, True)

Three=("apple","5","True")
print(Three)


#Access the second element from the given tuple: ('cat', 'dog', 'bird', 'fish').
#Expected Input: No input required.
#Expected Output: 'dog'

Test=("cat","dog","bird","Fish")
pet1,pet2,pet3,pet4=Test
print(pet2)


#Concatenate two tuples: (1, 2, 3) and ('a', 'b', 'c').
#Expected Input: No input required.
#Expected Output: (1, 2, 3, 'a', 'b', 'c')

First=("1","2","3")
Second=("a","b","c")

print(First+Second)


#Check if the element 25 exists in the tuple: (10, 20, 30, 40, 50).
#Expected Input: No input required.
#Expected Output: False

Check=("10","20","30","40","50")

if "25" in Check:
    print("True")
else:
    print("False")    
