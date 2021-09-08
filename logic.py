from models import *
from Database import *
from classes import *
from shopping import *
from administration import *
from sellers import *
from main import *

def login():

    username = input("Enter your username: ")
    password = input("Enter passsword: ")
    role = input("Options: admin -- seller -- customer\n-> ")
    login_details = loginModel(username, password, role)

    response = User.verifyLogin(login_details)
    if response != False:
        # Action
        print("Successful Login.\n")
        while True:
            if role == "customer":
                userchoice = input("1.list items\n2. Add item to cart\n3. checkout\n\n0. to logout!\nT. Terminate program\n")
                
                if(userchoice == "1"):
                    shop.listItem()
                elif (userchoice == "2"):
                    shop.addItemToCart(response)
                elif (userchoice == "3"):
                    shop.checkOut(str(response))
                elif (userchoice == "0"):
                    return
                elif userchoice == "T":
                    print("Thanks for testing😊")
                    exit()
                else:
                    print("Invalid option!")
            elif role == "admin":
                userchoice = input("1.view sellers\n2. Add seller\n3. block seller\n4. unblock seller\n5. delete seller\n\n0. to logout!\nT. Terminate program\n")
                
                if(userchoice == "1"):
                    admins.view_sellers()
                elif (userchoice == "2"):
                    admins.add_seller()
                elif (userchoice == "3"):
                    admins.block_seller()
                elif (userchoice == "4"):
                    admins.unblock_seller()
                elif (userchoice == "5"):
                    admins.delete_seller()
                elif (userchoice == "0"):
                    return
                elif userchoice == "T":
                    print("Thanks for testing😊")
                    exit()
                else:
                    print("Invalid option!")
            elif role == "seller":
                userchoice = input("1. View your products\n2. Update price\n3. Add product\n4. Delete product\n\n0. to logout!\nT. Terminate program\n")
                
                if(userchoice == "1"):
                    Sellers.view_products(response)
                elif (userchoice == "2"):
                    Sellers.update_price(response)
                elif (userchoice == "3"):
                    Sellers.add_product(response)
                elif (userchoice == "4"):
                    Sellers.delete_product(response)
                elif (userchoice == "0"):
                    return
                elif userchoice == "T":
                    print("Thanks for testing😊")
                    exit()
                else:
                    print("Invalid option!")

            


    else:
        print("Incorrect user details try again\n")
        try_again = input("Will you like to try again? y/n: ")
        if try_again == "y":
            login()   # Recursion
        else:
            return

def register():

    username = input("Enter your username: ")
    password = input("Enter a new password: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")
    role = input("Options: admin -- seller -- customer\n-> ")

    register = (username, password, 0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), email, address, role)
    
    User.signUp(register)


