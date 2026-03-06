# Jacob Whittington
# jaw0731
# CSCE 4350 - Database Assignment

import os

DATA_FILE = "data.db"
# dictionary for storage
store = {}

# function to open the data.db file
def load_data():
    if not os.path.exists(DATA_FILE):
        return
    
    with open(DATA_FILE, "r") as file:  # opens the file using os
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) < 3:
                continue

            command = parts[0]

            if command == "SET":
                key = parts[1]
                value = " ".join(parts[2:])   # makes value the 3rd element and everything after
                store[key] = value

# function to append to the data.db file
def append_to_file(key, value):
    with open(DATA_FILE, "a") as file:  # opens file in append mode
        file.write(f"SET {key} {value}\n")
        file.flush()    
        os.fsync(file.fileno())    # forces the write immediately

def main():

    load_data()     # loads the data.db file

    # loops until broken
    while True:
        try:
            user_input = input().strip()    # accepts user input
        except EOFError:
            break

        if not user_input:  # ensures input is not null
            print("ERROR")
            continue

        parts = user_input.split()  # turns the string into separate parts

        command = parts[0].upper()  # puts set, get, exit in command upper case

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
                append_to_file(key, value)   # stores data to the data file
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

if __name__ == "__main__":
    main()