# File: RPG.py
#  Description: The goal is to simulate a simple RPG game.

#Weapon class is defined
class Weapon: 

    # constructor is created & valid weapon states initialized
    def __init__(self, kind):
        #setting instance variable & configuring its damage
        self.kind = kind
        if kind == "dagger": 
            self.damage = 4
        if kind == "axe":
            self.damage = 6
        if kind == "staff":
            self.damage = 6
        if kind == "sword": 
            self.damage = 10
        if kind == "none":
            self.damage = 1

    #overrides predefined method, converts weapon obj into str
    def __str__(self):
        return(self.kind)


#Armor class is defined
class Armor: 

    # constructor is created & valid armor states are initialized
    def __init__(self, kind):
        #setting instance variable & configuring its AC
        self.kind = kind
        if kind == "plate": 
            self.AC = 2
        if kind == "chain":
            self.AC = 5
        if kind == "leather":
            self.AC = 8
        if kind == "none":
            self.AC = 10

    #overrides predefined method, converts armor obj into str
    def __str__(self):      
        return(self.kind)


#Character class is defined
class RPGCharacter: 

    #method show is created to show character stats
    def show(self):
        print() 
        print(" ", self.name, sep = "")
        print("   Current Health:", self.health)
        print("   Current Spell Points:", self.spellPts)
        print("   Wielding:", self.weapon)
        print("   Wearing:", self.armor)
        print("   Armor Class:", self.AC)
        print()

    #method wield is defined
    def wield(self, weaponType): 
        #check if new weapon is valid and replaces if so 
        if weaponType.kind in self.validWeapon: 
            self.weapon = weaponType
            print(self.name, "is now wielding a(n)", weaponType.kind) 
        else: 
            print("Weapon not allowed for this character class.")

    #method unwield is defined
    def unWield(self, weaponType): 
        #character's current weapon is set to none
        currentWeapon = Weapon("none")
        print(self.name, "is no longer wielding anything.")
    
    #defines putOnArmor method
    def putOnArmor(self, armorType): 
        #checks if new armor is valid and replaces if so
        if armorType.kind in self.validArmor:
            self.armor = armorType
            self.AC = armorType.AC
            print(self.name, "is now wearing", armorType.kind)
        else: 
            print("Armor not allowed for this character class.")

    #defines takeOffArmor method
    def takeOffArmor(self, armorType): 
        self.armor = Armor("none")
        self.AC = 10 
        print(self.name, "is no longer wearing anything.")

    #defines fight method, two characters fight
    def fight(self, opponentName): 
        currentWeapon = self.weapon
        print(self.name, "attacks", opponentName.name, "with a(n)", self.weapon)
        opponentName.health -= currentWeapon.damage
        print(self.name, "does", currentWeapon.damage, "damage to", opponentName.name)
        print(opponentName.name, "is now down to", opponentName.health, "health")

        #checks to see if opponent is defeated from weapon attacks
        if opponentName.checkForDefeat(): 
            print(opponentName.name, "has been defeated!")

    #method is defined to check is character has been defeated
    def checkForDefeat(self):
        if self.health <= 0: 
            return True 


#Fighter subclass is defined
class Fighter(RPGCharacter): 
    #starting stats 
    maxHealth = 40
    maxSpellPts = 0 
    #allotted equipment
    validWeapon = ("dagger", "axe", "staff", "sword", "none")
    validArmor = ("plate", "chain", "leather", "none")

    # constructor & default states (dynamic) are initialized
    def __init__(self, name): 
        self.name = name
        self.health = self.maxHealth
        self.spellPts = self.maxSpellPts
        self.weapon = Weapon("none")
        self.armor = Armor("none")
        self.AC = 10


#Wizard subclass is defined
class Wizard(RPGCharacter): 
    #starting stats 
    maxHealth = 16
    maxSpellPts = 20
    #allotted equipment
    validWeapon = ("dagger", "staff", "none")
    validArmor = ("none")

    # constructor & default states (dynamic) are initialized
    def __init__(self, name): 
        self.name = name
        self.health = self.maxHealth
        self.spellPts = self.maxSpellPts
        self.weapon = Weapon("none")
        self.armor = Armor("none")
        self.AC = 10

    #subclass wizard specific method defined to implement spells 
    def castSpell(self, spellName, target): 
        spell = ("Fireball", "Lightning Bolt", "Heal")

        #valid spells
        if spellName == "Fireball":
            cost = 3
            effect = 5

        if spellName == "Lightning Bolt": 
            cost = 10 
            effect = 10

        if spellName == "Heal": 
            cost = 6
            effect = -6

        #checks if spells are known 
        if spellName not in spell: 
            print("Unknown spell name. Spell failed.")
            return

        #checks if sufficient spell points to cast the spell
        if self.spellPts < cost: 
            print("Insufficient spell points")
            return
        
        #the adverse effects on the target based on the spell
        print(self.name, "casts", spellName, "at", target.name)
        self.spellPts -= cost
        target.health -= effect

        #case of heal spell
        if spellName == "Heal": 
            #case of over max health
            if target.health > target.maxHealth: 
                target.health += effect
                print(self.name, "heals", target.name, "for", target.maxHealth - target.health, "health points")
                target.health = target.maxHealth
            #case of standard heal
            else: 
                print(self.name, "heals", target.name, "for", abs(effect), "health points")
                
            print(target.name, "is now at", target.health, "health")

        #case of damaging spell
        else: 
            print(self.name, "does", effect, "damage to", target.name)
            print(target.name, "is now down to", target.health, "health")

        #checks to see if target is defeated by spell damage
        if target.checkForDefeat():
            print(target.name, "has been defeated!")

# main function 
def main():

    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    harry = Wizard("Harry Potter")
    harry.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    
    harry.show()
    aragorn.show()

    harry.castSpell("Fireball",aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

    harry.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    harry.show()
    aragorn.show()

    harry.castSpell("Heal",harry)
    aragorn.fight(harry)

    harry.fight(aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

main()