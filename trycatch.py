#trycatch block
try:
    numerator=float(input("Enter a number:"))
    denominator=float(input("Enter a number:"))
    result=numerator/denominator
    print("Result:",result)


except ZeroDivisionError:
    print("ZeroDivision Error")
except ValueError:
    print("Invalid Input.Please enter valid input numbers")
except Exception as e:
    print("An exception occured",e)


