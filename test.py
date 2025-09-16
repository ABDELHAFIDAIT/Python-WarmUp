name = input("Enter your name: ")

try:
    salary_hour = float(input("Enter your hourly salary: "))
    while True :
        if salary_hour < 0:
            salary_hour = float(input("Enter your hourly salary: "))
        else:
            break
except ValueError:
    print("Invalid input for hourly salary. Please enter a numeric value.")
    exit()

try :
    hours_worked = int(input("Enter the number of hours worked : "))
    while True:
        if hours_worked < 0:
            hours_worked = int(input("Enter the number of hours worked : "))
        else:
            break
except ValueError:
    print("Invalid input for hours worked. Please enter an integer value.")
    exit()

if hours_worked > 40:
    salary = (40 * salary_hour) + ((hours_worked - 40) * salary_hour * 1.5)
else:
    salary = hours_worked * salary_hour

print(f"Hello {name}, your salary is {salary} DH.")