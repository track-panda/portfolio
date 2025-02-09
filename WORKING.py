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
      print(""" This place has vaulted ceilings, shelves, and shelves of maps, scrolls, books, etc. 
            Papers are askew all over the floor, lit by the grand chandelier.""")     
def underground_tunnel_system():   
      print("""This area can explore the true depths of the icy tundra. 
            It is unknown what places this system can take you to, but the risks may be great.
             Are there people here? How can one get here?""")


def scene_one_em():
    print("""You have found yourself stranded from home with no recollection of what happened. You need to find a way back. Legend
          has it that there is a mighty wizard that has powers to send you home. Find the wizard and be sent home! NOTE: YOU MAY VIEW,
          ADD, AND USE ITEMS FROM YOUR INVENTORY IN THE MAIN MENU.
          
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
         scene_five_em
    
    if choice_four == "2":
         print("""You have decided to search the ground of the cavern first. You crawl on your hands and knees moving a sole
               inch at a time. As you make your way across the cavern, you watch your sidekick sniff out and start to paw at
               a spot in the ice. Perplexed, you crawl towards them and wipe the snow off that spot. You see a wooden trap door.
               Curious, you pull on the handle and the door flies open, revealing a ladder beneath. 
               You get a hopeful feeling and crawl down the ladder and into the darkness.
               
               """)
         scene_five_em()

#STILL WORKING HERE
def scene_five_em():
    print("Good luck!")
    underground_tunnel_system()


scene_one_em()

