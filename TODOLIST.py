chores = ["Clean the kitchen counters", "Sweep the hardwood floors", "Dust the living room", "Clean the litter box of Mr. Snuffles"]
print(chores)

question_one = input("Would you like to add any chores to your to do list? Please capitalize your answer.").strip()

while(True):
    if question_one == "Yes":
        question_two = input("What task would you like to add to your TO-DO list?").strip()
        chores.append(question_two)
        print(chores)
        
        question_three = input("Would you like to add anything else? Please capitalize your answer.").strip()
        if question_three == "Yes":
            continue
        else:
            break
