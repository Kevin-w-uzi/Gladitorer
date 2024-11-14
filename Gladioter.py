import random

# Välkomstmeddelande
print("Välkommen till Piazza del Colosseo i vår fina stad Roma. Du ska snart ut i solen och den heta sanden och slås för ditt liv framför en bloodtörstig publik.")

# Spelkaraktärens hälsa
gladiator_health = 100
enemy_health = 100

# Spelens attacker
attacks = ["Hugg", "Slå", "Spjut"]

# Spel-loop
while gladiator_health > 0 and enemy_health > 0:
    print(f"\nGladiator hälsa: {gladiator_health}")
    print(f"Fiende hälsa: {enemy_health}")
    
    # Fråga användaren om vilken attack de vill använda
    print("\nVälj din attack:")
    for i, attack in enumerate(attacks, 1):
        print(f"{i}. {attack}")
    
    user_choice = int(input("\nAnge numret för din attack: ")) - 1
    
    # Kontrollera att användaren valde en giltig attack
    if user_choice < 0 or user_choice >= len(attacks):
        print("Ogiltigt val, du förlorade din tur!")
        continue
    
    gladiator_attack = attacks[user_choice]
    print(f"Du valde attack: {gladiator_attack}")
    
    # Fiendens drag (slumpas fortfarande)
    enemy_attack = random.choice(attacks)
    print(f"Fiendens attack: {enemy_attack}")
    
    # Skada som gjorts
    gladiator_damage = random.randint(10, 20)
    enemy_damage = random.randint(10, 20)
    
    # Uppdatera hälsan
    if gladiator_attack == "Hugg":
        enemy_health -= gladiator_damage
    elif gladiator_attack == "Slå":
        enemy_health -= gladiator_damage
    elif gladiator_attack == "Spjut":
        enemy_health -= gladiator_damage

    if enemy_attack == "Hugg":
        gladiator_health -= enemy_damage
    elif enemy_attack == "Slå":
        gladiator_health -= enemy_damage
    elif enemy_attack == "Spjut":
        gladiator_health -= enemy_damage

    # Kontrollera om någon är död
    if gladiator_health <= 0:
        print("\nGladiatorn förlorade!")
        break
    elif enemy_health <= 0:
        print("\nFienden förlorade!")
        break
