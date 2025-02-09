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
            scene_one_em()

        if koolaidman_HP <= 0:
            print("You have defeated the Kool-Aid Man!")
            break
        print("Your health is =", user_HP,".")
        print("The Kool-Aid Man's health is =",koolaidman_HP,".")
def igloo():
      print("""This is where the journey begins. The igloo is small with remnants of human life evident, 
            for valuables were left behind. You see a light blue cod with a shriveled up blanket on one side, 
            and a desk with what appears to be a broken compass and a torn map.
            There are no windows, but that keeps the little warmth from escaping 
            and keeps the bitter cold from creeping inside. """)
def animal_research_center():
      print(""" The facility is modern with marble floors and steel fixtures and cages. There are cages of penguins everywhere 
            staring at them as they walk by. This place reeks of fish and a weird odor. 
            The wall has a mysterious latch and a foul odor reeks from behind it.""")
def cavern():
      print("""The cavern is dark and cold water drips from the icicles above. 
            There are abandoned lanterns for the character to use, but they require a match. 
            There seems to be nothing here, but then there appears to be a wooden plank poking out from the ice.""")  
def abandoned_research_library(): 
      print("""This place has vaulted ceilings, shelves, and shelves of maps, scrolls, books, etc. 
            Papers are askew all over the floor, lit by the grand chandelier. You are looking for the other piece
            of a map, maybe its in one of the thousands and thousands of books that reside here.""")     
def underground_tunnel_system():  
      print("""This area can explore the true depths of the icy tundra. 
            It is unknown what places this system can take you to, but the risks may be great.
             Are there people here? How can one get here? Once you arrive here, you must fight to survive.""")
      

#SCENES
def scene_one_em():
    print("""You have found yourself stranded from home with no recollection of what happened. You need to find a way back. Legend
          has it that there is a mighty wizard that has powers to send you home. Find the wizard and be sent home! 
          
          """)
    
    print("Good luck!")
    igloo()

    print("""You and your sidekick have entered the igloo and it appears it hasn't seen human civilization in years.
          You scan the room and notice on a desk there is a torn map and the hollow body of a compass.
          You obtain the map and observed that the entire upper right corner is missing. However after you
          analyze the map, you see that there is an Animal Research Center four miles away. That is where you will head next.
          
          """)
    
    choice_one = input("""Before you leave the igloo, you obtain the compass and notice a problem. The magnetic arrow
                       inside the compass is missing and without that arrow the compass is useless. Where should you look first:
                       1) The Floor or 2) The Cot (ONLY ENTER A NUMBER)""").strip()
    
    if choice_one == "1":
         print("There is no arrow on the ground. You try looking near the cot next.")
         print("""As you survey the cot you notice a shiny, red and silver arrow interwoven into the light blue cot. 
               You carefully extract the arrow and pull the compass body out of your pocket. Like magic, the arrow pulls 
               itself towards the compass and clicks into place. With the compass now intact, you may now begin to travel 
               to the Animal Research Center.
               
               """)
         scene_two_em()

    if choice_one == "2":
         print("""As you survey the cot you notice a shiny, red and silver arrow interwoven into the light blue cot. 
               You carefully extract the arrow and pull the compass body out of your pocket. Like magic, the arrow pulls 
               itself towards the compass and clicks into place. With the compass now intact, you may now begin to travel 
               to the Animal Research Center.
               
               """)
         scene_two_em()

