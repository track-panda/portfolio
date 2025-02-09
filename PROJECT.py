import random 
introduction = random.randrange(0,2)

class Person: 
    def __init__(self, name, motivation, role, relationships, strengths, weaknesses, appearance):
        self.name = name
        self.motivation = motivation
        self.role = role
        self.relationships = relationships
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.appearance = appearance 

    def character_name(self):
            return self.name
        
    def character_motivation(self):
            return self.motivation
        
    def character_role(self):
            return self.role
        
    def character_relationships(self):
            return self.relationships
        
    def character_strengths(self):
            return self.strengths
        
    def character_weaknesses(self):
            return self.weaknesses
        
    def character_appearance(self):
            return self.appearance 
class Animal:
    
    def __init__(self, name, strength, weakness):
        self.name = name
        self.strength = strength 
        self.weakness = weakness 

    def character_name(self):
          return self.name
    
    def character_strength(self):
          return self.strength
    
    def character_weakness(self):
          return self.weakness

#I HAVE NOT FINISHED THIS I WILL FURTHUR INTO THE GAME 
class Character:
      def __init__(self, name, role, relationship, goal):
            self.name = name
            self.role = role
            self.relationship = relationship
            self.goal = goal

      def character_name(self):
            return self.name 
      
      def character_role(self):
            return self.role
      
      def character_relationship(self):
            return self.relationship
      
      def character_goal(self):
            return self.goal

#ANARCTICA ROOMS
def igloo():
      global inventory_zero
      print("""This is where the journey begins. The igloo is small with remnants of human life evident, 
            for valuables were left behind. You see a light blue cod with a shriveled up blanket on one side, 
            and a desk with what appears to be a broken compass and a torn map.
            There are no windows, but that keeps the little warmth from escaping 
            and keeps the bitter cold from creeping inside. """)
def animal_research_center():
      global inventory_zero
      print("""This is the destination that the character will travel to if they decide on the four-mile journey. 
            The facility is modern with marble floors and steel fixtures and cages. There are cages of penguins everywhere 
            staring at them as they walk by. This place reeks of fish and a weird odor. 
            The wall has a mysterious latch and a foul odor reeks from behind it.""")
def cavern():
      global inventory_zero
      print("""The cavern is dark and cold water drips from the icicles above. 
            There are abandoned lanterns for the character to use, but they require a match. 
            There seems to be nothing here, but then there appears to be a wooden plank poking out from the ice.""")  
def abandoned_research_library():
      global inventory_zero
      print("""This destination is where the character will travel if they choose the grueling ten-mile journey. 
            This place has vaulted ceilings, shelves, and shelves of maps, scrolls, books, etc. 
            Papers are askew all over the floor, lit by the grand chandelier.""")     
def underground_tunnel_system(): 
      global inventory_zero
      print("""This area can explore the true depths of the icy tundra. 
            It is unknown what places this system can take you to, but the risks may be great.
             Are there people here? How can one get here?""")

#ASIA ROOMS
inventory=["water bottle", "granola bar"]
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

#GAME CODE STARTS HERE

character_type = input("""Welcome to the game Finding My Way Home. Would you rather be the Female character or the Male character? Please capitalize your answer.""").strip()
person: Person

if character_type == "Female":
     person = Person("Your character's name is Maisie Melite", "Your character's goal is to find the great wizard", "Your character is the main character", "Your character is allies with the Hippo.", "Your character is fast/agile, smart and has a high stamina", "Your character is not very strong, has reduced stamina in colder environments, and is allergic to red dye", "Your character is 5'0 tall, has blue eyes, brown wavy mide-length hair, has freckles, and is pale.")
else:
    person =  Person("Your character's name is Devin Davis", "Your character's goal is to find the great wizard.", "Your character is the main character", "Your character is allies with the Hippo.", "Your character is strong, smart, and not affected by temperature", "Your character is not very fast/agile, has low stamina, and is allergic to peanut butter", "Your character is 6'0 tall, has one brown eye and one green eye, short, brown hair, is tan, and has a pink birth mark.") 

