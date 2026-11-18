print("-" *60)
print("          Login Password Verification System")
print("-" *60)
correct_password = "python123"
password =(input("ENTER THE PASSWORD HERE:"))
while password != correct_password:
    print("password is incorrect")
    password = (input("ENTER THE PASSWORD AGAIN:"))
print("login successful")
print("-" *60)
print("        welcome to dashboard")
print("-" *60)