print("-" * 50)
print("         AI HOSPITAL HEALTH CHECKER")
print("-" * 50)
patient_name = input("Enter the Patient Name:")
age = int(input("Enter the Age (year) :"))
temperature = float(input("Enter Body Temperature (°) :"))
oxygen_level = float(input("Enter the Oxygen Level (%) "))
heart_rate = float(input("Enter the heart rate (BPM)"))
if temperature >= 38:
    print("High fever")
else:
    print("Temperature is Normal")
if oxygen_level >= 90:
    print("Patient Stable")
else:
    print("Low Oxygen")
if 100 >= heart_rate >= 60:
    print("Heart Rate is Normal")
else:
    print("heart rate is Not Normal")
