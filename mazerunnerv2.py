import random

SAVE_FILE = "game_save.txt"

health = 0
shovel = 0
sword = 0
potion = 0
point = 0

def store():
    global shovel, sword, potion, point, health
    while True:
        print("\n🛒 You have enough points to gain access to the store.")
        print("1. ⚔️ Sword (5 Points)\n2. 🧪 Potion (5 Points)\n3. ❤️ Health (10 Points)\n4. ⛏️ Shovel (5 Points)\n5. 🚪 Exit")
        choice = input("What would you like to buy? [1/2/3/4/5]:")
        if choice == "1":
            if point >= 5:
                point -= 5
                sword += 1
                print(f"You purchased a ⚔️ sword. Now you have {sword} swords!")
                display_stats()
            else:
                print("❌ You do not have enough points.")
        elif choice == "2":
            if point >= 5:
                point -= 5
                potion += 1
                print(f"You purchased a 🧪 potion. Now you have {potion} potions!")
                display_stats()
            else:
                print("❌ You do not have enough points.")
        elif choice == "3":
            if point >= 10:
                point -= 10
                health += 1
                print(f"You purchased a ❤️ health booster. Now you have {health} healths!")
                display_stats()
            else:
                print("❌ You do not have enough points.")
        elif choice == "4":
            if point >= 5:
                point -= 5
                shovel += 1
                print(f"You purchased a ⛏️ shovel. Now you have {shovel} shovels!")
                display_stats()
            else:
                print("❌ You do not have enough points.")
        elif choice == "5":
            print("🚪 Exiting store...")
            break
        else:
            print("❌ Incorrect Input")

def character_choice():
    global shovel, sword, potion, point, health
    print("\n--- Character Choice ---")
    print("1. Warrior: +2 Swords⚔️\n2. Alchemist: +2 Potions🧪\n3. Durable: +2 Healths❤️\n4. Treasure Hunter: + 2 Shovels⛏️  \n 5. Point Madness: +5 Points⭐")
    choice = int(input("Choose your character[1/2/3/4/5]:"))

    if choice == 1:
        sword += 2
        print(f"You got 2 extra swords⚔️. Now you have {sword} swords. ")
    elif choice == 2:
        potion += 2
        print(f"You got 2 extra potions🧪. Now you have {potion} potions. ")
    elif choice == 3:
        health +=2
        print(f"You got 2 extra healths❤️. Now you have {health} healths. ")
    elif choice == 4:
        shovel += 2
        print(f"You got 2 extra shovels⛏️. Now you have {shovel} shovels. ")
    elif choice == 5:
        point += 5
        print(f"You got 5 extra points⭐. Now you have {point} points. ")
    else:
        print("❌Incorrect Input.")


def display_stats():
    global sword, potion, point, health, shovel
    print("\n📜 --- Player Stats ---")
    print(f"⚔️ Swords: {sword}, 🧪 Potions: {potion}, ❤️ Health: {health}, ⭐ Points: {point}, ⛏️ Shovels: {shovel}")
    print("--------------------\n")

def choose_difficulty():
    global shovel, sword, potion, point, health

    print("----Choose Difficulty----")
    print("Easy: 5 Swords⚔️ / 5 Potions🧪 / 2 Shovels⛏️ / 5 Health❤️ /")
    print("Medium: 3 Swords⚔️ / 3 Potions🧪 / 1 Shovels⛏️ / 3 Health❤️ /")
    print("Hard: 2 Swords⚔️ / 2 Potions🧪 / 0 Shovels⛏️ / 2 Health❤️ /")
    print("Impossible: 1 Swords⚔️ / 1 Potions🧪 / 1 Shovels⛏️ / 1 Health❤️ /")
    diff = input("Your answer: ")
    diff = diff.lower()
    diff = diff.strip()

    if diff == "easy":
        shovel += 2
        sword += 5
        potion += 5
        health += 5
        display_stats()

    elif diff == "medium":
        shovel += 1
        sword += 3
        potion += 3
        health += 3
        display_stats()

    elif diff == "hard":
        sword += 2
        potion += 2
        health += 2
        display_stats()

    elif diff == "impossible":
        shovel += 1
        health += 1
        potion += 1
        sword += 1
        display_stats()

    else:
        print("Incorrect Input")

    return shovel,sword,potion,point,health


