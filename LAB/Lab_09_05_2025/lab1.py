# Write a program for arithmatic operators

i = 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
while i == 1:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        result = num1 + num2
        print("Result:", result)
        i = 2
    elif choice == 2:
        result = num1 - num2
        print("Result:", result)
        i = 2
    elif choice == 3:
        result = num1 * num2
        print("Result:", result)
        i = 2
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
            i = 2
        else:
            print("Cannot divide by zero")
            i = 2
    else:
        print("Invalid choice Please Enter a valid choice")
        i = 1
        
        
        