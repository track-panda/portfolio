#CHICK-FIL-A

Chicken_Sandwhich = 7
Spicy_Chicken_Sandwhich = 7
Grilled_Chicken_Sandwhich = 8
Chicken_Nuggets_Eight_Count = 6
Chicken_Nuggets_Twelve_Count = 10
Chicken_Salad = 4
Chicken_Wrap = 10
Chicken_Minis = 12
Mac_Cheese = 3
Waffle_Fries = 3
Fruit_Cup = 3
Ice_Cream = 5
Drinks = 1

order_total = 0

while(True):
    print("Welcome to Chick-Fil-A! We have Chicken Sandwhich(number 1), Spicy Chicken Sandwhich(number 2), Grilled Chicken Sandwhich(number 3), Chicken Nuggets Eight Count(number 4), Chicken Nuggets Twelve Count(number 5), Chicken Salad(number 6), Chicken Wrap(number 7), Chicken Minis(number 8), Mac and Cheese (number 9), Waffle Fries(number 10), Fruit Cup(number 11), Ice Cream(number 12), and Drinks(number 13).")
    order = input("What you would like?").strip()
   
    if order == "Chicken Sandwhich" or order == "number 1":
        order_total + Chicken_Sandwhich == order_total
        print("You got a Chicken Sandwhich!")

    if order == "Spicy Chicken Sandwhich" or order == "number 2":
        order_total + Spicy_Chicken_Sandwhich == order_total
        print("You got a Spicy Chicken Sandwhich!")

    if order == "Grilled Chicken Sandwhich" or order == "number 3":
        order_total + Grilled_Chicken_Sandwhich == order_total
        print("You got a Grilled Chicken Sandwhich!")

    if order == "Chicken Nuggets Eight Count" or order == "number 4":
        order_total + Chicken_Nuggets_Eight_Count == order_total
        print("You got an Eight Count Chicken Nugget!")

    if order == "Chicken Nuggets Twelve Count" or order == "number 5":
        order_total + Chicken_Nuggets_Twelve_Count == order_total
        print("You got a Twelve Count Chicken Nugget!")

    if order == "Chicken Salad" or order == "number 6":
        order_total + Chicken_Salad == order_total
        print("You got a Chicken Salad!")

    if order == "Chicken Wrap" or order == "number 7":
        order_total + Chicken_Wrap == order_total
        print("You got a Chicken Wrap!")
 
    if order == "Chicken Minis" or order == "number 8":
        order_total + Chicken_Minis == order_total
        print("You got a Chicken Minis!")

    if order == "Mac and Cheese" or order == "number 9":
        order_total + Mac_Cheese == order_total
        print("You got a Mac and Cheese!")

    if order == "Waffle Fries" or order == "number 10":
        order_total + Waffle_Fries == order_total
        print("You got Waffle Fries!")
    
    if order == "Fruit Cup" or order == "number 11":
        order_total + Fruit_Cup == order_total
        print("You got a Fruit Cup!")

    if order == "Ice Cream" or order == "number 12":
        order_total + Ice_Cream == order_total
        print("You got an Ice Cream!")

    if order == "Drinks" or order == "number 13":
        order_total + Drinks == order_total
        print("You got a Drink!")
 
    order_done = input("Would you like anything else?").strip()
    
    if order_done == "No" or order_done == "no":
        print(order_total)
        break

    elif order_done == "Yes" or order_done == "yes":
        pass
    