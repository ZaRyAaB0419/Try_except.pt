try:
    num1, num2=eval(input("Enter num1, num2:"))
    result= num1/ num2
    print("your number is:", result)

except ZeroDivisionError:
    print("Dont add zero!¡!¡")

except SyntaxError:
    print("Forget to add the comma!¡!¡")

except:
    print("wrong input")

else:
    print("No exceptions")

finally:
    ("I will execute everytime")
