"""Python KM to MI Converter Module"""


def convert_km_to_mi():
    while True:
        input_km: str = input("Enter Kilometers: ")
        try:
            km: float = float(input_km)
        except ValueError:
            print("Invalid input, please enter a valid kilometers in numeric format.")
            continue
        mi: float = km * 0.621371
        break

    # print(f"{round(km, 2)} kilometers is equal to {round(mi, 2)} miles.")
    print(f"{km:.2f} kilometers is equal to {mi:.2f} miles.")


if __name__ == "__main__":
    convert_km_to_mi()
