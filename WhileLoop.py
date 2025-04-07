#while condition:
    # Code to execute while the condition is True
    #statement_2
    #statement_1
#Condition: The loop continues as long as the condition evaluates to True.
#Indentation: The body of the loop must be indented.
#Termination: To avoid an infinite loop, ensure the condition eventually becomes False.

#1.Write a while loop that prints numbers from 1 to 10.

count=1

while count<=10:
    print(f"count is {count} ")
    count+=1
    
#2.Write a while loop that prints even numbers from 2 to 10.

count=2

while count<=10:
    print(f"from 2 to 10 {count} ")
    count+=2
    
#3.Write a while loop that prints even number below 10.



test = 0  # Start from the first even number below 10

while test < 10:  # Continue while the number is below 10
    if test % 2 == 0:  # Check if the number is even
        print(f"{test} is Even")
    test += 1  # Increment to check the next number




#Break

x=1

while x<8:
    print(f"Numbers {x}")
    if x==3:
      break
    x=x+1


#continue

a = 1
while a < 8:  
    a += 1
    if a == 3:
        continue
    print(f"Number {a}")
    
 # Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.
n = 9
sums = 0
counter = 1

while counter <= n:  # Loop until counter reaches n
    sums += counter  # Add the current counter to sums
    counter += 1     # Increment the counter

print(f"The sum of numbers from 1 to {n} is {sums}.")

    

