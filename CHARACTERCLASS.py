
class Character:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k):
        self.name = a
        self.cool_nickname = b
        self.height = c
        self.weight = d
        self.attack_one = e
        self.attack_two = f
        self.attack_three = g
        self.weakness_one = h
        self.weakness_two = i
        self.health = j
        self.level = k

    def character_name(self):
            return self.name
        
    def character_nickname(self):
            return self.cool_nickname

    def character_height(self):
          return self.height
    
    def character_weight(self):
          return self.weight
    
    def character_attack_one(self):
          return self.attack_one
    
    def character_attack_two(self):
          return self.attack_two
    
    def character_attack_three(self):
          return self.attack_three
    
    def character_weakness_one(self):
          return self.weakness_one
    
    def character_weakness_two(self):
          return self.weakness_two
    
    def character_health(self):
          return self.health

    def character_level(self): 
          return self.level
    

character = Character("Rosalia Wilson", "Ruby Roundhouse", "5'10", "175lbs", "Jump Split Kick", "Nunchucks", "Posionous Kiss", "Cake", "Rainforest", "75", "15")
print(character.character_name())
print(character.character_nickname())
print(character.character_height())
print(character.character_weight())
print(character.character_attack_one())
print(character.character_attack_two())
print(character.character_attack_three())
print(character.character_weakness_one())
print(character.character_weakness_two())
print(character.character_health())
print(character.character_level())