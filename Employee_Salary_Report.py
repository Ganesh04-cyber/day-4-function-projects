# Smart Billing System - Calculates total with GST and discount

def Smart_Billing_System(name, qty, price):
    total = qty * price
    gst = total * 0.05  # 5% GST
    if total >= 1000 :
        discount = total * 0.10 
        final=total+gst-discount
    else:
        0  # 10% discount if eligible
    return total, gst, discount, final

# List of purchased items
items = [
    ("Laptop Bag", 2, 750),
    ("Wireless Mouse", 3, 400),
    ("Notebook", 5, 100),
    ("Pen Drive", 1, 900)
]

# Print individual bill summary
for name, qty, price in items:
    total, gst, discount, final = Smart_Billing_System(name, qty, price)
    print(f"\nItem: {name}")
    print(f"Total: ₹{total}")
    print(f"GST (5%): ₹{gst}")
    print(f"Discount: ₹{discount}")
    print(f"Final Amount: ₹{final}")

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
