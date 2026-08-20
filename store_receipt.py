
name=input("Enter Customer Name: ")
contact=input("Enter Customer Contact Number: ")
address=input("Enter Customer Address: ")

product1=input("Enter Product 1: ")
price1=float(input("Enter Price: "))
quantity1=int(input("Enter Quantity: "))
amount1 = price1 * quantity1

product2=input("Enter Product 2: ")
price2=float(input("Enter Price: "))
quantity2=int(input("Enter Quantity: "))
amount2 = price2 * quantity2

product3=input("Enter Product 3: ")
price3=float(input("Enter Price: "))
quantity3=int(input("Enter Quantity: "))
amount3 = price3 * quantity3

subtotal = amount1 + amount2 + amount3

discount=float(input("Enter Discount (%): "))
discount_amount = subtotal * (discount/100)
total = subtotal - discount_amount

print("======STORE RECEIPT======")
print(("Name: "), name)
print(("Contact: "), contact)
print(("Address: "), address)
print("------------------------")
print("PROD PRC QTY AMT")
print(product1, price1, quantity1, amount1)
print(product2, price2, quantity2, amount2)
print(product3, price3, quantity3, amount3)
print("------------------------")
print(("SUBTOTAL:"), subtotal)
print(("DISCOUNT:"), discount)
print("------------------------")
print(("TOTAL:"), total)
print("=========================")
print("THANK YOU FOR YOUR PURCHASE!")











