def is_palindrome(name):
    name=name.replace(" "," ").lower()
    return name==name[::-1]
print(is_palindrome("Racar"))
print(is_palindrome("Hello"))

def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        print("Enter a valid input")

string_input=input("Enter a string:")
integer_output=string_to_integer(string_input)
if integer_output is not None:
    print("Integer representation:",integer_output)

