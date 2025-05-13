salary = float(input("Enter your salary: "))
year = float(input("Enter the year of service: "))
if year > 5:
    bonus = (salary * 5)/100
    print("Bonus: ", bonus)
else : 
    print("No bonus :-/")