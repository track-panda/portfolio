import random 

user_HP = 50
enemy_HP = 45

flamingo_flurry = 15
snow_ball = 5
lightning_bolt = 20
seafood_plate = 7
kick = 5

racoon_bite_rabies = user_HP
sword_slash = 10
John_Cena_special = 20
punch = 5
bazooka = 8

while(True):
    CPU_choice = random.randrange(5)
    user_attack = int(input("Give me an attack. 1) FlamingoFlurry, 2) Snowball, 3) Lightningbolt, 4) SeafoodPlate, 5) Kick").strip())
    if user_attack == 1:
        print("User chose to use the FlamingoFlurry.")
        enemy_HP -= flamingo_flurry

    if user_attack == 2:
        print("User chose to use the Snowball.")
        enemy_HP -= snow_ball

    if user_attack == 3:
        print("User chose to use the Lightining Bolt.")
        enemy_HP -= lightning_bolt

    if user_attack == 4:
        print("User chose to use the Seafood Plate.")
        enemy_HP -= seafood_plate

    if user_attack == 5: 
        print("User chose to use the Kick.")
        enemy_HP -= kick

    if CPU_choice == 0:
        print("Coach K. chose to use the Raccoon Rabies Bite.")
        user_HP -= racoon_bite_rabies

    if CPU_choice == 1:
        print("Coach K. chose to use the Sword Slash.")
        user_HP -= sword_slash

    if CPU_choice == 2:
        print("Coach K. chose to use the John Cena Special.")
        user_HP -= John_Cena_special

    if CPU_choice == 3:
        print("Coach K. chose to use the Punch.")
        user_HP -= punch

    if CPU_choice == 4:
        print("Coach K. chose to use the Bazooka.")
        user_HP -= bazooka

    if user_HP <= 0:
        print("User has succumbed to their injuries. Coack K. Wins.")
        break 

    if enemy_HP <= 0:
        print("Coach K. succumbed to his injuries. You Win!")
        break
    print("User HP = ",user_HP,".")
    print("Enemy HP =",enemy_HP,".")


