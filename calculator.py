
def calc():
    print("What would you like to calculate?")
    imp1 = input("First Number:  ")
    imp2 = input("Operator:  ")
    imp3 = input("Second Number:  ")

    if imp2 == "+":
        output = int(imp1) + int(imp3)
    elif imp2 == "-":
        output = int(imp1) - int(imp3)
    elif imp2 == "*":
        output = int(imp1) * int(imp3)
    elif imp2 == "/":
        output = int(imp1) / int(imp3)

    else:
        print("This operation is not valid yet")
    
    print(output)