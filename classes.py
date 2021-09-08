from Database import *

class User:
    def __init__(self, name, user_id, password, login_status, register_date, email):
        self.user_id = user_id
        self.password = password
        self.login_status = login_status
        self.register_date = register_date
        self.email = email
        self.name = name

    def verifyLogin(login):
        """
            check if user is logged in
            precondition: we assume user is logged out
            postcondition: returns true if user credentials are correct, false otherwise
        """
        if(login.role == "admin"):
            # print("I'm here!")
            user = DB.getAdminByName(login)
            
            if( user != None and user[2] == login.password):
                print(f"{login.username} with id: {user[0]} is connected to the system ")
                return user[0]
                
            
            print(f"{login.username} is not connected to the system")
            return False

        elif(login.role == "seller"):
            user = DB.getSellerByName(login)
            if( user != None and user[2] == login.password):
                print(f"{login.username} is connected to the system")
                return user[0]
            else:
                print(f"{login.username} is not connected to the system")

        elif(login.role == "customer"):
            user = DB.getCustomerByName(login)
            if( user != None and user[2] == login.password):
                print(f"{login.username} is connected to the system")
                return user[0]
            else:
                print(f"{login.username} is not connected to the system")
        
        return False

    def signUp(signupModel):
        if(signupModel[6]== "admin"):
            user = DB.addAdmin(signupModel)
            print(signupModel[0] + " signed up as admin!")
            return True
        if(signupModel[6] == "seller"):
            user = DB.addSeller(signupModel)
            print(signupModel[0] + " signed up as seller!")
            return True
        if(signupModel[6] == "customer"):
            user = DB.addCustomer(signupModel)
            print(signupModel[0] + " signed up  as customer!")
            return True
        
        return False
   

    def updateProfile():
        """
            update user profile
            precondition: must authenticate
            postcondition: return true if profile updated, otherwise return error message.
        """
        pass
        

class SystemAdmin(User):
    def __init__(self, name, user_id, password, login_status, register_date, email):
        super().__init__(user_id, name, password, login_status, register_date, email)

    """
        effect general changes on the online store
        precondition: we assume user is logged out.
        postcondition: returns true if user credentials are correct.
    """
    # def manageOnlineShop():
    #     pass

    def addNewSeller():
        """
            add new seller to store
            precondition: 
                -   must authenticate as administrator.
                -   the seller your adding shouldn't already exist.
            postcondition: 
                -   add seller if he doesn't exist.
                -   return seller's details.
        """
        pass

    def suspendSeller(admin, sellerId):
        if(admin.login_status):
            DB.suspendSeller(sellerId)
        """
           suspend seller from store
           precondition: 
               -   must authenticate as administrator.
               -   seller most exist and be active.
           postcondition: 
               -   suspend seller.
               -   return true if suspended, false otherwise.
       """
        pass

    def deleteSellersItem():
        """
        delete seller from store
        precondition: 
            -   must authenticate as administrator.
        postcondition: 
            -   suspend deleted.
            -   return true if item deleted, false otherwise.
        """
        pass

    def deleteSeller():
        """
        delete seller from store
        precondition: 
            -   must authenticate as administrator.
        postcondition: 
            -   suspend deleted.
            -   return true if deleted, false otherwise.
        """
        pass

class Seller(User):
    def __init__(self, name, user_id, password, login_status, register_date, email):
        super().__init__(name, user_id, password, login_status, register_date, email)

    def addItem():
        """
            add item to Seller inventory
            precondition: 
                -   must authenticate as Seller.
            postcondition: 
                -   return true if item added, false otherwise.
        """
        pass

    def deleteItem():
        """
        delete item to Seller inventory
        precondition: 
            -   must authenticate as Seller.
        postcondition: 
            -   return true if item deleted, false otherwise.
        """
        pass

    def updateItem():
        """
            update item to Seller inventory
            precondition: 
                -   must authenticate as Seller.
            postcondition: 
                -   return true if item updated, false otherwise.
        """
        pass

    # Implement when GUI is ready
    def modifyBanner():
        pass

class Customer(User):
    def __init__(self, name, user_id, password, login_status, register_date, email, address, creditcard_info):
        super().__init__(name, user_id, password, login_status, register_date, email)
        self.address = address
        self.creditcard_info = creditcard_info

    def register():
        """
            register onto the online store
            precondition: customer email must be unique
            postcondition: returns true if customer is created, otherwise error message.
        """
        pass

    def login():
        """
            login onto the online store
            precondition: 
                - have an existing account.
                - enter correct correct credentials
            postcondition: returns true if credentials are valid, false otherwise.
        """
        pass

class Item:
    def __init__(self, item_id, seller_id, name, expiry_date, cost):
        self.item_id = item_id
        self.seller_id = seller_id
        self.name = name
        self.expiry_date = expiry_date
        self.cost = cost

class ShoppingCart:
    def __init__(self, cart_id, product_ids, date_added, customer_id, total_cost):
        self.cart_id = cart_id
        self.product_ids = product_ids
        self.date_added = date_added
        self.customer_id = customer_id
        self.total_cost = total_cost

    def addCartItem():
        """
            add an item to the cart
            precondition: customer email must be unique
            postcondition: returns true if customer is created, otherwise error message.
        """
        pass

    def updateItemQuantity():
        pass

    def viewCartDetails():
        pass

    def checkOut():
        pass

class Order:
    def __init__(self, order_id, date_shipped, status, date_created, ShoppingCartId):
        self.order_id = order_id
        self.date_shipped = date_shipped
        self.status = status
        self.date_created = date_created
        self.ShoppingCartId = ShoppingCartId

    def placeOrder():
        """
        place an order
        precondition: customer must have created an order with items in the shopping cart
        postcondition: order validated and proceed to shipping details
        """
        pass

class Payment:
    def __init__(self, id, order_id, payment_method, total_cost):
        self.id = id
        self.order_id = order_id
        self.payment_method = payment_method
        self.total_cost = total_cost

    def processPayment():
        """
        proceed the payment
        precondition: the customer selects a valid payment method
        postcondition: if the payment is successful or not he will receive the appropriate message
        """

    # def selectPaymentMethod():
    #     """
    #     select the payment
    #     precondition: Payment method must exist
    #     postcondition: Payment method is selected
    #     """

class BankCard:
    def __init__(self, account_id, user_id, accountNumber, balance, expiry_date):
        self.account_id = account_id
        self.user_id = user_id
        self.accountNumber = accountNumber
        self.balance = balance
        self.expiry_date = expiry_date

    def dataCheck():
        """
        validate account details
        precondition: 
            - user input valid account details
            - send and withdraw 2$ into the account
        postcondition:
            - succesful initial transactions
        """
        pass

    def validityCheck():
        """
        verify account has enough funds before payment
        precondition: 
            - check if account not expired
        postcondition:
            - return true if account not expired, false otherwise.
        """
        pass

class Shipping:
    def __init__(self, shippingId, order_id, shippingType, shippingCost, shippingAddress):
        self.shippingId = shippingId
        self.order_id = order_id
        self.shippingType = shippingType
        self.shippingCost = shippingCost
        self.shippingAddress = shippingAddress

    def updateShippingInfo():
        """
        update shipping info
        precondition: 
            -   must authenticate.
        postcondition: 
            -   return true if shipping updated, false otherwise.
        """
        pass


