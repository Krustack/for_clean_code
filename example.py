def create_character(name, health, damage):
    return {'name': name, 'health': health, 'damage': damage, 'defense': 0}

def is_alive(character):
    return character['health'] > 0

def attack(attacker, defender):
    if is_alive(defender):
        damage_dealt = max(0, attacker['damage'] - defender['defense'])
        defender['health'] -= damage_dealt
        print(f"{attacker['name']} attacks {defender['name']} for {damage_dealt} damage.")
        defender['defense'] = 0
    else:
        print(f"{defender['name']} has already been defeated.")

def defend(character):
    character['defense'] = 10
    print(f"{character['name']} is defending.")

def heal(character):
    character['health'] += 15
    if character['health'] > 100:
        character['health'] = 100
    print(f"{character['name']} heals. Current health: {character['health']}.")


def game():
    player = create_character("Player", 100, 20)
    dragon = create_character("dragon", 100, 15)
    print("Welcome to the dragon slayer game!") #can change to your game name
    while is_alive(player) and is_alive(dragon):
        print(f"\n{player['name']}'s Health: {player['health']}, {dragon['name']}'s Health: {dragon['health']}")
        player_choice = input("Enter 1 to attack\nEnter 2 to defend \nEnter 3 to heal\nplease enter 1 - 3 for play!: ")
        if player_choice == "1":
            attack(player, dragon)
        elif player_choice == "2":
            defend(player)
        elif player_choice == "3":
            heal(player)
        else:
            print("Invalid choice. You lose your turn.")
        
        if is_alive(dragon):
            import random
            npc_choice = random.choice(["1", "2", "3"])
            if npc_choice == "1":
                attack(dragon, player)
            elif npc_choice == "2":
                defend(dragon)
            elif npc_choice == "3":
                heal(dragon)

    if is_alive(player):
        print("\nPlayer wins!")
    else:
        print("\nDragon wins!")

game()
