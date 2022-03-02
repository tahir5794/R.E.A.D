def retrieve_data():
    print("Clients: \n \t 1. Harry\n \t 2. Rohan\n \t 3. Hammad")
    inp2 = str(input("Enter the name of client >>> "))
    if inp2.isdigit():
        print("Name cannot be a digit! \n Please enter name correctly.")
        retrieve_data()
    else:
        print("Do you want", inp2.__add__("'s"), ": \n 1. Exercise log \n 2. Diet log")
        inp3 = input(">>> ")
        try:
            if int(inp3) == 1:
                file1 = inp2.__add__("Exercise.txt")
                with open(file1, "rt") as f:
                    print(f.read())
            elif int(inp3) == 2:
                file1 = inp2.__add__("Diet.txt")
                with open(file1, "rt") as f:
                    print(f.read())
            else:
                print("Please choose correct option and try again!")
                retrieve_data()
        except Exception as e:
            print("ERROR! UNEXPECTED INPUT.\n PLEASE TRY AGAIN.\n", e)