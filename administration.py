from Database import *

class admins:

    def view_sellers():
        sellers = DB.getSellers()
        for i in sellers:
            print(i)
    
    def add_seller():
        username = input("Enter your username: ")
        password = input("Enter a new password: ")
        email = input("Enter your email address: ")

        seller = (username, password, 1, 0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), email)
        
        DB.addSeller(seller)
    
    def block_seller():
        admins.view_sellers()
        seller_id = str(input("which seller will you like to block: "))
        DB.block_seller(seller_id)

    def unblock_seller():
        admins.view_sellers()
        seller_id = str(input("which seller will you like to block: "))
        DB.unblock_seller(seller_id)

    def delete_seller():
        admins.view_sellers()
        seller_id = str(input("which seller will you like to delete: "))
        DB.deleteSeller(seller_id)
    
