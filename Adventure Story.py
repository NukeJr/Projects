class AdventureGame:
    def __init__(self):
        self.inventory = []
        self.current_location = "forest"
    
    def start(self):
        print("Welcome to the Quest for the Lost Amulet!")
        self.introduction()
    
    def introduction(self):
        print("\nYou stand at the edge of the Forest of Whispers, where many seek a powerful amulet.")
        self.first_choice()

    def first_choice(self):
        choice = input("\nWhat would you like to do? (enter '1' to enter the forest, '2' to set up camp, '3' to call out): ")
        if choice == '1':
            self.enter_forest()
        elif choice == '2':
            self.camp()
        elif choice == '3':
            self.call_out()
        else:
            print("Invalid choice. Try again.")
            self.first_choice()

    def enter_forest(self):
        print("\nYou cautiously enter the forest, surrounded by the sounds of nature.")
        self.second_choice()

    def second_choice(self):
        choice = input("\nYou hear a rustling sound. What do you do? (enter '1' to investigate, '2' to ignore, '3' to prepare your weapon): ")
        if choice == '1':
            self.investigate()
        elif choice == '2':
            self.ignore()
        elif choice == '3':
            self.prepare_weapon()
        else:
            print("Invalid choice. Try again.")
            self.second_choice()

    def investigate(self):
        print("\nYou discover a small, friendly fox.")
        self.third_choice()

    def ignore(self):
        print("\nYou decide to ignore it and move deeper into the forest.")
        self.third_choice()

    def prepare_weapon(self):
        print("\nYou prepare your weapon, ready for anything.")
        self.third_choice()

    def third_choice(self):
        choice = input("\nWhat will you do next? (enter '1' to befriend the fox, '2' to search the area, '3' to move on): ")
        if choice == '1':
            self.befriend_fox()
        elif choice == '2':
            self.search_area()
        elif choice == '3':
            self.move_on()
        else:
            print("Invalid choice. Try again.")
            self.third_choice()

    def befriend_fox(self):
        print("\nThe fox seems happy and leads you to a hidden path!")
        self.hidden_path()

    def search_area(self):
        print("\nYou find a glimmering key hidden among the leaves.")
        self.inventory.append("key")
        print("You now have a key in your inventory.")
        self.hidden_path()

    def move_on(self):
        print("\nYou decide to keep moving deeper into the forest.")
        self.hidden_path()

    def hidden_path(self):
        print("\nYou arrive at an ancient tree with a chest at its base.")
        if "key" in self.inventory:
            self.open_chest()
        else:
            self.no_key_choice()

    def open_chest(self):
        choice = input("\nDo you want to open the chest? (enter 'yes' or 'no'): ")
        if choice.lower() == 'yes':
            print("\nYou unlock the chest and find a magical gemstone!")
            print("Congratulations! You have completed your quest!")
        else:
            print("\nYou decide not to open the chest and continue your journey.")
            print("The adventure continues...")
    
    def no_key_choice(self):
        choice = input("\nThe chest is locked. What do you want to do? (enter '1' to search for a key, '2' to leave): ")
        if choice == '1':
            print("\nYou search and find the glimmering key!")
            self.inventory.append("key")
            self.open_chest()
        else:
            print("\nYou leave the ancient tree behind, but the adventure is not over!")
            print("The journey continues...")

    def camp(self):
        print("\nYou set up camp for the night and prepare for the journey ahead.")
        self.start()  # Restart the game after camping

    def call_out(self):
        print("\nYou call out, but the forest is silent.")
        self.start()  # Restart the game after calling out

# Start the game
if __name__ == "__main__":
    game = AdventureGame()
    game.start()