q = int(input("Enter the quantity of items: "))
if q > 1000:
    total = q * 100
    discount = (total * 10)/100
    print("Total : ", total)
    print("You will get 10 percent discount \U0001F973")
    print("Total amount after discount: ", total - discount)
    
else:
    total = q * 100
    print("Total : ", total)
    print("You will not get any discount \U0001F62D")
    print("Total amount: ", total)