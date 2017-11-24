name = 'Zed A. Shaw'
age = 35
height_in_inches = 74
height_in_cents  = round(height_in_inches * 2.54,1)
weight_in_pounds = 180
weight_in_kilos = round(weight_in_pounds * 0.45359237,1)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_inches} iches tall.")
print(f"He's {height_in_cents} centimeters tall.")
print(f"He's {weight_in_pounds} pounds heavy.")
print(f"He's {weight_in_kilos} kilograms heavy.")
print("Actually it's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth is usually {teeth} depending on the coffee.")

total = age + height_in_inches + weight_in_pounds
print(f"If I add {age}, {height_in_inches}, and {weight_in_pounds} I get {total}.")

#str.51 dokończyć