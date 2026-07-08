print("-" * 50)
print("       ASTRONAUT MISSION READINESS CHECKER")
print("-" * 50)
astronaut_name = input("Enter the Astronaut Name: ")
age = int(input("Enter the Age (years): "))
height = float(input("Enter the Height (cm): "))
weight = float(input("enter the Weight (kg): "))
oxygen_level = float(input("Enter the Oxygen Level (%): "))
eyesight_score = float(input("Enter the Eyesight in under (1-10)"))
heart_rate = float(input("Enter the Heart Rate (BPM):"))
experience_year = float(input("Enter the Experience Year: "))
training_score = int(input("Enter the Training Score"))
age_check = age >= 21 and age <= 26
height_check = height >= 170 and height <= 190
weight_check = weight >= 50 and weight <= 80
oxygen_check = oxygen_level >= 70 and oxygen_level <= 90
eyesight_check = eyesight_score >= 8 and eyesight_score <= 10
heart_rate_check = heart_rate >= 60 and heart_rate <= 100
experience_year_check = experience_year >= 5
condition_requirement = experience_year >= 5 or training_score >= 90
blacklisted = False
print("-" * 50)
print("          MISSION READINESS REPORT")
print("-" * 50)
print("Astronaut Name :", astronaut_name)
print("Age :", age)
print("Height :", height)
print("Weight :", weight)
print("Oxygen Level :", oxygen_level)
print("Eyesight Score :", eyesight_score)
print("Heart Rate :", heart_rate)
print("Experience Year :", experience_year)
print("Training Score :", training_score)
#Check Results
print("Age Check :", age_check)
print("Height Check :", height_check)
print("Weight Check :", weight_check)
print("Oxygen Check :", oxygen_check)
print("Eyesight Check :", eyesight_check)
print("Heart Rate Check :", heart_rate_check)
print("Experience Check :", experience_year_check)
#Logical Operators Result
print("Condition Requirement :", condition_requirement)
#for not
print("Blacklisted :", blacklisted)
print("Astronaut Allowed :", not blacklisted)
