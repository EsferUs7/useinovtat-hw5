class Warrior:
    max_exp = 10000
    max_lvl = 100
    next_lvl = 100
    correct_lvl = range(1, 101)
    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master",
             "Greatest"]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []

    def solo_leveling(self, new_exp):
        self.level += (self.experience % 100 + new_exp) // self.next_lvl
        if self.level >= self.max_lvl:
            self.level = self.max_lvl
        self.experience += new_exp
        if self.experience >= self.max_exp:
            self.experience = self.max_exp
        self.rank = self.ranks[self.level // 10]

    def training(self, array):
        if self.level >= array[2]:
            self.achievements.append(array[0])
            self.solo_leveling(array[1])
            return array[0]
        return "Not strong enough"

    def result(self, args):
        diff = self.level - args
        if diff == 0:
            self.solo_leveling(10)
            return "A good fight"
        elif diff == 1:
            self.solo_leveling(5)
            return "A good fight"
        elif diff > 1:
            return "Easy fight"
        elif diff < 0:
            if diff <= -5 and self.level // 10 < args // 10:
                return "You've been defeated"
            else:
                self.solo_leveling(20 * diff * diff)
                return "An intense fight"

    def battle(self, enemy_lvl):
        if enemy_lvl in self.correct_lvl:
            return self.result(enemy_lvl)
        return "Invalid level"
