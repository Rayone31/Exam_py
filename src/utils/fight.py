type_avantages = {
    "Feu": {"Plante": 1.5, "Eau": 0.75},
    "Eau": {"Feu": 1.5, "Plante": 0.75},
    "Plante": {"Eau": 1.5, "Feu": 0.75}
}

## This function calculates the damage dealt by the attacker to the defender
def calculate_damage(attacker, defender):
    damage_multiplier = type_avantages.get(attacker.type, {}).get(defender.type, 1)
    return attacker.attack * damage_multiplier

## This function calculates the damage dealt by the attacker to the defender
def attack(pokemon, opponent):
    damage_to_opponent = calculate_damage(pokemon, opponent)
    damage_to_pokemon = opponent.attack
    opponent.health -= damage_to_opponent
    pokemon.health -= damage_to_pokemon
    return damage_to_opponent, damage_to_pokemon

## This function calculates the damage dealt by the attacker to the defender
def defend(pokemon, opponent):
    damage_multiplier = type_avantages.get(opponent.type, {}).get(pokemon.type, 1)
    if pokemon.defense > 0:
        damage_to_pokemon_defense = min(opponent.attack * damage_multiplier, pokemon.defense)
        pokemon.defense -= damage_to_pokemon_defense
        return damage_to_pokemon_defense, 0
    else:
        damage_to_pokemon = opponent.attack * damage_multiplier
        pokemon.health -= damage_to_pokemon
        return 0, damage_to_pokemon
    
## This function uses a potion to heal the pokemon
def use_potion(pokemon, potion_name):
    if potion_name == "Petite Potion":
        pokemon.health = min(pokemon.health + 20, pokemon.healthmax)
    elif potion_name == "Moyenne Potion":
        pokemon.health = min(pokemon.health + 50, pokemon.healthmax)
    elif potion_name == "Grande Potion":
        pokemon.health = min(pokemon.health + 100, pokemon.healthmax)
    elif potion_name == "Potion Max":
        pokemon.health = pokemon.healthmax
    elif potion_name == "Antidote":
        pokemon.condition = "Normal"