def scene_two_em():
    print("Good luck!")
    animal_research_center()

    print("""You and your sidekick travel upon the Animal Research Center and travel inside. When you
          walk inside there is an army of penguins all throughout the center, staring at you as you walk by.
          Then you notice a foul stench radiating from behind a group of penguins. You stand on your tiptoes and
          see a latched door behind them.
          
          """)
    
    choice_two = input("""You need to get to that door, but that group of penguins is in you way. You and your sidekick 
                       survey the room and see a bucket of fish in one corner and a bucket of cowbells in a different corner.
                       You need the penguins to move, do you 1) Use the Bucket of Fish or 2) Use the Bucket of Cowbells,
                       ENTER A NUMBER ONLY""").strip()
    
    if choice_two == "1":
         print("""You walk to the bucket of fish and pick it up. You wrinkle your nose at the smell. You begin tossing fish 
               across the room and away from the door. It takes a minute, but the penguins eventually smell the fish and start
               running for it. You dodge penguins on your way to the door. The latch of the door is rusty, but after exerting some
               effort, the latch breaks off and the door swings free.
               
               """)
         
         print("""You enter the room behind the door and gasp in awe. The room houses shelves and shelves of mysterious potions of
               varying colors and volumes. There is a cauldron in the middle of the room filled with a peculiar green goo. You stare 
               into the cauldron and suddenly a face appears. The face looks creepy and distorted. The face says, 'Please listen to me,
               I know how to set you free, You must travel next to the Abandoned Research Library, That is the place you ought to be.'
               Taking the message to heart, you pull the map and compass out of your bag and travel towards the library.
               
               """)
         scene_three_em()
         
    if choice_two == "2":
         print("""You grab some cowbells from the bucket and begin to shake them violently. The noise from the cowbells fills
               the room and bounces off the walls. The penguins do nothing but continue to stare at you. You shake them some more,
               but still no reaction from the penguins.
               
               """)
         print("""After the failed attempt with the cowbells, you decide to try your other option. You walk to the bucket of fish and pick it up. 
               You wrinkle your nose at the smell. You begin tossing fish across the room and away from the door. It takes a minute, but the penguins 
               eventually smell the fish and start running for it. You dodge penguins on your way to the door. The latch of the door is rusty, 
               but after exerting some effort, the latch breaks off and the door swings free.
               
               """)
         print("""You enter the room behind the door and gasp in awe. The room houses shelves and shelves of mysterious potions of
               varying colors and volumes. There is a cauldron in the middle of the room filled with a peculiar green goo. You stare 
               into the cauldron and suddenly a face appears. The face looks creepy and distorted. The face says, 'Please listen to me,
               I know how to set you free, You must travel next to the Abandoned Research Library, That is the place you ought to be.'
               Taking the message to heart, you pull the map and compass out of your bag and travel towards the library.
               
               """)
         scene_three_em()

def scene_three_em():
    print("Good luck!")
    abandoned_research_library()

    print("""You and your sidekick arrive to the Abandoned Research Library after traveling miles in the frozen tundra.
          The library is one big room housing thousands and thousands of books, and you begin to feel overwhelmed. The face didn't 
          tell you what you were looking for, so you are having to search the room one book at a time.
          
          """)
    choice_three = input("""After hours of searching, you begin to get frustrated. You sit on a desk in the middle of the room and fiddle with a
          box of matches that you found lying around. As you look around the room should you realize you need to make a plan. 
          Should you first search 1) Books that have dull covers or 2) Books that have colorful covers, ENTER A NUMBER ONLY""").strip()
    
    if choice_three == "1":
         print("""You begin to only search through only books that are dull, with you taking the east side of the room 
               and your sidekick taking the west side. After finishing your section, discovering nothing, you check on your
               sidekick anf discovered they also had no luck. It seems as though the next best course of action is to analyze
               the books that have colorful covers.
               
               """)
         print("""There is only one option left, so you begin to only review the books that have colorful, vibrant covers, with you taking the east side and
                your sidekick taking the west side. You begin to lose hope as you only have one bookshelf to go, but then you notice
               a book that is particularly shiny. The others haven't been remotely shiny. Your sidekick bounds over and perches 
               beside you as you open the front cover of the book. Nothing. You continue flipping and a slip of paper slips out onto the floor.
               
               """)
         print("""Your sidekick picks it up with their mouth and spits it out infront of you. It is the missing corner of your map!
               You pull out the map out of your bag and when you line up the pieces, the map suddenly sews itself together into one 
               piece. As you flip the map over onto the back, a note in cursive magically appears reading, 'Head to the cavern!'. You 
               contine to stand there in awe as this map is pure magic. You decide to listen to the note on the back of the map, and 
               yout journey in the frozen tundra continues.
               
               """) 
         scene_four_em()

         
    if choice_three == "2":
         print("""You begin to only review the books that have colorful, vibrant covers, with you taking the east side and
                your sidekick taking the west side. You begin to lose hope as you only have one bookshelf to go, but then you notice
               a book that is particularly shiny. The others haven't been remotely shiny. Your sidekick bounds over and perches 
               beside you as you open the front cover of the book. Nothing. You continue flipping and a slip of paper slips out onto the floor.
               
               """)
         print("""Your sidekick picks it up with their mouth and spits it out infront of you. It is the missing corner of your map!
               You pull out the map out of your bag and when you line up the pieces, the map suddenly sews itself together into one 
               piece. As you flip the map over onto the back, a note in cursive magically appears reading, 'Head to the cavern!'. You 
               contine to stand there in awe as this map is pure magic. You decide to listen to the note on the back of the map, and 
               yout journey in the frozen tundra continues.
               
               """)
         scene_four_em()