def monster_battle():
    global sword, point, health
    monster_health = random.randint(2, 4)
    player_stamina = random.randint(health, health + 3)
    print(f"\n👹 A monster appeared! It has {monster_health} health.")
    while monster_health > 0 and player_stamina > 0:
        print("\n⚔️ --- Battle Options ---")
        print("1. ⚔️ Attack with sword")
        print("2. 🏃 Try to flee")
        choice = input("Choose your action [1/2]: ")
        if choice == "1":
            if sword > 0:
                player_attack = random.randint(1, 6)
                monster_attack = random.randint(1, 6)
                if player_attack >= 3:
                    monster_health -= 1
                    print(f"⚔️ You hit the monster! Its health is now {monster_health}.")
                else:
                    print("❌ You missed your attack!")
                if monster_health > 0 and monster_attack > 3:
                    player_stamina -= 1
                    print(f"💥 The monster attacked! Your stamina is now {player_stamina}.")
                elif monster_health > 0 and monster_attack <= 4:
                    print("👀 The monster missed its attack!")
            else:
                print("❌ You have no swords left! You cannot attack!")
        elif choice == "2":
            flee_chance = random.randint(1, 5)
            if flee_chance > 3:
                print("🏃 You successfully fled the battle!")
                break
            else:
                player_stamina -= 1
                print(f"❌ You failed to escape! Your stamina is now {player_stamina}. The battle continues.")
        else:
            print("❌ Invalid input. Choose again.")
    if monster_health <= 0:
        print("🎉 You defeated the monster and earned 3 ⭐ points!")
        sword -= 1
        point += 3
    elif player_stamina <= 0:
        print("💀 You have been defeated! You can continue your journey.")
        sword -= 1
        point -= 1

def final_boss():
    global sword, point, health

    monster_health = random.randint(5, 11)
    player_stamina = random.randint(health, health + 3)

    print(f"🔥 The final boss is here! It has {monster_health} health. ⚔️")

    while monster_health > 0 and player_stamina > 0:
        print("\n⚔️ --- Battle Options --- ⚔️")
        print("1️⃣ Attack with sword 🗡️")
        print("2️⃣ Try to flee 🏃")
        choice = input("Choose your action [1/2]: ")

        if choice == "1":
            if sword > 0:
                player_attack = random.randint(1, 6)
                monster_attack = random.randint(1, 6)

                if player_attack > 3:
                    monster_health -= 1
                    print(f"💥 You hit the monster with your sword! Its health is now {monster_health}.")
                else:
                    print("❌ You missed your attack!")

                if monster_health > 0 and monster_attack >= 3:
                    player_stamina -= 1
                    print(f"😵 The monster attacked you! Your stamina dropped to {player_stamina}.")
                elif monster_health > 0 and monster_attack <= 4:
                    print("👀 The monster missed its attack!")
            else:
                print("❌ You have no swords left! You cannot attack!")

        elif choice == "2":
            flee_chance = random.randint(1, 5)
            if flee_chance > 3:
                print("🏃💨 You successfully fled the battle!")
                break
            else:
                player_stamina -= 1
                print(f"⚠️ You failed to escape but your stamina dropped to {player_stamina}! The battle continues.")

        else:
            print("❌ Invalid input. Choose again.")

    if monster_health <= 0:
        print("🎉 You defeated the monster and earned 3 points! 🏆")
        sword -= 1
        point += 3
    elif player_stamina <= 0:
        print("💀 You have been defeated! Game Over! 💀")
        exit()

def poison_fight():
    global health, point, potion
    print("☠️ A poison trap!")
    if potion != 0:
        print("🧪 You used a potion and gained 1 ⭐ point.")
        potion -= 1
        point += 1
        display_stats()
    else:
        if health != 0:
            print("💀 The poison is taking your health away! You lost 1 ❤️ health.")
            health -= 1
            display_stats()
        else:
            print("☠️ You died!")
            print(f"🏆 Total points: {point}")
            display_stats()


