class Game(object):
    
    def __init__(self):
        pass
        
    def player_name(self, name):
        self.name = name
        return self.name


    def get_computer_choice(self):
        """ returns computer choice; rock, paper, or scissors"""
        from random import randint
        self.computer_choice = randint(1, 3)
        if self.computer_choice == 1:
            self.computer_choice = "rock"
        elif self.computer_choice == 2:
            self.computer_choice = "paper"
        else:
            self.computer_choice = "scissors"
        return self.computer_choice

rps = Game()
name = rps.player_name("steve")
print(name)
print(rps.get_computer_choice())
print(rps.get_computer_choice())
