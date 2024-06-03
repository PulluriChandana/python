def sumofdigits(num):
    digits=str(num)
    digit_sum=0
    for digit in digits:
        digit_sum+=int(digit)
    return digit_sum
num=input("Enter a number:")
print("Sum of digits in",num,"is",sumofdigits(num))