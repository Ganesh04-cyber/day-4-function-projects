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