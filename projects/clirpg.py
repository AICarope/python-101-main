# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.


import time

# Function to introduce the player to the game world
def intro(player_name):
    print(f"Welcome, {player_name}, to the world of adventure!")

# Function to handle the player's choice of doors
def choose_door():
    choice = input("You are in two doors. Which door do you choose? (left/right): ").lower()
    if choice == 'left':
        empty_room()
    elif choice == 'right':
        dragon_encounter()
    else:
        print("not an option. Please try again.")
        choose_door()

# Function for the empty room scenario
def empty_room():
    print("You enter the empty room.")
    time.sleep(1)
    look_around = input("would you like to look around? (yes/no): ").lower()
    if look_around == 'yes':
        print("find a sword in the corner.")
        take_sword = input("would you take the sword? (yes/no): ").lower()
        if take_sword == 'yes':
            print("take the sword and go to the previous room.")
            choose_door()
        else:
            print("leave the sword and go back to the previous room.")
            choose_door()
    else:
        print("You decide to head to the previous room.")
        choose_door()

# Function for the dragon encounter scenario
def dragon_encounter():
    print("You encounter a fierce dragon!")
    time.sleep(1)
    if 'sword' in player_inventory:
        print("You have a sword and decide to fight the dragon.")
        time.sleep(1)
        print("With the sword, you defeat the dragon. Congratulations, you win!")
    else:
        print("You don't have a sword to fight the dragon. Game over!")

# Main game logic
player_name = input("What is your name, adventurer? ")
intro(player_name)
player_inventory = []

choose_door()