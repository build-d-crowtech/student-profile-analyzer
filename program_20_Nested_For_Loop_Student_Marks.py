
print("-" * 40)
print("       Student Marks Calculator")
print("-" * 40)

for i in range(1, 4):

    student = input("Enter student name: ")

    total = 0

    for j in range(1, 5):

        subject = input("Enter subject name: ")

        marks = int(input("Enter marks: "))

        total = total + marks

    print("-" * 40)
    print("Student Name:", student)
    print("Total Marks:", total)
    print("-" * 40)

print("All Student Results Completed")
