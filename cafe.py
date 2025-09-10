menu = {
    'Pizza': 99,
    'Burger': 80,
    'Chowmin': 60,
    'Ice-cream': 50,
    'Pasta': 40,
    'chiken roll': 120,

}

print("Welcome to TRP cafe")
print("Pizza: Rs99\nBurger: Rs80\nChowmin: Rs60\nIce-cream: Rs50\nPasta: Rs40\nchiken roll: Rs120\n")

order_total = 0

item_1 = input("enter the name of the item that you want = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")    

another_order = input("do you want to add more item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your oder")
else:
     item_2 = None

print(f"the total amount of items to pay {order_total}")                