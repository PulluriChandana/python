age=int(input("Enter your age:"))
if(age<18):
    print("Your not an adult")
elif(age>18 and age<60):
    print("You are an adult")
else:
    print("You are a senior citizen")