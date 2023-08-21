# races.py

class Race:
    def __init__(self, name, ability_bonuses):
        self.name = name
        self.ability_bonuses = ability_bonuses
        # Add other race-specific attributes and methods as needed

# Define race-specific data
races_data = [
    Race(name="Elf", ability_bonuses={"Dexterity": 2, "Intelligence": 1}),
    Race(name="Dwarf", ability_bonuses={"Constitution": 2, "Wisdom": 1}),
    Race(name="Human", ability_bonuses={"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1}),
    # Add more race data as needed
]


