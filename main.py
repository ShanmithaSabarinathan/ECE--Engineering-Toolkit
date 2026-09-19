print("================================")
print("     ECE ENGINEERING TOOLKIT")
print("================================")

print("1. Ohm's Law")
print("2. Power Calculator")
print("3. Resistance Calculator")
print("4. Frequency / Time Period")
print("5. Signal Analyzer")
print("6. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n--- Ohm's Law Calculator ---")

    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohm): "))

    current = voltage / resistance

    print("Current =", current, "A")

elif choice == 2:
    print("\n--- Power Calculator ---")

    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    power = voltage * current

    print("Power =", power, "W")

else:
    print("This feature will be added soon!")
