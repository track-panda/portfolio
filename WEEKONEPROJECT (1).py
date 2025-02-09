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
      print("""This is where the journey begins. The igloo is small with remnants of human life evident, 
            for valuables were left behind. You see a light blue cod with a shriveled up blanket on one side, 
            and a desk with what appears to be a broken compass and a torn map.
            There are no windows, but that keeps the little warmth from escaping 
            and keeps the bitter cold from creeping inside. """)
def animal_research_center():
      print("""This is the destination that the character will travel to if they decide on the four-mile journey. 
            The facility is modern with marble floors and steel fixtures and cages. There are cages of penguins everywhere 
            staring at them as they walk by. This place reeks of fish and a weird odor. 
            The wall has a mysterious latch and a foul odor reeks from behind it.""")
def cavern():
      print("""The cavern is dark and cold water drips from the icicles above. 
            There are abandoned lanterns for the character to use, but they require a match. 
            There seems to be nothing here, but then there appears to be a wooden plank poking out from the ice.""")  
def abandoned_research_library():
      print("""This destination is where the character will travel if they choose the grueling ten-mile journey. 
            This place has vaulted ceilings, shelves, and shelves of maps, scrolls, books, etc. 
            Papers are askew all over the floor, lit by the grand chandelier. Feels as though someone has been here.""")     
def underground_tunnel_system(): 
      print("""This area can explore the true depths of the icy tundra. 
            It is unknown what places this system can take you to, but the risks may be great.
             Are there people here? How can one get here?""")

#ASIA ROOMS



#GAME CODE STARTS HERE

character_type = input("""Welcome to the game Finding My Way Home. Would you rather be the Female character or the Male character? Please capitalize your answer.""").strip()

person: Person
if character_type == "Female":
     person = Person("Your character's name is Maisie Melite", "Your character's goal is to find the great wizard", "Your character is the main character", "Your character is allies with the Hippo.", "Your character is fast/agile, smart and has a high stamina", "Your character is not very strong, has reduced stamina in colder environments, and is allergic to red dye", "Your character is 5'0 tall, has blue eyes, brown wavy mide-length hair, has freckles, and is pale.")
else:
     person =  Person("Your character's name is Devin Davis", "Your character's goal is to find the great wizard of Bartholomew Richard Fitzgerald-Smythe (The Peanut Man)", "Your character is the main character", "Your character is allies with the Hippo.", "Your character is strong, smart, and not affected by temperature", "Your character is not very fast/agile, has low stamina, and is allergic to peanut butter", "Your character is 6'0 tall, has one brown eye and one green eye, short, brown hair, is tan, and has a pink birth mark.") 

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
            print(input("You have chosen a character! Enter a letter A thru G to find out important information about your new character.").strip())
            
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

others = input("""Well done on choosing your new side character! 
               To make the game more mysterious, two of the characters and their traits will 
               not be revealed until applicable in the game. Have fun!""")


#EMERSON START

if introduction == 0:
      print("""You awake outside of an igloo, surrounded by a thick blanket of snow that hides any 
            indication of civilization and no recollection of what happened. 
            The winds are fierce almost knocking you over several times, but you sneak your way inside the igloo.""") 
      igloo()
         
      print("""You set your belongings on the cot and analyze the map. You notice the map is missing the entire upper right corner, however, to your luck, the map is still legible. 
            The map indicates that you are near the southwestern border of Antarctica, 4 miles east of a research base, 
            and 10 miles south of a differnet research base. There is a note on the bottom of the map that notes limited supplies in the 
            Animal Research Center base 4 miles from you.The map also notes that the base ten miles away is the Research Library Base. You are forced to make a choice. 
            Travel four miles to the nearest base but risk finding no supplies, or traveling ten miles north and risk dying in the cold in pursuit of knowledge.""")

      choice_one = input("What will you chose? Option One: Travel to the Animal Research base 4 miles away. Option Two: Travel to the Research Library base 10 miles away.").strip()

      if choice_one == "1":
            print("You have chosen to travel the shorter four mile distance to the Animal Research base, however, before you can leave you must grab the compass first!")

            print("""The glass front of the compass was covered with snow, so you take the sleeve of your shirt and wipe it off, that is when you notice a problem.
            The arrow inside the compass was missing. You remember that the arrow witin a compass is magnetic, and rotates directions based on the magnetic force exhibited by the Earth.
            Without that arrow, the compass will be useless.""")


      elif choice_one == "2":
            print("You have chosen to travel the longer ten mile distance, however, before you can leave, you must grab the compass first!")


#LACEY START

if introduction == 1:
      print("""You wake up in the middle of nowhere. You glance outside and notice you are in a small town in Asia. 
            You walk to the near by shops in hopes to find the so called 'wizard' who can teleport you home. 
            You have a backpack containing a half-full waterbottle, a compass, and 2 granola bars. 
            REMINDER: Make sure to always have food and water because your helth will go down if you don't!""")


      choice1as=input("You arrive at the shops tired and hungry. Do you: 1. Eat a granola bar, 2. Explore the shops, 3. Ask about the wizard PLEASE ENTER ONLY A NUMBER")
      if choice1as==("1"):
            print("you ate a granola bar. You are at full health.")
      elif choice1as==("2"):
            print("you chose to explore the shops. Your health decreased slightly since you chose not to eat.")
      elif choice1as==("3"):
            print("you chose to ask about the wizard. The people thought you were crazy. Your health decreased slighly since you chose not to eat.")
      else:
            print("invalid response. please try again!")



