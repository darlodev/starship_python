

class Character():
    def __init__(self, title, name, race, strength, intelligence, dexterity):
    # MAIN
        self.title = title
        self.name = name
        self.race = race
    # SKILLS
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
    #TODO - decide on race names and characteristics
        if race == "race1":
            self.strength += 1
        elif race == "race2":
            self.intelligence += 1
        elif race == "race3":
            self.dexterity =+ 1
        else:
            print("ISSUE: 'race' is non-existent.\n")