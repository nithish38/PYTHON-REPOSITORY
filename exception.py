try:
    n=int(input("enter the number:"))
    res=50/n
except ValueError:
    print("you have given as the value.it is division by zero error")
else:
    print("the value is",res)
finally:
    print("the program ends")