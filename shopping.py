from  Database import *

class shop:
    def listItem():
        items = DB.getItems()
        for i in items:
            print(i)
        print("\n")

    def addItemToCart(user_id):
        # create a cart that for that user
        # call addItemToCart from DB and passin the item id and the cart id
        shop.listItem()
        userchoice = input("choose Item by id: ")

        userCart = DB.checkOpenCart(user_id)

        if userCart == None:
            cart = (str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), user_id, 0, 0)
            DB.createCart(cart, userchoice)

            # DB.addCartItems(cart_id, userchoice)
        else:
            DB.addCartItems(str(userCart[0]), userchoice)


    # def removeItem():

    def checkOut(user_id):
        cart = DB.checkOpenCart(user_id)
        # print(cart_id)

        if cart == None:
            print("Cart is empty\n")
            return

        items = DB.getCartItemsByCartId(str(cart[0]))
        print("Items in your cart are :")
        for i in items:
            print(i)
        print("Total cost: ", end="")
        print(DB.getCartCost(cart[0]))
        print("\n")


        userchoice = input("Will you like to checkout? y/n: ")
        if userchoice == "y":
            DB.checkOut(str(cart[0]))