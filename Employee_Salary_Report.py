# Employee Salary Report - Calculates final salary and generates summary

def Employee_Salary_Report(emp_name, base_salary, bonus, deduction):
    final_salary = base_salary + bonus - deduction
    return emp_name, base_salary, bonus, deduction, final_salary

# List of employees
employees = [
    ("Ganesh", 50000, 7000, 3000),
    ("Riya", 62000, 5000, 4000),
    ("Aman", 45000, 4500, 2000),
    ("Sneha", 55000, 6000, 3500)
]

salaries = []

# Generate report for each employee
for name, base, bonus, deduct in employees:
    n, b, bo, d, final = Employee_Salary_Report(name, base, bonus, deduct)
    print(f"\nName: {n}")
    print(f"Base Salary: ₹{b}")
    print(f"Bonus: ₹{bo}")
    print(f"Deduction: ₹{d}")
    print(f"Final Salary: ₹{final}")
    salaries.append(final)

# Print summary of salaries
print("\n--- Salary Summary ---")
print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))
print("Average Salary:", round(sum(salaries)/len(salaries), 2))

   #code example
def  Employee_Salary_Report(emp_name,base_salary,bonus,deduction):
    final_salary=base_salary+bonus-deduction
    return emp_name,base_salary,bonus,deduction,final_salary
employees = [
    ("Ganesh", 50000, 7000, 3000),
    ("Riya", 62000, 5000, 4000),
    ("Aman", 45000, 4500, 2000),
    ("Sneha", 55000, 6000, 3500)
]
salaries=[]
for name,salary,bonus,deduct in employees:
    n,b,bo,d,final=Employee_Salary_Report(name,salary,bonus,deduct)
    print(f"\name:{n} | base salary:{b} | bonus:{bo} | deduction:{d} |final salary:{final} ")
    salaries.append(final)
print("\n--- Summary Report ---")
print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))
print("Average Salary:", round(sum(salaries)/len(salaries), 2))
