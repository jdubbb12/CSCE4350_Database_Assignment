# Jacob Whittington
# jaw0731
# CSCE 4350 - Database Assignment

# dictionary for storage
store = {}

while True:
    user_input = input().strip()

    if not user_input:
        print("ERROR")
        continue

    parts = user_input.split()

    command = parts[0].upper()

    if command == "EXIT":
        if len(parts) == 1:
            break
        else:
            print("ERROR")

    elif command == "SET":
        if len(parts) < 3:
            print("ERROR")
        else:
            key = parts[1]
            value = " ".join(parts[2:])  # allows values with spaces
            store[key] = value
            print("OK")

    elif command == "GET":
        if len(parts) != 2:
            print("ERROR")
        else:
            key = parts[1]
            if key in store:
                print(store[key])
            else:
                print("NOT FOUND")

    else:
        print("ERROR")