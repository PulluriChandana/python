#string functions
#String Concatination
str1="Pulluri"
str2="Chandana"
str_conact=str1+str2
print("String Conactination:",str_conact)
#length of a string
str_length=str.__len__(str1)
print("String length:",str_length)
#Indexing of a string
str_Indexing=str1[0:3]
print("String Indexing:",str_Indexing)
#String Slicing
str_Slicing=str1[:3]
str_Slicing1=str1[-3:]
print("First 3 characters of slicing:",str_Slicing)
print("Last 3 characters of slicing:",str_Slicing1)
#String Uppercase
str_upper=str.upper(str1)
print("Upper case string:",str_upper)
#Substring
if "uri" in str1:
    print("Substring is there")
else:
    print("Substring is not there")
#String Reverse
str_reverse="".join(reversed(str1))
print("String Reversed:",str_reverse)
#String replace
str_replace=str1.replace('l','d')
#str_replace = str1.replace('l', 'd')
print("String replacing:",str_replace)