question = input("You have chosen a character! Enter a letter A thru G to find out important information about your new character.").strip()

while(True):
      if question == "A":
            print(person.character_name())

      elif question == "B":
            print(person.character_motivation())

      elif question == "C":
            print(person.character_role())

      elif question == "D": 
            print(person.character_relationships())

      elif question == "E":
            print(person.character_strengths())

      elif question == "F":
            print(person.character_weaknesses())

      elif question == "G":
            print(person.character_appearance())

      instruction = input("Would you like to learn more?").strip()

      if instruction == "Yes":
            question = input("You have chosen a character! Enter a letter A thru G to find out important information about your new character.").strip()
            
      elif instruction == "No":
            break

friend_character = input("Now that you have chosen your main character, please choose one of the following side characters: Platypus, Hippo, Frog.").strip()
friend: Animal

if friend_character == "Platypus":
      friend = Animal("Your side character's name is Mystic Noodlefin.", "Your side character's strength is that they are a good swimmer.", "Your character's weakness is that they are stupid.")
elif friend_character == "Hippo":
      friend = Animal("Your side character's name is Nina.", "Your side character's strength is that they are strong.", "Your character's weakness is that they are temperamental/ bites people.")
elif friend_character == "Frog":
      friend = Animal("Your side character's name is Gidget.", "Your side character's strength is that they are good at solving problems.", "Your character's weakness is that they are small.")

question_two = input("You have chosen a side character, type a letter A - C to learn information about your new friend!").strip()

while(True):
      if question_two == "A":
            print(friend.character_name())

      elif question_two == "B":
            print(friend.character_strength())

      elif question_two == "C":
            print(friend.character_weakness())
      else:
            break

      instruction = input("Would you like to learn more?").strip()

      if instruction == "Yes":
            question_two = input("You have chosen a friend character! Enter a letter A thru C to find out important information about your new character.").strip()
            
      elif instruction == "No":
            break

others = input("""Well done on choosing your new side character! 
               To make the game more mysterious, two of the characters and their traits will 
               not be revealed until applicable in the game. Have fun! (Press ENTER to proceed...)""")


#EMERSON START
inventory_zero = ["Three Granola Bars","Two Canteens","One Key"]

