name = input("Enter your name: ")
salary_hour = float(input("Enter your hourly salary: "))
hours_worked = int(input("Enter the number of hours worked : "))

if hours_worked > 40:
    salary = (40 * salary_hour) + ((hours_worked - 40) * salary_hour * 1.5)
else:
    salary = hours_worked * salary_hour

print(f"Hello {name}, your salary is {salary} DH.")