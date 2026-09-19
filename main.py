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
    print("6. Impedance Calculator")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n--- Ohm's Law Calculator ---")

            try:
                voltage = float(input("Enter voltage (V): "))
                resistance = float(input("Enter resistance (Ohm): "))

                if resistance == 0:
                    print("Resistance cannot be zero!")
                else:
                    current = voltage / resistance
                    print("Current =", current, "A")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == 2:
            print("\n--- Power Calculator ---")

            try:
                voltage = float(input("Enter voltage (V): "))
                current = float(input("Enter current (A): "))

                power = voltage * current

                print("Power =", power, "W")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == 3:
            print("\n--- Resistance Calculator ---")

            try:
                voltage = float(input("Enter voltage (V): "))
                current = float(input("Enter current (A): "))

                if current == 0:
                    print("Current cannot be zero!")
                else:
                    resistance = voltage / current
                    print("Resistance =", resistance, "Ohm")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == 4:
            print("\n--- Frequency / Time Period ---")
            print("1. Calculate Time Period")
            print("2. Calculate Frequency")

            try:
                sub_choice = int(input("Enter your choice: "))

                if sub_choice == 1:
                    frequency = float(input("Enter frequency (Hz): "))

                    if frequency == 0:
                        print("Frequency cannot be zero!")
                    else:
                        time_period = 1 / frequency
                        print("Time Period =", time_period, "seconds")

                elif sub_choice == 2:
                    time_period = float(
                        input("Enter time period (seconds): ")
                    )

                    if time_period == 0:
                        print("Time period cannot be zero!")
                    else:
                        frequency = 1 / time_period
                        print("Frequency =", frequency, "Hz")

                else:
                    print("Invalid choice!")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == 5:
            print("\n--- Signal Analyzer ---")

            try:
                peak_voltage = float(
                    input("Enter peak voltage (V): ")
                )

                rms_voltage = peak_voltage / math.sqrt(2)
                peak_to_peak = 2 * peak_voltage

                print("Peak Voltage =", peak_voltage, "V")
                print("RMS Voltage =", rms_voltage, "V")
                print(
                    "Peak-to-Peak Voltage =",
                    peak_to_peak,
                    "V"
                )

            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == 6:
            print("\n--- Impedance Calculator ---")

            try:
                resistance = float(
                    input("Enter resistance (Ohm): ")
                )
                reactance = float(
                    input("Enter reactance (Ohm): ")
                )

                impedance = math.sqrt(
                    resistance ** 2 + reactance ** 2
                )

                print("Impedance =", impedance, "Ohm")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == 7:
            print("\nThank you for using ECE Engineering Toolkit!")
            break

        else:
            print("Invalid choice! Please select 1 to 7.")

    except ValueError:
        print("Invalid input! Please enter a number from 1 to 7.")
