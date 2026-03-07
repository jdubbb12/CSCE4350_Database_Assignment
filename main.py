# Jacob Whittington
# jaw0731
# CSCE 4350 - Database Assignment

import os

DATA_FILE = "data.db"
# list for storage
store = []

# function for setting value in the list
def set_value(key, value):
    for pair in store:
        if pair[0] == key:
            pair[1] = value
            return
    store.append([key, value])

# function for getting the value from the list
def get_value(key):
    for pair in store:
        if key == pair[0]:
            return pair[1]
        
    return None

# function to open the data.db file
def load_data():
    if not os.path.exists(DATA_FILE): # makes sure the path exists
        return
    
    with open(DATA_FILE, "r") as file:  # opens the file using os
        for line in file:
            line = line.rstrip("\n")

            if not line:
                continue

            parts = line.split(" ", 2)

            if len(parts) < 3:
                continue

            command = parts[0]

            if command == "SET":
                key = parts[1]     # makes key the 2nd element
                value = parts[2]   # makes value the 3rd element
                set_value(key,value)

# function to append to the data.db file
def append_to_file(key, value):
    with open(DATA_FILE, "a") as file:  # opens file in append mode
        file.write(f"SET {key} {value}\n")
        file.flush()    
        os.fsync(file.fileno())    # forces the write immediately


# main function
def main():

    load_data()     # loads the data.db file

    # loops until broken
    while True:
        try:
            user_input = input()   # accepts user input
            user_input = user_input.rstrip("\n")
        except EOFError:
            break

        if not user_input:  # ensures input is not null
            print("", flush=True)
            continue

        parts = user_input.split(" ", 2)  # turns the string into separate parts

        command = parts[0].upper()  # puts set, get, exit in command upper case

        if command == "EXIT":   # terminates loop
            if len(parts) == 1:
                break
            else:
                print("", flush=True)

        elif command == "SET":
            if len(parts) < 3:
                print("", flush=True)
            else:
                key = parts[1]
                value = parts[2]  # allows values with spaces
                append_to_file(key, value)   # stores data to the data file
                set_value(key, value)  # stores the value in the list
                print("",flush=True)

        elif command == "GET":
            if len(parts) != 2:
                print("", flush=True)
            else:
                key = parts[1]
                value = get_value(key)

                if value is not None:
                    print(value, flush=True)
                else:
                    print("", flush=True)

        else:
            print("ERROR", flush=True)

if __name__ == "__main__":
    main()