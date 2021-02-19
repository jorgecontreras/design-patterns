class SoccerPlayer:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name

    def action(self):
        action = f'{self} scores amazing bicycle kick goal!'
        print(action)

class TennisPlayer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def action(self):
        action = f'{self} serves an ace and wins the set!'
        print(action)

class Azteca:
    def __init__(self, name):
        self.player_name = name
        print(self)

    def __str__(self):
        return "[ Estadio Azteca ]"

    def make_player(self):
        return SoccerPlayer(self.player_name)

class Wimbledon:
    def __init__(self, name):
        self.player_name = name
        print(self)
        
    def __str__(self):
        return "[ Wimbledon Stadium ]"

    def make_player(self):
        return TennisPlayer(self.player_name)


class Stadium:
    def __init__(self, factory):
        self.player = factory.make_player()

    def play(self):
        self.player.action()

def let_user_pick(name):
    options = ["soccer", "tennis"]
    print(f'Welcome {name}. Choose your favorite sport:')
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            i = int(i)
            return (True, i)
        else:
            print(f'Choose a valid sport')
            return (False, int(i))
    except:
        return (False, i)
    
def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, sport = let_user_pick(name)
    game = Azteca if sport == 1 else Wimbledon
    stadium = Stadium(game(name))
    stadium.play()

main()