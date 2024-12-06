#Index of first character - 0 
#Index of last character - (length - 1)


string="Robert Pattinson"

select1=string[0:6]
select2=string[1]
select3=string[-1] #--Get the last character of the sentence
select4=string[3:9] #--Get a substring from index 3 to index 9 (exclusive).
select5=string[-2] #--Get the second last character of the sentence
select6=string[7:] #--starts with index 7 and prints from 7 to end i.e Pattinson
select7=string[:-8]
select8=string[-8:-1]


print(f"select1 ={select1} " )
print(f"select2 ={select2} " )
print(f"select3 ={select3} " )
print(f"select4 ={select4} " )
print(f"select5 ={select5} " )
print(f"select6 ={select6} " )
print(f"select7 ={select7} " )
print(f"select8 ={select8} " )



#2.Example: Reverse the sentence using slicing.
#Input: "Python is awesome!"
#Output: "!emosewa si nohtyP"


#string[start:end:step]

Input="Python is awesome!"
slice=Input[::-1] #-- -1 indicates reverse
print(slice)


#==============================================