def scene_four_em():
    print("Good luck!")
    cavern()

    print("""You and your sidekick finally come across the cavern after walking through the tundra for hours. The cavern sits in
          middle of the frozen tundra acting as a shield against the freezing cold snow and wind. You enter the cavern and notice
          a pile of lanterns off to the side. You remove the box of matched from your bag and light a match and toss it into the 
          cage of the lantern. The lantern helps illuminate the open space.
          
          """)
    
    choice_four = input("""With a lantern lit, you need to survey the cavern to look for directions on what to do next. Do you
                        1) Survey the walls first or 2) Survey the ground first. ENTER A NUMBER ONLY""").strip()
    
    if choice_four == "1":
         print("""You decide to search the walls of the cavern first. Maybe there are drawings or enscriptions that could
               be potentially useful on your journey. You graze your hand across each wall, feeling every groove of the ice 
               beneath your fingertips. After surveying each wall, you find nothing. Looks like your final option is to search
               the ground for clues.
               
               """)
         print("""You have decided to search the ground of the cavern first. You crawl on your hands and knees moving a sole
               inch at a time. As you make your way across the cavern, you watch your sidekick sniff out and start to paw at
               a spot in the ice. Perplexed, you crawl towards them and wipe the snow off that spot. You see a wooden trap door.
               Curious, you pull on the handle and the door flies open, revealing a ladder beneath. 
               You get a hopeful feeling and crawl down the ladder and into the darkness.
               
               """)
         scene_five_em()
    
    if choice_four == "2":
         print("""You have decided to search the ground of the cavern first. You crawl on your hands and knees moving a sole
               inch at a time. As you make your way across the cavern, you watch your sidekick sniff out and start to paw at
               a spot in the ice. Perplexed, you crawl towards them and wipe the snow off that spot. You see a wooden trap door.
               Curious, you pull on the handle and the door flies open, revealing a ladder beneath. 
               You get a hopeful feeling and crawl down the ladder and into the darkness.
               
               """)
         scene_five_em()

