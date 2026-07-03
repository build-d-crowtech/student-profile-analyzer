print("-" * 60)
print("          PLANET HABITABILITY SCORE CALCULATOR")
print("-" * 60)
planet_name = input("Enter the Planet Name:")
oxygen_percentage = float(input("Enter the Oxygen Percentage"))
water_percentage = float(input("Enter the water percentage"))
gravity = float(input("Enter the Gravity"))
average_temperature = float(input("Enter the Average Temperature"))
atmospheric_pressure = float(input("Enter Atmoshpheric Pressure "))
total_resources = oxygen_percentage + water_percentage
resource_difference = water_percentage - oxygen_percentage
double_gravity = gravity * 2
earth_temperature = float(input("Enter Earth's Average Temperature: "))
temperature_difference = average_temperature - earth_temperature
half_pressure = atmospheric_pressure / 2
gravity_square_8 = gravity ** 8
resource_blocks = total_resources // 10
remaining_resources = total_resources % 10
print("-" * 40)
print("          PLANET REPORT")
print("-" * 40)
print("Planet Name:", planet_name)
print("Total Resources:", total_resources)
print("Resource Difference:", resource_difference)
print("Double Gravity:", double_gravity)
print("Temperature Difference:", temperature_difference)
print("Half Pressure:", half_pressure)
print("Gravity Power 8:", gravity_square_8)
print("Resource Blocks:", resource_blocks)
print("Remaining Resources:", remaining_resources)
