from Database import *

class Sellers:

    def view_products(seller_id):
        products = DB.getItemsBySellerId(str(seller_id))
        if len(products) == 0:
            print("You've no products yet\n")
        else:
            for i in products:
                print(i)
        return len(products)
    
    def update_price(seller_id):
        itemsLen = Sellers.view_products(seller_id)
        if itemsLen != 0:
            item_id = str(input("which product would you like to update the price?: "))
            price = str(input("what's the new price: "))
            DB.updateItemPrice(price, item_id)
            print("price updated.")
        

    def add_product(seller_id):
        item_name = str(input("Enter the name's product: "))
        item_date = str(input("Enter the expiry date's product: "))
        item_price = str(input("Enter the price's product: "))

        item = (str(seller_id), item_name, item_date, item_price)

        DB.createItems(item)

    def delete_product(seller_id):
        Sellers.view_products(seller_id)
        item_id = str(input("which product would you like to delete?: "))
        DB.deleteItem(item_id)

    







