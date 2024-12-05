'''### BODMAS

The BODMAS rule stands for:

1. B - Brackets first
2. O - Orders (exponents and roots, like square roots) next
3. DM - Division and Multiplication, from left to right
4. AS - Addition and Subtraction, from left to right'''


result = 10 + 5 * (2 ** 3) - 6 / 2

print(result)


#2.Print the letter multiple times 

a="Hello" * 5

print(a)


#3.Length Of The String

name=input("Enter your Name : ")

check=len(name)

print(check)

#4.1. Concatenate two strings `str1` and `str2`, and print the result.
   # - **Expected Input:** str1 = "Hello", str2 = "World"
   #- **Expected Output:** "HelloWorld"
   
First="Hello"
second="world"

print(First+second)

# 5.Ask the user to enter a word and a number. Repeat the word as many times as the given number and print the result.
    #- **Expected Input:** word = "Hello", number = 3
    #- **Expected Output:** "HelloHelloHello"
    
Word=input("Enter the word")
number=int(input("Enter the Number:") )

result=Word*number

print(result)

#6.6. Ask the user to input a sentence. Find the length of the sentence, and print the last character of the sentence.
   # - **Expected Output:** Length of the sentence and the last character.
   
sentence=input("Enter the sentence : ")
length=len(sentence)
index=sentence[-1]

print(f"Length of the sentence: {length}")
print(f"Last character of the sentence: {index}")



