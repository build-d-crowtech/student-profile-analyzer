print("-" * 60)
print("          ATM PIN Verification System")
print("-" * 60)
correct_atm_pin =1234
atm_pin = (int(input("enter the ATM PIN")))
while atm_pin != correct_atm_pin:
    print("incorrect ATM pin")
    atm_pin = (int(input("enter PIN again")))
print("PIN Verified Successfully")