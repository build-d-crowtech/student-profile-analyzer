print("-" *60)
print("       ATM Transaction Menu")
print("-" *60)
while True:
   print("1, check balence"  )
   print("2, withdrwal money" )
   print("3, exit" )
   choice = (int(input("enter the choice given in your screen" )))
   if choice == 1:
        print("balence:10000")
   elif choice == 2:
        print("withdrwal selected")
   elif choice == 3:
        break
   else:
    print("invaid choice")
print("-" *60)
print("      Thank You for Using ATM")
print("-" *60)


