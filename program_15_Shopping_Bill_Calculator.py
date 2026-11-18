print("-" *60)
print("       Shopping Bill Calculator")
print("-" *60)
total = 0
price = (int(input("enter the price: ")))
while 0 != price:
    total = total + price
    price = (int(input("enter the price: ")))
    print("Total Bill:", total)



