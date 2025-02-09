import random

user_HP = 100
koolaidman_HP = 125

bear_hug = 10
leg_sweep = 5
spinebuster = 15
german_suplex = 25
deafening_blow = 50

John_Cena_special = 20
punch = 10
bazooka = 15
tropical_tsunami = 45


while(True):
    villain_attack = random.randrange(4)
    user_attack = int(input("Choose an attack: 1) Bear Hug 2) Leg Sweep 3) Spinebuster 4) German Suplex 5) Deafening Blow; Please enter in the number only.").strip())

    if user_attack == 1:
        print("You have chosen to use the Bear Hug")
        koolaidman_HP = koolaidman_HP - bear_hug

    if user_attack == 2:
        print("You have chosen to use the Leg Sweep")
        koolaidman_HP = koolaidman_HP - leg_sweep

    if user_attack == 3:
        print("You have chosen to use the Spinebuster")
        koolaidman_HP = koolaidman_HP - spinebuster

    if user_attack == 4:
        print("You have chosen to use the German Suplex")
        koolaidman_HP = koolaidman_HP - german_suplex

    if user_attack == 5:
        print("You have chosen to use the Deafening Blow")
        koolaidman_HP = koolaidman_HP - deafening_blow

    if villain_attack == 0:
        print("The Kool-Aid Man decided to use the John Cena Special.")
        user_HP = user_HP - John_Cena_special

    if villain_attack == 1:
        print("The Kool-Aid Man decided to use the Punch.")
        user_HP = user_HP - punch

    if villain_attack == 2:
        print("The Kool-Aid Man decided to use the Bazooka.")
        user_HP = user_HP - bazooka

    if villain_attack == 3:
        print("The Kool-Aid Man decided to use the Tropical Tsunami.")
        user_HP = user_HP - tropical_tsunami

    if user_HP <= 0: 
        print("You were defeated by the Kool-Aid Man!")
        break

    if koolaidman_HP <= 0:
        print("You have defeated the Kool-Aid Man!")
        break
    print("Your health is =", user_HP,".")
    print("The Kool-Aid Man's health is =",koolaidman_HP,".")
         

        

    


        
