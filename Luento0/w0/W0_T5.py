total = 0.0

while True:
    print(f"Current value {total}")
    value = input("Add number(empty stops): ")

    if value == "":
        break

    total += float(value)

print(f"Final value {total}")
