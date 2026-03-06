# Jacob Whittington
# jaw0731
# CSCE 4350 - Database Assignment

# dictionary for storage
store = {}

# loops until broken
while True:
    user_input = input().strip()    # accepts user input

    if not user_input:  # ensures input is not null
        print("ERROR")
        continue

    parts = user_input.split()  # turns the string into separate parts

    command = parts[0].upper()  # makes command upper case

    if command == "EXIT":   # terminates loop
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
            store[key] = value  # stores the value in the dictionary
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