from getdate import getdate

def log_data():
    print("For which client you want to log data: \n \t 1. Harry\n \t 2. Rohan\n \t 3. Hammad")
    inp2 = str(input("Enter the name of client >>> "))
    if inp2.isdigit():
        print("Name cannot be a digit! \n Please enter name correctly.")
        log_data()
    else:
        print("What do you want to log:\n\t 1.Exercise\n\t 2. Diet")
        inp3 = input(">>> ")
        try:
            if int(inp3) == 1:
                file1 = inp2.__add__("Exercise.txt")
                with open(file1, "a") as f:
                    f.write("[ ")
                    f.write(str(getdate()))
                    f.write(" ]: ")
                    f.write(input("Enter the updates: "))
                    f.write("\n")
                print(inp2.__add__("'s"), "Exercise log has been updated successfully.")
            elif int(inp3) == 2:
                file1 = inp2.__add__("Diet.txt")
                with open(file1, "a") as f:
                    f.write("[ ")
                    f.write(str(getdate()))
                    f.write(" ]: ")
                    f.write(input("Enter the updates: "))
                    f.write("\n")
                print(inp2.__add__("'s"), "'s Diet log has been updated successfully.")
            else:
                print("Please choose correct option and try again!")
                log_data()
        except Exception as e:
            print("ERROR! UNEXPECTED INPUT.\n PLEASE TRY AGAIN.\n", e)