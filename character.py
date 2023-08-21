import random

class DnDCharacter:
    def apply_race_bonuses(self):
        if self.race == "Human":
            pass  # Humans typically don't have racial ability score bonuses
        elif self.race == "Elf":
            self.abilities["Dexterity"] += 2
            self.abilities["Intelligence"] += 1
        elif self.race == "Dwarf":
            self.abilities["Constitution"] += 2
            self.abilities["Wisdom"] += 1
    
    def apply_subrace_bonuses(self):
        pass # Code these in future

    def apply_class_ability_scores(self):
        class_ability_rankings = {
            "Fighter": ["Strength", "Constitution", "Dexterity", "Wisdom", "Intelligence", "Charisma"],
            "Wizard": ["Intelligence", "Constitution", "Dexterity", "Wisdom", "Strength", "Charisma"],
            "Rogue": ["Dexterity", "Constitution", "Intelligence", "Wisdom", "Strength", "Charisma"]
            # Add more class-ability rankings as needed
        }
        
        ability_ranking = class_ability_rankings.get(self.character_class)
        if ability_ranking:
            rolled_scores = sorted(list(self.abilities.values()), reverse=True)  # Sort scores in descending order
            for ability in ability_ranking:
                self.abilities[ability] = rolled_scores.pop(0)  # Assign the highest score to the ranked ability


    def __init__(self, name, race, character_class):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = 1
        self.hp = self.roll_hit_points()
        self.abilities = self.roll_ability_scores()
        self.apply_class_ability_scores()  # Apply class-specific ability score adjustments
        self.apply_race_bonuses()
        self.apply_subrace_bonuses() # Need to code these bonuses

    def roll_hit_points(self):
        hit_dice = {
            "Fighter": 10,   # Fighter uses a d10 hit dice
            "Wizard": 6,     # Wizard uses a d6 hit dice
            "Rogue": 8       # Rogue uses a d8 hit dice
            # Add more classes and hit dice as needed
        }
        
        hit_dice_value = hit_dice.get(self.character_class)
        if hit_dice_value:
            if self.level == 1:
                hit_points = hit_dice_value + random.randint(1, hit_dice_value)
                return hit_points
            else:
                hit_points = random.randint(1, hit_dice_value)
                return hit_points
        else:
            return 0  # Default hit points if class is not recognized

    def roll_ability_scores(self):
        abilities = {
            "Strength": self.roll_ability_score(),
            "Dexterity": self.roll_ability_score(),
            "Constitution": self.roll_ability_score(),
            "Intelligence": self.roll_ability_score(),
            "Wisdom": self.roll_ability_score(),
            "Charisma": self.roll_ability_score()
        }
        return abilities

    def roll_ability_score(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]  # Roll 4d6
        dice_rolls.sort()
        ability_score = sum(dice_rolls[1:])  # Take the highest 3 rolls
        return ability_score

    def __str__(self):
        ability_str = "\n".join(f"{ability}: {score}" for ability, score in self.abilities.items())
        return f"{self.name} - Level {self.level} {self.race} {self.character_class}\n" \
               f"HP: {self.hp}\n\nAbility Scores:\n{ability_str}"
    
    def level_up(self):
        self.level += 1
        self.hp += self.roll_hit_points()
        print(f"{self.name} leveled up to level {self.level}!")

# Define races and classes
races = ["Human", "Elf", "Dwarf"]
classes = ["Fighter", "Wizard", "Rogue"]


'''
# Create a character
name = input("Enter character name: ")
race = input("Select a race (Human, Elf, Dwarf): ")
character_class = input("Select a class (Fighter, Wizard, Rogue): ")

if race not in races or character_class not in classes:
    print("Invalid race or class selected.")
else:
    new_character = DnDCharacter(name, race, character_class)
    print("\nCharacter created:\n")
    print(new_character)
    new_character.level_up()
    print(f"Character after level up:\n{new_character}")
    '''
