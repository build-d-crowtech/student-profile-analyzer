print("-" * 60)
print("       ATM Withdrawal Eligibility Checker")
print("-" * 60)
account_balence = (float(input("enter the account balence: ")))
withdrawl_amount =(int(input("enter the withdrawl amount")))
if account_balence >= 500:
    print("withdrawl amount: " ,withdrawl_amount)
    if withdrawl_amount <= account_balence:
        print("withdrawl successful")
    else:
        print("insufficent balence")
else:
    print("minimum balance requirement not met")

print("atm transaction complete")
