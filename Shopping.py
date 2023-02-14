import random
class Shopper:
    def __init__(self, name):
        self.name  = name
        self.cart = []
    
    def add_to_cart (self , item, price, quantity):
        self.cart.append({'name': item, 'price':price, 'quantity': quantity })

    def checkout (self, amount):
        price = 0
        for item in self.cart:
            price = price + item['price'] * item['quantity']
        if amount< price:
            return f'Please give me more {price - amount} taka'
        elif amount > price:
            return f'Here is the items and extra money : {amount - price}'
        else:
            return f'Here is your items'

shop=Shopper("Bata")
while True:
    print("1.Order Items")
    print("2.Order Checkout")
    print("3.Exit")
    print("Enter choice:",end="")
    ch=int(input())
    if ch==1:
        print("Enter Item Name:",end="")
        itemName=input()
        print("Enter total quanitiy:",end="")
        total=int(input())
        totalPrice=random.randint(10,1000)
        shop.add_to_cart(itemName,totalPrice,total)
    elif ch==2:
        print("Enter the amound you are willing to pay:",end="")
        payment=int(input())
        print(shop.checkout(payment))
    elif ch==3:
        print("Program Exited")
        break
    else:
        print("Invalid Choice")

