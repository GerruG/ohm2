def calculate_ohms_law(v, i, r, p):
    try:
        v = float(v) if v != '' else None
        i = float(i) if i != '' else None
        r = float(r) if r != '' else None
        p = float(p) if p != '' else None

        if v is not None and i is not None:
            calculated_r = v / i
            calculated_p = v * i
            print(f"Resistance (R): {calculated_r:.3f} Ohms")
            print(f"Power (P): {calculated_p:.3f} Watts")
        elif v is not None and r is not None:
            calculated_i = v / r
            calculated_p = v * calculated_i
            print(f"Current (I): {calculated_i:.3f} Amperes")
            print(f"Power (P): {calculated_p:.3f} Watts")
        elif i is not None and r is not None:
            calculated_v = i * r
            calculated_p = i * calculated_v
            print(f"Voltage (V): {calculated_v:.3f} Volts")
            print(f"Power (P): {calculated_p:.3f} Watts")
        elif v is not None and p is not None:
            calculated_i = p / v
            calculated_r = v / calculated_i
            print(f"Current (I): {calculated_i:.3f} Amperes")
            print(f"Resistance (R): {calculated_r:.3f} Ohms")
        elif i is not None and p is not None:
            calculated_v = p / i
            calculated_r = calculated_v / i
            print(f"Voltage (V): {calculated_v:.3f} Volts")
            print(f"Resistance (R): {calculated_r:.3f} Ohms")
        elif r is not None and p is not None:
            calculated_i = (p / r) ** 0.5
            calculated_v = calculated_i * r
            print(f"Voltage (V): {calculated_v:.3f} Volts")
            print(f"Current (I): {calculated_i:.3f} Amperes")
        else:
            print("Error: Please enter at least two values.")
    except ValueError:
        print("Error: Please enter valid numbers.")

def main():
    while True:
        print("\nOhm's Law Calculator")
        print("Enter the known values and leave the unknowns blank. Type 'exit' to quit.")

        v = input("Enter Voltage (V) or leave blank: ")
        if v.lower() == 'exit':
            break
        i = input("Enter Current (I) or leave blank: ")
        if i.lower() == 'exit':
            break
        r = input("Enter Resistance (R) or leave blank: ")
        if r.lower() == 'exit':
            break
        p = input("Enter Power (P) or leave blank: ")
        if p.lower() == 'exit':
            break

        calculate_ohms_law(v, i, r, p)

if __name__ == "__main__":
    main()
