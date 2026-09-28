while True:
    count = 0
    while True and count <= 3:
        count += 1
        age = (input("Enter age: "))
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Input Valid Numebers only!")
        
    has_license = input("Do you have a driver's license? (Yes/No): ").strip().lower()
    has_license = True if has_license == "yes" else False if has_license == "no" else None

    
    if has_license and age >= 18:
        print(f"You are eligible to drive because you are.\n{age} years old and have a license")
        break
    elif has_license == False:
        print("You don't have a license")
        break
    else:
        print("Please input correct value (Yes/No).\n\n")