#Write a program that takes a year as input and prints "Leap Year" 
# if it's a leap year, and "Not a Leap Year" otherwise.


year=int(input("Enter the Year : "))
Test = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print("Given Year Is Leap Year ")
else:
     print("Given Year is Not leap Year")
    
    #Logic in simple words 
    #If Year Divisible by 4
    #If Year Divisible by 400
    #If Year Not Divisible by 100
    
    
    #################################################
    
    #Write a program that takes a grade as input (A, B, C, D, or F) and prints "Pass" 
    #if it's A, B, C, or D, and "Fail" if it's F.
    
Check=input("Enter the Grades : ")
PassedGrades=["A","B","C","D","a","b","c","d"]
FailedGrades=["F","f"]
    
if Check in PassedGrades:
        print("Pass")
elif Check in FailedGrades:
        print("Failed")
else:
        print("not define")     
    
