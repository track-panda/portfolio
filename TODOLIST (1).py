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

while(True):
    question_four = input("Okay! Would you like to mark any tasks as done on your TO-DO list? Please capitalize your answer.").strip()
    if question_four == "Yes":
        question_five = input("What would you like to mark as complete? Please type task as formatted previously.").strip()
        chores.remove(question_five)
        print(chores)

        question_six = input("Would you like to mark anything else as complete? Please capitalize your answer.").strip()
        if question_six == "Yes":
                continue
        else:
            break

while(True):
    question_seven = input("Would you like to sort your list? Please capitlize your answer.").strip()
    if question_seven == "Yes":
        chores.sort()
        print(chores)
    else:
        break