if introduction == 0:
      print("""You awake outside of an igloo with a backpack strapped tightly around you, surrounded by a thick blanket of snow that hides any 
            indication of civilization and no recollection of what happened. 
            The winds are fierce almost knocking you over several times""") 

      while(True):
            igloo_entry = input("Enter the igloo?").strip()

            if igloo_entry == "No":
                  print("You have to enter the igloo! You are freezing!")

            else: 
                  print("You have entered the igloo.")
                  igloo()
                  map = "Map"
                  inventory_zero.append(map)
            break

      print("""You set your belongings on the cot and analyze the map. You notice the map is missing the entire upper right corner, however, to your luck, the map is still legible. 
            The map indicates that you are near the southwestern border of Antarctica, 4 miles east of a research base, 
            and 10 miles south of a different research base. There is a note on the bottom of the map that notes limited supplies in the 
            Animal Research Center base 4 miles from you. The map also notes that the base ten miles away is the Research Library Base. You are forced to make a choice. 
            Travel four miles to the nearest base but risk finding no supplies, or traveling ten miles north and risk dying in the cold in pursuit of knowledge.""")

      choice_one = input("What will you chose? Option One: Travel to the Animal Research base 4 miles away. Option Two: Travel to the Research Library base 10 miles away. Type in a number please.").strip()

      if choice_one == "1":
            print("You have chosen to travel the shorter four mile distance to the Animal Research base, however, before you can leave you must grab the compass first!")
            compass = "Compass"

            while(True):   
                  compass = input("Pick up Compass? Capitalize your answer.").strip() 
                  if compass == "No":
                              print("You can't go anywhere without the compass!")
                  else:
                        inventory_zero.append(compass)
                        break 

                  print("""You have now accquired a compass! The glass front of the compass was covered with snow, so you take the sleeve of your shirt and wipe it off, that is when you notice a problem.
            The arrow inside the compass was missing. You remember that the arrow witin a compass is magnetic, and rotates directions based on the magnetic force exhibited by the Earth.
            Without that arrow, the compass will be useless. You need to find it.""")
                         
            arrow_zero = input("Where will you check first? The cot or the floor? Please capitalize your answer.").strip()

            if arrow_zero == "Cot":
                print("""You move to the East side of the igloo. This area of the igloo is empty besides your torn backpack sitting upon the cot.
                        You pick up your backpack and see nothing. When you set down your bag you notice a shimmer to your right. 
                      You look down and see a metallic arrow interwoven in the cot's fabric.""")

            elif arrow_zero == "Floor":
                  print("""You lower yourself onto your hands and knees and start analyzing the ground. You see nothing besides the hard packed ice below you.
                        Your hands begin to go numb as you grave your hand over the ice's ridges. You still see nothing.""")
                  
                  search = input("Do you want to keep searching the floor or move on to the cot? Enter a number: 1) Keep searching the floor or 2) Search the cot instead")
                  if search == "1":
                        print("")
                  else: 
                        print("""You give up looking on the floor and make your way to the cot. You move to the East side of the igloo. 
                              This area of the igloo is empty besides your torn backpack sitting upon the cot. You pick up your backpack and see nothing.
                              When you set down your bag you notice a shimmer to your right. You look down and see a metallic arrow interwoven in the cot's fabric.""")
                        
                  arrow = "Compass Arrow"
                  while(True):
                        arrow_one = input("Pick up the arrow? Capitalize your answer.")
                        if arrow_one == "No":
                              print("You can't advance without it!")
                        else:
                              inventory_zero.append(arrow)
                              break

                        print("""You work to unweave the arrow, and within seconds you set it free. 
                                    You hold it up to the light. It is small, with a red tip. You should pull out the compass from your bag.""")
                              
                  while(True):
                        compass_arrow = input("Pull out the compass? Capitalize your answer.").strip()
                        if compass_arrow == "No":
                                    print("You must pull out the compass before leaving the room.")

                        else:
                              inventory_zero.remove(compass)
                              break
                        
                        print("""You pull out the compass and put it next to the arrow. You notice the arrow has a magnetic pull towards the compass, 
                              and then you hear a click. The compass is fixed! You spin slowly in a circle to test the arrow's sense of direction, and find no error.
                              You gather your belongings, for you may now leave to Animal Research Base. There is nothing left for you here.""")
                        
                        travel_one = input("Are you ready? Enter in number 1) to proceed")
                        if travel_one == "1":
                              animal_research_center()

                              
      elif choice_one == "2":
            print("You have chosen to travel the longer ten mile distance, however, before you can leave, you must grab the compass first!")
            
            while(True):   
                  compass = input("Pick up Compass? Capitalize your answer.").strip() 
                          
                  if compass == "No":
                              print("You can't go anywhere without the compass!")
            
                  else:
                        inventory_zero.append(compass)
                        break 

                  print("""You have now accquired a compass! The glass front of the compass was covered with snow, so you take the sleeve of your shirt and wipe it off, that is when you notice a problem.
            The arrow inside the compass was missing. You remember that the arrow witin a compass is magnetic, and rotates directions based on the magnetic force exhibited by the Earth.
            Without that arrow, the compass will be useless. You need to find it.""")

            arrow_zero = input("Where will you check first? The cot or the floor? Please capitalize your answer.").strip()

            if arrow_zero == "Cot":
                print("""You move to the East side of the igloo. This area of the igloo is empty besides your torn backpack sitting upon the cot.
                      You pick up your backpack and see nothing. When you set down your bag you notice a shimmer to your right. 
                      You look down and see a metallic arrow interwoven in the cot's fabric.""")

            elif arrow_zero == "Floor":
                  print("""You lower yourself onto your hands and knees and start analyzing the ground. You see nothing besides the hard packed ice below you.
                        Your hands begin to go numb as you grave your hand over the ice's ridges. You still see nothing.""")
                  
                  search = input("Do you want to keep searching the floor or move on to the cot? Enter a number: 1) Keep searching the floor or 2) Search the cot instead")
                  if search == "1":
                        print("")

                  else: 
                        print("""You give up looking on the floor and make your way to the cot. You move to the East side of the igloo. 
                              This area of the igloo is empty besides your torn backpack sitting upon the cot. You pick up your backpack and see nothing.
                              When yous et down your bag you notice a shimmer to your right. You look down and see a metallic arrow interwoven in the cot's fabric.""")
                        
                  arrow = "Compass Arrow"
                  while(True):
                        arrow_one = input("Pick up the arrow? Capitalize your answer.")
                        if arrow_one == "No":
                              print("You can't advance without it!")
                        else:
                              inventory_zero.append(arrow)
                              break

                        print("""You work to unweave the arrow, and within seconds you set it free. 
                                    You hold it up to the light. It is small, with a red tip. You should pull out the compass from your bag.""")
                              
                  while(True):
                        compass_arrow = input("Pull out the compass? Capitalize your answer.").strip()
                        if compass_arrow == "No":
                                    print("You must pull out the compass before leaving the room.")

                        else:
                              inventory_zero.remove(compass)
                              break
                  
                  print("""You pull out the compass and put it next to the arrow. You notice the arrow has a magnetic pull towards the compass, 
                              and then you hear a click. The compass is fixed! You spin slowly in a circle to test the arrow's sense of direction, and find no error.
                              You gather your belongings, for you may now leave to the Abandoned Research Library. There is nothing left for you here.""")
                        
                  travel_one = input("Are you ready? Enter in number 1) to proceed")
                  if travel_one == "1":
                        abandoned_research_library()

            

