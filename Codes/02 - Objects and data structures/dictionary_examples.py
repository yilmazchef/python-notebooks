# dictionary => key value paren
# databank -> data + identifier (key) 
# product 1, "Chips", 2.80
products = {
    ("C", "Chips (Scoops)") : 2.80, 
    ("F", "Fish (Battered)") : 2.90, 
    ("Fc", "Fish (Crumbed)") : 4.90, 
    ("Fib", "Filet (Battered)") : 6.90, 
    ("Fic", "Filet (Crumbed)") : 6.90,
    ("Hd", "Hot Dog") : 2.60, 
    ("S", "Sausage") : 2.60, 
    ("Mp" , "Meat Patty (Homemade)") : 3.90, 
    ("Cr", "Crabstick") : 2.50, 
    ("Sr", "Spring Roll (Homemade)") : 2.80,
    ("Cr", "Curry Roll (Homemade)"): 2.80, 
    ("Pof", "Potato Fritter (Homemade)") : 1.20, 
    ("Paf", "Paua Fritter (Homemade)") : 5.90, 
    ("Cn", "Chicken Nugget") : 1,
    ("Mh", "Mini Hot Dog (On a stick)") : 1.20, 
    ("Pf", "Pineapple Fritter") : 2.50
}

print( products[("C", "Chips (Scoops)")] )

# key = "de naam van het product"
# val = "het aantal van het product"
order01 = {
    ("C", "Chips (Scoops)") : 2,
    ("F", "Fish (Battered)") : 1,
    ("Cr", "Curry Roll (Homemade)") : 1,
}

order02 = {
    ("C", "Chips (Scoops)") : 4,
    ("F", "Fish (Battered)") : 4,
    ("Cr", "Curry Roll (Homemade)") : 3   
}

processing_orders  = [
    order01, order02
]

# tuple -> immutable (constant) 

# ordered_food = {}

# for food, quantity in order_dictionary.items():
#     for (key, food_name), price in order_menu.items():
#         if food == food_name:
#             total_price = quantity * price
#             print("• {} x{} (${:.2f})".format(food, quantity, total_price))
#             ordered_food[(food, quantity)] = (price, total_price)

# buy = input("Type '-1' to cancel, press any other key to continue.)")
# if buy == "-1":
#     active_ordering = False
#     print("Order is canceled")
# else:
#         active_ordering = True
        
         
# if active_ordering != False:
#         total=0
#         for (food, quantity), (price, total_price) in ordered_food.items():
#             print("• {}    Qty: {}    ${} each    Total ${:.2f}".format(food, quantity, price, total_price))
#             total= total+round(total_price, 2)
#         print("Total to pay ${:.2f}".format(total))