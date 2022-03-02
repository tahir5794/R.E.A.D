from getdate import getdate
from logdata import log_data
from retrieve import retrieve_data


while True:
    print("_____________________________Welcome to R.E.A.D_____________________________________")
    print("_____________________________Record.Exercise.And.Diet_____________________________________")
    print("_____________________________Date/Time: ", getdate(), "_________________________________")
    print("Do you want to: \n \t 1. Log Data \n \t 2. Retrieve Data")
    inp = input(">>> ")
    try:
        if int(inp) == 1:
            log_data()
        elif int(inp) == 2:
            retrieve_data()
        else:
            print("Please enter as suggested.")
    except Exception as e:
        print("Please enter the correct input.\n", e)
    inp1 = input("Do you want to log/retrieve data again ?[y/n]: ")
    if inp1 == "y":
        continue
    elif inp1 == "n":
        print("Thank you for using R.E.A.D!")
        break
    else:
        print("Please enter as suggested.")
        continue
