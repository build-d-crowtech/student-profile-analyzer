print("-" *40)
print("      Skip Multiples of 3")
print("-" *40)
for i in range(1,30):
    if i % 3 == 0:
        continue
    print(i)
