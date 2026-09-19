import math

while True:
    print("\n================================")
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

    elif choice == 3:
        print("\n--- Resistance Calculator ---")

        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))

        resistance = voltage / current

        print("Resistance =", resistance, "Ohm")

    elif choice == 4:
        print("\n--- Frequency / Time Period ---")
        print("1. Calculate Time Period")
        print("2. Calculate Frequency")

        sub_choice = int(input("Enter your choice: "))

        if sub_choice == 1:
            frequency = float(input("Enter frequency (Hz): "))

            time_period = 1 / frequency

            print("Time Period =", time_period, "seconds")

        elif sub_choice == 2:
            time_period = float(input("Enter time period (seconds): "))

            frequency = 1 / time_period

            print("Frequency =", frequency, "Hz")

        else:
            print("Invalid choice!")

    elif choice == 5:
        print("\n--- Signal Analyzer ---")

        peak_voltage = float(input("Enter peak voltage (V): "))

        rms_voltage = peak_voltage / math.sqrt(2)

        print("RMS Voltage =", rms_voltage, "V")

    elif choice == 6:
        print("\nThank you for using ECE Engineering Toolkit!")
        break

    else:
        print("Invalid choice! Please try again.")
