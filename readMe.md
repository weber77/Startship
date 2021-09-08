- we removed admin class from diagram. Bcs the email attribute existed both in customer and all admins.
- we changed Website class to systemAdmin
- we remove email and respective names attributes from user subclasses  and added it to user class as email and name respectively.
- Seller updatePrice method was rename to updateItem bcs seller can want to update other attributes of an item.
- we removed manageOnlineShop() from systemAdmin class and splited it into verious sub methods

+ add sellers inventory class
- removed soldOut() from Seller class and implemented it into inventory class as checkItemQuantity().
- removed shippingInfo from Customer class
- removed updateProfile() from Customer and implemented it in parent User class.

- we removed the link between customer and item.
+ added a link between Seller and Item. this is bcs the Seller can modify (CRUD) the item
+ added cost attribute to item

- In shoppingCart, we replace productDictionary for productId and quantity bcs a production is associated with it's quantity in a cart. And added  customer_id, total_cost

- we changed updateQuantity() from ShoppingCart to updateItemQuantity()
- I removed the customerName attribute from Order class
- I removed the unitCost, productId attributes from Payment class and replaced subTotal by total_cost
- changed proceedPayment() to processPayment() and removed selectMethod()
- changed Verfication to bankAccount class and added  Balance, expiry_date attributes.
- removed accountCheck() from BankCard class.

- changed shippingRegion to shippingAddress in shipping class

-- we removed DeliveryCompany class

+ created new class ItemInCart to accomodate for many to one relationship between items and cart
+ added table payment_methods
+ added order_id to shipping class
+ added seller_id to item
+ added is active to seller class
