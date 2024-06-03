def count(num):
    num_str=str(num)
    return len(num_str)
number=input("Enter a number:")
print("Number of a digits in",number,"is",count(number))