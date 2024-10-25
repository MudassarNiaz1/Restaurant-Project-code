# Define the menu of the restaurant

menu = {
    'Pizza' : 400,
    'Pasta' : 350,
    'Salad' : 200,
    'Coffee' : 400,
    'Burger' : 300
}
 
print("--- Welcome to Muddies Restaurant ---")
print("Pizza: Rs.400\nPasta: Rs.350\nSalad: Rs.200\nBurger: Rs. 300\nCoffee: Rs.400")


order_total = 0


user_1 = input("Enter the name of the item you want to order = ")

if user_1 in menu:
  order_total += menu[user_1]
  print(f"Your item {user_1} has been added to your order")
else:
     print(f"Sorry, Ordered item {user_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
        
     item_2 = input("Enter the name of second item = ")
       
     if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added to your order") 
            
     else: 
        print(f"Sorry, Orrdered item {item_2} is not available!")
     print(f"The total amount of items to pay is {order_total}")
