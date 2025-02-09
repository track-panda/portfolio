snacks = ["Popcorn", "Yogurt", "Chickpea", "Trail Mix", "Hard Boiled Eggs", "Apple and Peanut Butter", "Hummus", "Cheese", "Fruit", "Nuts"]
print(snacks)

while(True):
    question_one = input("Would you like to add any values to the list? Capitalize your answer.").strip() 
    if question_one == "Yes":
        question_two = input("What would you like to add?").strip()
        snacks.append(question_two)
        print(snacks)

    else:
        print("Oh okay!")
    break

while(True):
    question_three = input("Would you like to remove any value from the list? Capitalize your answer.").strip()
    if question_three == "Yes":
        question_four = input("What would you like to remove? Please copy the value entirely how it is written.").strip()
        snacks.remove(question_four)
        print(snacks)
        
    else: 
            print("Oh okay!")
            break

while(True):
    question_five = input("Would you like to sort the list? Please capitalize your answer.").strip()
    if question_five == "Yes":
        snacks.sort()

    else:
        print("Oh okay! Here is your list again.")
        print(snacks)
        break
