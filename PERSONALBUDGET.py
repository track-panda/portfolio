#Track expenses
#summarize data
#set goals

question = input("Would you like to log any expenses for today? Capitilize, Yes or No.").strip() 

while(True):
    food_expenses = 0
    housing_expenses = 0 
    entertainment_expenses = 0
    savings = 0 

    if question == "Yes":
        category = input("""What category would you like to label your expense? 
                            Enter a number, 1) Food, 2) Housing, 3) Entertainment 4) Savings""").strip()
        if category == "1":
                f_ex = float(input("Please enter the amount of your expense. EX: 14.67").strip())
                print("Your food expenses have totaled to", f_ex + food_expenses, ".")

                again = input("""Would you like to add another expense? Capitilize, Yes or No.""").strip()
                if again == "Yes":
                      continue
                else:
                      pass
                
        elif category == "2":
                h_ex = float(input("Please enter the amount of your expense. EX: 14.67").strip())
                print("Your housing expenses have totaled to",h_ex + housing_expenses,".")

                again = input("""Would you like to add another expense? Capitilize, Yes or No.""").strip()
                if again == "Yes":
                      continue
                else:
                      pass
                
        elif category == "3":
                e_ex = float(input("Please enter the amount of your expense. EX: 14.67").strip())
                print("Your entertainment expenses have totaled",e_ex + entertainment_expenses,".")

                again = input("""Would you like to add another expense? Capitilize, Yes or No.""").strip()
                if again == "Yes":
                      continue
                else:
                      pass
                
        elif category == "4":
                s_ex = float(input("Please enter the amount of your expense. EX: 14.67").strip())
                print("Your savings have totaled to",s_ex + savings,".")

                again = input("""Would you like to add another expense? Capitilize, Yes or No.""").strip()
                if again == "Yes":
                      continue
                else:
                      pass
                
    print("""Here is you total amount of expenses in each section:
          Food Expenses:""", f_ex + food_expenses,"""
        

"""
          )
