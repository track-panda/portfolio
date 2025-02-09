import sys

class Game:
    def __init__(self):
        self.state = 'start'
        self.character = None
        self.sidekick = None
        self.attributes = {}
        self.inventory = []

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
        print("4. Exit game")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.state = 'choose_character'
        elif choice == '2':
            self.state = 'character_info'
        elif choice == '3':
            self.state = 'inventory'
        elif choice == '4':
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
            self.attributes = {'Strength': 10, 'Agility': 8, 'Intelligence': 7}
        elif choice == '2':
            self.character = 'Female'
            self.attributes = {'Strength': 8, 'Agility': 10, 'Intelligence': 9}
        else:
            print("Invalid choice. Try again.")
            return

        self.state = 'choose_sidekick'

    def choose_sidekick(self):
        print("Choose your sidekick:")
        print("1. Dragon")
        print("2. Fairy")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.sidekick = 'Dragon'
        elif choice == '2':
            self.sidekick = 'Fairy'
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
            print("3. Use item from inventory")
            print("4. Back to main menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_inventory()
            elif choice == '2':
                self.add_to_inventory()
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
        print("Once upon a time...")
        self.state = 'start'

    def exit_game(self):
        print("Thanks for playing! Goodbye!")
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()