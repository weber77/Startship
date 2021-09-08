from Database import *
from logic import *
 
        

if __name__ == "__main__":
    # Initialise Database with tables
    
    '''
        Uncomment line 12 and 13 if you're running the program for the first time
    '''
    # DB.initDB()
    # DB.initInsert()

    print("Welcome to the Online Store, Please select an option.")
   
    while True:
        userchoice = input("1. Login\n2. Register\nT. Terminate program\n-> ")
        if(userchoice == "1"):
            login()
        elif(userchoice == "2"):
            register()
        elif userchoice == "T":
            print("Thanks for testing😊")
            exit()
        else:
            print("Invalid option!")
