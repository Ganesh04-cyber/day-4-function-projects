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
def Smart_Billing_System(name,qty,price):
    total=qty*price
    gst=total*0.05
    if total>=1000:
        discount=total*0.10
        final_amount=total+gst-discount
    else:
        discount=0
        final_amount=total+gst
    return name,total,gst,discount,final_amount
items = [
    ("Laptop Bag", 2, 750),
    ("Wireless Mouse", 3, 400),
    ("Notebook", 5, 100),
    ("Pen Drive", 1, 900)
]
for name,qty,price in items:
    n,t,g,d,f=Smart_Billing_System(name,qty,price)
    print(f"\name:{n} | total={t} | gst={g} | discount={d} | final amount={f}")
