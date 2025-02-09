import sys
import random
import scenes
import lacey_scenes

class Game:
    def __init__(self):
        self.state = 'start'
        self.character = None
        self.sidekick = None
        self.attributes = {}
        self.inventory = [
            "Granola Bar One: Used to keep you from going hungry",
            "Granola Bar Two: Used to keep you from going hungry",
            "Canteen One: Used to keep you from going thirsty",
            "Canteen Two: Used to keep you from going thirsty",
            "Key: Vital for a later room in the game",
        ]

    def run(self):
        while True:
            if self.state == 'start':
                self.start()
            elif self.state == 'choose_character':
                self.choose_character()
            elif self.state == 'choose_sidekick':
                self.choose_sidekick()
            elif self.state == 'character_info':
                self.character_info()
            elif self.state == 'inventory':
                self.inventory_management()
            elif self.state == 'story':
                self.story()
            elif self.state == 'exit':
                self.exit_game()

    def start(self):
        print("Welcome to the Text-Based Adventure Game!")
        print("1. Choose main character")
        print("2. Learn about character")
        print("3. Manage inventory")
        print("4. Go to story")
        print("5. Exit game")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.state = 'choose_character'
        elif choice == '2':
            self.state = 'character_info'
        elif choice == '3':
            self.state = 'inventory'
        elif choice == '4':
            self.state = 'story'
        elif choice == '5':
            self.state = 'exit'
        else:
            print("Invalid choice. Try again.")

    def choose_character(self):
        print("Choose your main character:")
        print("1. Male")
        print("2. Female")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.character = 'Male'
            self.attributes = {'Name': "Devin Davis", 'Goal': "To find the wizard that will send you back home",
                               'Strengths': "strong, smart, not affected by temperatires", 'Weaknesses': "not very fast/agile, has low stamina, and is allergic to peanut butter",
                               'Physical Description': "6'0 tall, has one brown eye and one green eye, short, brown hair, is tan, and has a pink birth mark"}
        elif choice == '2':
            self.character = 'Female'
            self.attributes = {'Name': "Maisie Melite", 'Goal': "To find the wizard that will send you back home", 
                               'Strengths': "agile, smart, has high stamina", 'Weaknesses': "Not very strong, reduced stamina in cold environments, allergis to red dye",
                                'Physical Description': "5'0 tall, has blue eyes, brown wavy mide-length hair, has freckles, and is pale."}
        else:
            print("Invalid choice. Try again.")
            return

        self.state = 'choose_sidekick'

    def choose_sidekick(self):
        print("Choose your sidekick:")
        print("1. Platypus")
        print("2. Hippo")
        print("3. Frog")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.sidekick = 'Platypus'
        elif choice == '2':
            self.sidekick = 'Hippo'
        elif choice == '3':
            self.sidekick = 'Frog'
        else:
            print("Invalid choice. Try again.")
            return

        print(f"You have chosen a {self.character} character with a {self.sidekick} sidekick.")
        self.state = 'start'

    def character_info(self):
        if not self.character:
            print("You need to choose a character first.")
        else:
            print(f"Character: {self.character}")
            for attribute, value in self.attributes.items():
                print(f"{attribute}: {value}")
        self.state = 'start'

    def inventory_management(self):
        while True:
            print("Inventory Management:")
            print("1. View inventory")
            print("2. Add item to inventory")
            print("5. Remove item from inventory")
            print("3. Use item from inventory")
            print("4. Back to main menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_inventory()
            elif choice == '2':
                self.add_to_inventory()
            elif choice == '5':
                self.remove_inventory()
            elif choice == '3':
                self.use_inventory_item()
            elif choice == '4':
                self.state = 'start'
                break
            else:
                print("Invalid choice. Try again.")

    def view_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory items:")
            for item in self.inventory:
                print(f"- {item}")

    def add_to_inventory(self):
        item = input("Enter the item to add: ")
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_inventory(self):
        item = input("Enter the item to remove: ")
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} has been removed to your inventory.")
        else:
            print(f"Item {item} not found.")

    def use_inventory_item(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return

        item = input("Enter the item to use: ")
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You have used {item}.")
        else:
            print(f"{item} is not in your inventory.")

    def story(self):
            print("Story mode")
            scenes_path = random.randrange(2)
            if scenes_path:
                lacey_scenes.lacey()
            else:
                scenes.scene_one_em()
        
    
    def combat(self):
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

    def exit_game(self):
        print("Thanks for playing! Goodbye!")
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()




      