def scene_five_em():
    print("Good luck!")
    underground_tunnel_system()

    print("""You climb down the mysterious ladder and into the void. When you finally reach the bottom of the ladder,
          you are engulfed in the darkness. You relight your lantern and survey the room. There is a door located on the northern wall
          of the room. You notice there are various pipes interweaving on all the other walls and covering the door. You turn to your
          left and see a control panel with a series of valves and these valves are one of four colors: Purple, Blue,
          Green, and Red. As you survey the room more you realize that all of the various pipes are one of these four colors. Maybe
          the control panel can open the door in front of you.

        """)

    choice_five = input("""Before you approach the control panel, you notice there are three slips of paper scattered on the ground
                    around the room. Do you pick 1) Head to the control panel anyway 2) Pick-up the pieces of paper ENTER ONLY A NUMBER

                    """).strip()
    
    if choice_five == "1":
         print("""You have decided to ignore the slips of paper and head to the control panel anyways. As you analyze the panel,
               you notice that there are four labels. Red = Hot, Blue = Cold, Green = Pressure Release, and Purple = Steam. You realize
               that you have no instructions and that those slips of paper might actually be helpful. You acquire the slips of paper
               and there are clues that read:

                """)
         
         print("The cold water comes first, but do not let it freeze")
         print("Too much steam will boil the pressure away")
         print("Heat before you release")

         print("""Reading these three clues confirms your suspicions. The pipes are part of a puzzle. You must solve the puzzle to advance
           furthur and potentially find the solution you need to that can take you home. After reading these clues, you approach the
           control panel and see four labels. Red = Hot, Blue = Cold, Green = Pressure Release, and Purple = Steam. These labels and the
           clues should be enough to solve the puzzle.

            """)
     
         puzzle = input("""To advance in the game, you must open and release the correct series of valves in order to open the door. Every time
               you get the answer wrong the scene will restart! Be careful!! When entering you answer please type the color with
               open or closed in parentheses. EXAMPLE: Pink(Release) IF YOU GET IT CORRECT YOU WILL BE ABLE TO TYPE AGAIN
               Please enter a color sequence:
            
               """).strip()
    

    if choice_five == "2":
        print("""You decided to acquire the three pieces of paper first and see what they say. There is one clue on each slip of paper
            it reads:

                """)
        
        print("The cold water comes first, but do not let it freeze")
        print("Too much steam will boil the pressure away")
        print("Heat before you release")

        print("""Reading these three clues confirms your suspicions. The pipes are part of a puzzle. You must solve the puzzle to advance
            furthur and potentially find the solution you need to that can take you home. After reading these clues, you approach the
            control panel and see four labels. Red = Hot, Blue = Cold, Green = Pressure Release, and Purple = Steam. These labels and the
            clues should be enough to solve the puzzle.

                """)
        
        puzzle = input("""To advance in the game, you must open and release the correct series of valves in order to open the door. Every time
                you get the answer wrong the scene will restart! Be careful!! When entering you answer please type the color with
                open or closed in parentheses. EXAMPLE: Pink(Release)
                Please enter a color sequence:
                
                """).strip()


    while(True):
            if puzzle == "Red(Open)":
                puzzle_two = input("Please enter the second sequence:").strip()
                if puzzle_two == "Green(Release)":
                    puzzle_three = input("Please enter the third sequence:").strip()
                    if puzzle_three == "Blue(Open)":
                            puzzle_four = input("Please enter the final sequence:").strip()
                            if puzzle_four == "Yellow(Release)":
                                break
                            
            else:
                scene_five_em()

    print("""You stand there breathing heavily and suddenly you hear gears turning. You turn around and the pipes
                around the door are retracting into the walls leaving the door standing alone. You have done it! You have 
                completed the puzzle!!
                                
                """)
        
    print("""With the pipes being removed, you use your key to unlock the door. You pull the door open and you see a figure in the
            shadows. He is made of glass and there seems to be a red flowing liquid churning inside of him; shaped as a glass
            pitcher. The suddenly he turns towards you.

                """)
        
    print("""I see that you have made the journey to find the wizard. I know that you seek a way home, but you are going to
            have to get passed me first, THE KOOL-AID MAN!!!

            """)
        
    print("""The Kool-Aid Man turned around and you see the wizard stuck inside the red liquid inside the Kool-Aid Man! 
            You must defeat the Kool-Aid Man so that you can free the wizard and go home! Good Luck! If you die the entire game will restart!
            """)
    
    combat()

    print("YOU HAVE DONE IT! The Kool-Aid Man became a heap of sharp glass on the floor and the wizard is free.")

    print("""Thank you for saving me! I realize that you have been searching for me, so that I may send you home.
          You have showed me your bravery here today. Off to home you go!
          
          """)
    
    print("""You are surrounding by a cloud of purple dust and suddenly you are back home, in your tree house, like nothing ever happend.
          Thank you for playing! I hope you enjoyed it!
          
          """)
    

#scene_five_em()
    




    
    

