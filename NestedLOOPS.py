#Nested Loop =Aloop with in the other loop

'''rows=int(input("Enter the no of rows : "))
columns=int(input("Enter the no of columns : "))
symbol=input("enter symbol : ")

for i in  range(rows):
  for j in range(columns):
    print(symbol ,end=" ")
  print()'''
  
  ####Triangle For output
  
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print() 