#LACEY START

if introduction == 1:
      print("""You wake up in the middle of nowhere. You glance outside and notice you are in a small town in Asia. 
            You walk to the near by shops in hopes to find the so called 'wizard' who can teleport you home. 
            You have a backpack containing a half-full waterbottle and a granola bar. 
            REMINDER: Make sure to always have food and water because your health will go down if you don't!""")


      choice1as=input("You arrive at the shops tired and hungry. Do you: 1. Eat a granola bar, 2. Explore the shops, 3. Ask about the wizard PLEASE ENTER ONLY A NUMBER")
      if choice1as==("1"):
            print("you ate a granola bar. You choose to explore the shops and familiarize yourself with the area. You notice an old shop in the distance and walk towards it. ")
            item ="granola bar"
            inventory.remove("granola bar")
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
            key="key"
            keyq=input("you have found a key! Do you: 1. keep it, or 2. leave it? PLEASE ENTER ONLY A NUMBER")
            if keyq==("1"):
                  print("you chose to keep the key")
                  inventory.append(key)
                  minichoice=print("""you prepare for bed but are suddenly startled by someone trying to open the window.
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
                  pass
                  print("""you prepare for bed but are suddenly startled by someone trying to open the window.
                         You decide to walk towards the window and investigate. You look out the window and see
                        a...peanut? He asks you to let him in and he will explain himself.""")
                  minchoice=print("""you prepare for bed but are suddenly startled by someone trying to open the window.
                         You decide to walk towards the window and investigate. You look out the window and see
                        a...peanut? He asks you to let him in and he will explain himself. Do you:
                        1. hear  him out, 2. yell at him to leave? please enter only a number.""")
                  if minchoice==("1"):
                        print("""you decided to let the peanut-man inside. He explains that he
                              can help you get home IF you help him defeat the koolaide man.
                              You decide to help him so that you can return home""")
                  elif minchoice==("2"):
                        print("""the peanut-man doesn't listen and breaks the window to enter. 
                              He explains that he can get you home IF you help him defeat the koolaide man first.
                              You appoligize and agree to help him defeat the koolaide man.""")
            
      choice3as=input("""morning finally arrives. You grab your backpack and follow the peanut
                       to the temple that the koolaide man supposedly lives in. The path you're
                      one suddenly splits into two different directions. Do you: 1. go left, 2. go right? 
                      PLEASE ENTER ONLY A NUMBER""")
