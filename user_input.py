# Assignment 2

first_name, last_name = input("Enter your first and last name: ").split()

if len(first_name) <= 2 or len(last_name) <= 2:
    print("Invalid length. First name and last name must be 2 characters or more.")
else:
    print("Names are valid length.")