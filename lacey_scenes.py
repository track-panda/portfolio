import random
def combat():
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
            lacey()

        if koolaidman_HP <= 0:
            print("You have defeated the Kool-Aid Man!")
            break
        print("Your health is =", user_HP,".")
        print("The Kool-Aid Man's health is =",koolaidman_HP,".")



def abandoned_house():
      print("""There is a small mattress in the corner. The house is filled with cobwebs and has a leaky roof. 
            There is no heating or electricity in the house""")
      global inventory
def market():
      print("""The market is packed with people shopping in the afternoon. The shops are brightly lit and inviting. 
            This is where you can purchase supplies for your adventure.""")
      global inventory
def temple():
      print("""The temple is connected to the garden. The temple is large and uninviting. Everything inside is well
            kept but it does not look like anyone is there.""")
      global inventory
def garden():
      print("""The garden is connected to the temple. It is filled with all sorts of plants, trees, and flowers. 
            Animals frequently visit this garden.""")
      global inventory
def old_shop():
      print("""The old shop is located in the market. It is rumored that the owner may know the
            wizard. The shop is dimly lit and looks like it hasen't been stocked in years.""")
      global inventory

def room2():
    print("""congrats, you have reached the 2nd level of the palace, but 
        I doubt you'll make it any further""")
def room1():
    print("""you have entered my palace with hopes of beating me and returning home.
        I accept your challenge but you will need to solve 3 riddles first.
        if you get any wrong, you will have to restart, so remember
        your answers. """)
def room3():
            print("""how did you manage to make it here? 
                There's no way you'll solve my 3rd riddle""")

def lacey():
    
        print("""You wake up in the middle of nowhere. You glance outside and notice you are in a small town in Asia. 
                    You walk to the near by shops in hopes to find the so called 'wizard' who can teleport you home. 
                    You have a backpack containing a half-full waterbottle and a granola bar. 
                    REMINDER: Make sure to always have food and water because your health will go down if you don't!""")


        choice1as=input("You arrive at the shops tired and hungry. Do you: 1. Eat a granola bar, 2. Explore the shops, 3. Ask about the wizard PLEASE ENTER ONLY A NUMBER")
        if choice1as==("1"):
                    print("you ate a granola bar. You choose to explore the shops and familiarize yourself with the area. You notice an old shop in the distance and walk towards it. ")
                    item ="granola bar"
        elif choice1as==("2"):
                    print("you chose to explore the shops. You see an old shop and walk towards it.")
        elif choice1as==("3"):
                    print("you chose to ask about the wizard. The people thought you were crazy. you see an old shop nearby and go to it.")
        else:
                    print("invalid response. please try again!")

        choice2as=input("""You head over to the old shop and look inside. It doesn't look like anyone is in there.
                            But, you need to find the wizard to be sent home. Do you: 1. Enter the shop, 2. Walk away. PLEASE ENTER ONLY A NUMBER""")
        if choice2as==("1"):
            old_shop()
            print("""you chose to go in the shop. You look around and at first you dont see anyone. 
                        Suddenly, you see a figure moving in the corner of your eye. You turn around and it is none other than 
                        the wizard, Bartholamew Richard Fitzgerald-Smythe! But he doesn't really look like a wizard
                        he kinda just looks like a peanut.""")
            wizard=input("yay you found the wizard! Do you: 1. ask to send you home, 2. try and befriend him before asking him to send you home")
            if wizard==("1"):
                        print("""you asked the wizard nicely to send you home. He explains that the Kool-aid man has stolen his powers and he is not able to fight back.
                                However, The wizard says that he can send you home IF you help him defeat the Koolaid man. The wizard offers you a place
                                to stay for the night before you go to confront the Kool-aid man tommorow.""")
            elif wizard==("2"):
                        print("""you attempt to befriend the wizard. He is nice but quiet. Eventually, you ask him to send you home. 
                                He explains how the Kool-aid man has stolen his powers so he is unable to. 
                                But, He says if you can help him get his powers back then he will get you home!
                                The wizard offers you a place to stay for the night before fighting the kool-aid man tommorow.""")
            else:
                    print("response invalid, plase try again!")
        elif choice2as==("2"):
            print("""you chose to walk away from the shop. You might regret this later! You walk back to the abandoned house you woke up in and prepare for the night.""")
            abandoned_house()
            minichoice=input("""you prepare for bed but are suddenly startled by someone trying to open the window.
                                You decide to walk towards the window and investigate. You look out the window and see
                                a...peanut? He asks you to let him in and he will explain himself. Do you:
                                1. hear  him out, 2. yell at him to leave? please enter only a number.""")
        if minichoice==("1"):
                                print("""you decided to let the peanut-man inside. He explains that he
                                    can help you get home IF you help him defeat the koolaide man.
                                    You decide to help him so that you can return home""")
        elif minichoice==("2"):
                                print("""the peanut-man doesn't listen and breaks the window to enter. 
                                    He explains that he can get you home IF you help him defeat the koolaide man first.
                                    You appoligize and agree to help him defeat the koolaide man.""")
        else:
            print("invalid response please try again!")

                    
        choice3as=input("""morning finally arrives. You grab your backpack and follow the peanut
                            to the temple that the koolaide man supposedly lives in. The path you're
                            one suddenly splits into two different directions. Do you: 1. go left, 2. go right? 
                            PLEASE ENTER ONLY A NUMBER""")
        if choice3as==("1"):
                garden()
        elif choice3as==("2"):
                temple()
        else:
                print("invalid response, please try again!")

        
        print("""You continue walking and hear a booming voice in the distance.""")
        room1()
        riddle=input("what has an eye but can't see?")
        if riddle==("needle"):
                room2()
        else:
                room1()
        
        
        riddletwo=input("what has legs but can't walk?")
        if riddletwo=="table":
                room3()
        else:
                room1()
        riddlethree=input("I am an odd number, take away a letter and I become even. What am i?")
        if riddlethree==("seven"):
            print("""I never expected you to make it here. Since you have solved my riddles 
                    you now have to defeat me or there's no way you're ever 
                    going home!""")
            combat()
        else:
            room1()


    



