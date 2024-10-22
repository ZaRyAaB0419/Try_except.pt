try:
    num=int(input("Enter your number:"))
    print("your number is:", num)

except ValueError as ex:
    print("exception:", ex)
