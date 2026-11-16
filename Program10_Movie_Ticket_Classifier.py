print("-" * 40)
print("       Movie Ticket Classifier")
print("-" * 40)
customer_name = input("enter the name of customer: ")
age = (int(input("enter the age: ")))
print("customer_name: " , customer_name)
print("age: " , age)
print("ticket category: ")
if age <= 5:
    print("FREE TICKET")
elif age <= 17:
    print("CHILD TICKET")
elif age <= 59:
    print("ADULT TICKET")
else:
    print("SENIOR CITIZEN CLASS")
print("Ticket Classification completed")




