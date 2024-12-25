#Lists are mutable-these can be modified

fruits = ["apple", "banana", "orange"]


fruits.append("Papaya")  #Adding Elements
print(fruits)

fruits.remove("orange")  #Remove Elements
print(fruits)


test=["a","g","c","b"]  #Sorting Elements
test.sort()
print(test)

#1.Write a Python program that takes a list of numbers [1, 2, 3, 4, 5] and prints each number on a new line.

Numbers=[1,2,3,4,5]

for i in Numbers:
    print(i)
    
#2. Given a list of strings ["apple", "banana", "orange"], concatenate all the strings together with a space in between and print the result.

Input = ["apple", "banana", "orange"] 
result = " ".join(Input)  #Join can be used to concatinate the strings 
print(result + " ")


#3. Write a Python function that takes a list of numbers as input and returns the sum of all the numbers.
    
Fix = [1, 2, 3, 4, 5]
Tnew = 0 
for i in Fix: 
    Tnew += i 
    # Print the final total after the loop is complete 
print(Tnew)


#4.Given a list of numbers [10, 20, 30, 40, 50], find the maximum number using the `max()` function and print the result.
    
Newlist=[10,20,30,40,50]
Newresult=max(Newlist)

print(Newresult)

#5 Write a Python program that takes a list of names ["Alice", "Bob", "Charlie"] and checks if a given name (e.g., "Alice") is present in the list. Print "Name found" if the name is in the list; otherwise, print "Name not found".
    
Names = ["Alice", "Bob", "Charlie"]
FindName="Alice"

if FindName in Names:
    print("Name is Found")
else:
    print("Not Found")
    
#ReversedList

number1 = [1, 2, 3, 4, 5]
ReversedNum=[]


for i in reversed(number1):
    ReversedNum.append(i)
    
print(ReversedNum)

 

   
 