List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(List)
for list in List:
    if list%2==0:
        print(f"{list} is even")
    else:
        print(f"{list} is odd")
My=[*range(1,21)]
print(My)
for li in My:
    if li%2==0:
        print(f"{li} is even")
    else:
        print(f"{li} is odd")
