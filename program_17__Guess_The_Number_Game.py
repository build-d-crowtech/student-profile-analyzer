print("-" *60)
print("       ATM Transaction Menu")
print("-" *60)
secret_number = 7
while True:
    number = (int(input("guess the number")))
    if number < secret_number:
        print("too low")
    elif number > secret_number:
        print("too high")
    else:
        print("correct guess")
        break
print("-" *40)
print("       game over")
print("-" *40)