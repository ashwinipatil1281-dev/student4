import sys

default_salary = 30000.0

if len(sys.argv) == 2:
    salary = float(sys.argv[1])
    source = "User Input"
else:
    salary = default_salary
    source = "Self-assigned"

bonus = salary * 0.10
total_salary = salary + bonus

print(f"Salary: {salary} ({source})")
print("Bonus Amount:", bonus)
print("Total Salary after Bonus:", total_salary)
