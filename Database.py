from os import remove
import mysql.connector
from datetime import date, datetime


#establishing the connection
conn = mysql.connector.connect(user='Julia', password='password',
                               host='localhost', #localhost 127.0.0.1
                               database='shoppingOnline')

#Creating a cursor object using the cursor() method 
cursor = conn.cursor()

class DB:
    """
    Initialize the classes in database
    precondition: shoppingOnline should be created
    postcondition: tables created
    """
    def initDB():
        
        cursor.execute('''CREATE TABLE customers (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255), 
                            password VARCHAR(255),
                            login_status BOOLEAN,
                            register_date VARCHAR(255),
                            email VARCHAR(255),
                            address VARCHAR(255)
                            )''')

        cursor.execute('''CREATE TABLE systemAdmins (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255), 
                            password VARCHAR(255),
                            login_status BOOLEAN,
                            register_date VARCHAR(255),
                            email VARCHAR(255)
                            )''')

        cursor.execute('''CREATE TABLE Sellers (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255), 
                            password VARCHAR(255),
                            isActive BOOLEAN,
                            login_status BOOLEAN,
                            register_date VARCHAR(255),
                            email VARCHAR(255)
                            )''')

        cursor.execute('''CREATE TABLE items (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            seller_id INTEGER,
                            name VARCHAR(255), 
                            expiry_date VARCHAR(255),
                            cost DOUBLE,
                            FOREIGN KEY(seller_id) REFERENCES sellers(id)
                            )''')
        
        cursor.execute('''CREATE TABLE shoppingCarts (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            date_added VARCHAR(255),
                            customer_id INTEGER,
                            total_cost INTEGER,
                            closed boolean,
                            FOREIGN KEY(customer_id) REFERENCES customers(id)
                            )''')

        cursor.execute('''CREATE TABLE orders (
                            id INT AUTO_INCREMENT PRIMARY KEY, 
                            date_shipped VARCHAR(255),
                            status BOOLEAN,
                            date_created VARCHAR(255),
                            shoppingCart_id INTEGER,
                            FOREIGN KEY(shoppingCart_id) REFERENCES shoppingCarts(id)
                            )''')
        
        cursor.execute('''CREATE TABLE itemInCarts (
                            cart_id INTEGER ,
                            item_id INTEGER,
                            FOREIGN KEY(cart_id) REFERENCES shoppingCarts(id),
                            FOREIGN KEY(item_id) REFERENCES items(id)
                            )''')

        cursor.execute('''CREATE TABLE PaymentMethods (
                            id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            description VARCHAR(255)
                            )''')
                            
        cursor.execute('''CREATE TABLE Payments (
                            id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            order_id INTEGER,
                            payment_method_id INTEGER,
                            total_cost DOUBLE,
                            FOREIGN KEY(order_id) REFERENCES orders(id),
                            FOREIGN KEY(payment_method_id) REFERENCES paymentMethods(id)
                            )''')

        cursor.execute('''CREATE TABLE Shippings (
                            id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            shippingType VARCHAR(255),
                            cost DOUBLE,
                            shippingAddress VARCHAR(255),
                            order_id INTEGER,
                            FOREIGN KEY(order_id) REFERENCES orders(id)
                            )''')
        
        cursor.execute('''CREATE TABLE BankCards (
                            id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            customer_id INTEGER,
                            account_number INTEGER,
                            balance DOUBLE,
                            expiry_date VARCHAR(255),
                            FOREIGN KEY(customer_id) REFERENCES customers(id)
                            )''')

    def initInsert():
        # set default customers
        sqlc = "INSERT INTO customers \
                (name, password, login_status, register_date, email, address) \
                VALUES \
                (%s, %s, %s, %s, %s, %s)"
        customers = [
            ('Peter', "12345", 0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Amy', 'Apple st 652', 0,str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'a@w.com', 'Cowstreet 4'),
            ('Hannah', 'Mountain 21',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'hanna@w.com', 'bigstreet 4'),
            ('Michael', 'Valley 345',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'mich@w.com', 'Carystreet 4'),
            ('Sandy', 'Ocean blvd 2',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Betty', 'Green Grass 1',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Richard', 'Sky st 331',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Susan', 'One way 98', 0,str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Vicky', 'Yellow Garden 2',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Ben', 'Park Lane 38',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('William', 'Central st 954',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Chuck', 'Main Road 989',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4'),
            ('Viola', 'Sideway 1633',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'p@w.com', 'Lowstreet 4')
            ]

        for i in customers:
            cursor.execute(sqlc, i)
            conn.commit()

        # set default admins
        sqla = "INSERT INTO systemAdmins \
                (name, password, login_status, register_date, email) \
                VALUES \
                (%s, %s, %s, %s, %s)"
        admin = [
            ('David', "12345", 0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'admin1@w.com'),
            ('Anthoer', '7890', 0,str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'admin2@w.com'),
            ('Weber', 'karaki34',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'admin3@w.com')
            ]
        for i in admin:
            cursor.execute(sqla, i)
            conn.commit()

        # set default sellers
        sqls = "INSERT INTO sellers \
                (name, password, login_status, register_date, email) \
                VALUES \
                (%s, %s, %s, %s, %s)"

        seller = [
            ('josh', "12345", 0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'seller1@w.com'),
            ('Anthony', '7890', 0,str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'seller2@w.com'),
            ('carlos', 'karaki34',0, str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')), 'seller3@w.com')
            ]
        
        for i in seller:
            cursor.execute(sqls, i)
            conn.commit()

        # insert items
        
        sqli = "INSERT INTO items \
                (seller_id, name, expiry_date, cost) \
                VALUES \
                (%s, %s, %s, %s)"

        items = [
            (1, 'Nike', "07-06-2050" , 1500.4),
            (2, 'Nike', "07-06-2050" , 1500.4),
            (3, 'Nike', "07-06-2050" , 1500.4)
        ]

        for i in items:
            cursor.execute(sqli, i)
            conn.commit()


        print(cursor.rowcount, "record was inserted.")

    # Customer Controller
    def addCustomer(customer):
        sql = "INSERT INTO customers \
                (name, password, login_status, register_date, email, address) \
                VALUES \
                (%s, %s, %s, %s, %s, %s)"
        
        adm = list(customer)
        adm.pop(-1)
        customer = tuple(adm)
        cursor.execute(sql, customer)
        conn.commit()

    def getCustomerByName(customer):
        sql = "SELECT * FROM Customers where name = '" + customer.username + "' AND password= '" + customer.password + "'"
        cursor.execute(sql)

        # conn.commit()
        return cursor.fetchone()
        
    def setCustomerLoginStatus( status, id):
        sql = "UPDATE customers SET login_status = True WHERE id = "+ id
        cursor.execute(sql)
        conn.commit()
    # def updateCustomer():

    def deleteCustomer( id):
        sql = "DELETE FROM customers WHERE id = " + id

        cursor.execute(sql)

        conn.commit()

    # Admin controller
    def addAdmin(admin):
        sql = "INSERT INTO systemAdmins \
                (name, password, login_status, register_date, email) \
                VALUES \
                (%s, %s, %s, %s, %s)"
        
        adm = list(admin)
        adm.pop(-1)
        adm.pop(-1)
        admin = tuple(adm)

        print(admin)

        cursor.execute(sql, admin)
        conn.commit()

        print("New admin created")

    def suspendSeller( seller_id):
        sql = "UPDATE sellers SET isActive = False WHERE id = "+ seller_id
        cursor.execute(sql)
        conn.commit()

    def getAdminByName(user):
        sql = "SELECT * FROM systemAdmins where name = '" + user.username + "' AND password= '" + user.password +"'"
        # SELECT * FROM User WHERE username = 'WEBER'
        cursor.execute(sql)
        user = cursor.fetchone()
        return user

    # def updateAdmin():
    def setAdminLoginStatus( status, id):
        sql = "UPDATE systemAdmins SET login_status = True WHERE id = "+ id
        cursor.execute(sql)
        conn.commit()

    def deleteAdmin( id):
        sql = "DELETE FROM systemAdmins WHERE id = " + id

        cursor.execute(sql)

        conn.commit()
    
    # Seller controller
    def addSeller(seller):
        sql = "INSERT INTO sellers \
                (name, password, login_status, register_date, email) \
                VALUES \
                (%s, %s, %s, %s, %s)"
        
        print(tuple(seller))

        slr = list(seller)
        slr.pop(-1)
        slr.pop(-1)
        seller = tuple(slr)

        cursor.execute(sql, seller)
        conn.commit()
        print("seller " + seller[0] + " added!")

    def getSellerByName(seller):
        sql = "SELECT * FROM sellers WHERE name = '" + seller.username + "' AND password ='" + seller.password + "'"
        cursor.execute(sql)
        # conn.commit()
        user = cursor.fetchone()
        return user

    def getSellers():
        sql = "SELECT * FROM sellers"
        cursor.execute(sql)
        # conn.commit()
        sellers = cursor.fetchall()
        return sellers

    # def updateSeller():
    def block_seller( id):
        sql = "UPDATE sellers SET isActive = '0' WHERE id = "+ id
        cursor.execute(sql)
        conn.commit()
        print("seller blocked successfully!")

    def unblock_seller( id):
        sql = "UPDATE sellers SET isActive = '1' WHERE id = "+ id
        cursor.execute(sql)
        conn.commit()
        print("seller blocked successfully!")

    def deleteSeller( id):
        sql = "DELETE FROM sellers WHERE id = " + id

        cursor.execute(sql)

        conn.commit()
        print("seller deleted by id " + id + " successfully!")

    # Items Controller
    def createItems(item):
        sql = "INSERT INTO items \
                (seller_id, name, expiry_date, cost) \
                VALUES \
                (%s, %s, %s, %s)"
        
        item = tuple(item)
        print(item)
        

        cursor.execute(sql,item)
        conn.commit()
        print("product added!\n")
        
    def getItems():
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
        return items

    def getItemsBySellerId(seller_id):
        cursor.execute("SELECT * FROM items WHERE seller_id= '" + seller_id + "'")
        items = cursor.fetchall()
        
        return items

    def getItem(id):
        cursor.execute("SELECT * FROM items where id= '" + id + "'")
        item = cursor.fetchone()
        return item
    
    def getItemById( id):
        sql = "SELECT * FROM items where id = " + id
        cursor.execute(sql)

        return cursor.fetchone()

    def updateItemPrice( price, id):
        sql = "UPDATE items SET cost = " + price +  " WHERE id = " + id
        cursor.execute(sql)
        conn.commit()

    def deleteItem(id):
        sql = "DELETE FROM items WHERE id = '" + id +"'"

        cursor.execute(sql)

        conn.commit()
        print("Item successfully deleted!")

    # ShoppingCart Controller
    def createCart(cart, item_id):
        sql = "INSERT INTO shoppingcarts \
                (date_added, customer_id, total_cost, closed) \
                VALUES \
                (%s, %s, %s, %s)"
        
        cursor.execute(sql, cart)
        conn.commit()
        cart_id = cursor.lastrowid
        
        DB.addCartItems(cart_id, item_id)

    def getCartByCustomerId( id):
        sql = "SELECT * FROM shoppingcarts where customer_id = '" + id + "'"
        cursor.execute(sql)

        return cursor.fetchall()

    def checkOpenCart( id):
        sql = "SELECT * FROM shoppingcarts where customer_id = '" + str(id) + "' AND closed ='0'"
        cursor.execute(sql)
        cart = cursor.fetchone()
        # print(cart)
        return cart
    
    def getCartCost(cart_id):
        sql = "SELECT total_cost FROM shoppingcarts where id = '" + str(cart_id) + "'"
        cursor.execute(sql)
        cost = cursor.fetchone()
        return int(cost[0])

    def updateCartTotalCost( price, cart_id):
        sql = "UPDATE shoppingcarts SET total_cost = '" + str(price) +  "' WHERE id = '" + str(cart_id) + "'"

        cursor.execute(sql)

        conn.commit()

    def deleteCart():
        sql = "DELETE FROM Shoppingcarts WHERE id = " + id

        cursor.execute(sql)

        conn.commit()

    # shoppingCartItems controller
    def addCartItems(cart_id, item_id):
        sql = "INSERT INTO itemInCarts \
                (cart_id, item_id) \
                VALUES \
                (%s, %s)"
        
        data = (cart_id, item_id)
        
        cursor.execute(sql, data)
        conn.commit()
        item = DB.getItemById(item_id)
        print(item)
        price = DB.getCartCost(cart_id) + int(item[4])
        DB.updateCartTotalCost(price, cart_id)
        print("Item add to cart")
        
    def getCartItemsByCartId( cart_id):
        sql = "SELECT item_id FROM itemInCarts where cart_id = '" + cart_id + "'"
        cursor.execute(sql)
        items_id = list(cursor.fetchall())

        items_in_cart = []
        for i in items_id:
            i = list(i)
            items_in_cart.append(DB.getItem(str(i[0])))
        return items_in_cart
        
    def updateCartItems( items, cart_id):
        
        DB.deleteCartItems(cart_id)
        DB.addCartItems(cart_id, items) 

    def removeItemFromCart(cart_id):
        sql = "DELETE FROM itemInCarts WHERE cart_id = '" + cart_id + "'"
        cursor.execute(sql)

        conn.commit()
    
    def checkOut(cart_id):
        sql = "UPDATE shoppingCarts SET closed= '1'"
        DB.removeItemFromCart(cart_id )
        cursor.execute(sql)
        conn.commit()
        print("Check out complete")