def check_game_end():
    global point, health

    while True:

        if point >= 50:
            print("🎉 You found the exit of the maze! 🏆")
            print("1️⃣ Escape with a chance of 50%! 🎲")
            print("2️⃣ Stay and Fight the Final Boss 💀 (Hard Ending)")
            print("3️⃣ Search for Hidden Treasure and Escape 💰 (Risky but Rewarding)")

            choice = input("🤔 What do you choose? [1️⃣/2️⃣/3️⃣]: ")

            if choice == "1":
                if random.randint(1, 5) > 2:
                    game_end_screen("🏆 WIN 🎉", point)

                else:
                    point -= 25
                    print("🚪 You couldn't get out of the maze and lost ❌ 25 points!")
                    break

            elif choice == "2":
                print("⚔️ You chose to fight the Final Boss! 💀🔥")
                final_boss()


            elif choice == "3":
                if random.randint(1, 5) == 1:

                    print("💎 You found a great treasure and gained ➕30 points!")
                    print("🎊 You escaped the maze safely! Congratulations! 🎊")

                    point += 30
                    game_end_screen("🏆 WIN 🎉", point)
                    exit()

                else:
                    print("🚨 It was a trap! 💀 You lost half your health and points! ❌")

                    health = health / 2
                    point -= 25
                    display_stats()
                    break

            else:
                print("❌ Invalid choice. Try again! 🚫")

        elif health <= 0:

            game_end_screen("💀 LOSE ❌", point)


def game_end_screen(result, points):
    print("\n" + "=" * 30)
    if result == "🏆 WIN 🎉":
        print("🎉 CONGRATULATIONS! YOU ESCAPED THE MAZE! 🎉")
    else:
        print("💀 GAME OVER! YOU DIDN'T SURVIVE THE MAZE! 💀")
    print(f"🏆 Final Score: {points} points")
    print("=" * 30 + "\n")
    input("Press Enter to exit...")
    exit()


def main_menu():
    while True:
        print("🎮 ---Main Menu--- 🕹️")
        print("1️⃣ New Game 🌟")
        print("2️⃣ Load Game 💾")
        print("3️⃣ Save 💾✅")
        print("4️⃣ Quit ❌")

        choice = int(input("📌 Choose an option [1️⃣/2️⃣/3️⃣/4️⃣]: "))

        if choice == 1:
            choose_difficulty()
            character_choice()

            print("👀 You opened your eyes in a mysterious maze!!!! 🌀")
            break

        elif choice == 2:

            if load_game():
                print("✅ Game loaded successfully. 🎯")
                break

        elif choice == 3:
            save_game()
            print("💾 Successfully saved. ✅")

        elif choice == 4:
            print("🚪 Quitting... 👋")
            exit()

        else:
            print("⚠️ Incorrect Input. Please Try Again. 🔄")
            continue

def load_game():
    global shovel,sword,point,potion, health

    try:
        with open(SAVE_FILE, "r") as file:
            data = file.read().strip().split(',')
            health, shovel, sword, potion, point = map(int, data)
    except FileNotFoundError:
        print("The file could not be found. ❌ Game didn't load successfully.")
        return False

    return True



def save_game():
    global health, point, sword, shovel, potion
    game = open(SAVE_FILE, "w")
    game.write(f"{health},{shovel}, {sword},{potion},{point}")

main_menu()


while True:

    if point >= 50:
        check_game_end()

    monster, poison, treasure = random.choice("LRUD"), random.choice("LRUD"), random.choice("LRUD")
    userChoice = input("🗺️ Where to go? ➡️ Left (L) 🔄 Right (R) ⬆️ Up (U) ⬇️ Down (D) 🏪 Store (S) (min 🔟 points) 📜 Main Menu (M): ")

    if userChoice not in ["L", "R" , "U" ,"D","S","M"]:
        print("⚠️ Incorrect Input. Try Again 🔄")
        continue


    elif userChoice == monster:
        monster_battle()


    elif userChoice == poison:
        poison_fight()


    elif userChoice == treasure:
        print("🎁 A treasure! 💰")

        if shovel != 0:
            print("⛏️ You used your shovel to dig up the treasure and gained ➕3 points.")
            shovel -= 1
            print(f"🛠️ Now you have {shovel} shovels.")
            point += 3
            print(f"⭐ Current point: {point}")
            display_stats()

        else:
            print("❌ You couldn't get the treasure.")
            continue


    elif userChoice == "S":

        if point >= 10:
            print("🛒 Entering the store...")
            store()

        else:
            print("❌ You do not have enough points.")
            continue



    elif userChoice == "M":
        print("📜 Returning to Main Menu...")
        main_menu()
        continue


    else:
        print("🚶‍♂️ You faced nothing. Moving on... ⏭️")
        continue