class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.2
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds,assists):

        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)

        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

luka = BasketballPlayer(first_name="Luka", last_name="Doncin", height_cm=201, weight_kg=105, points=32, rebounds=8, assists=9)
jan = FootballPlayer(first_name="Jan", last_name="Oblak", height_cm=200, weight_kg=100, goals=0, yellow_cards=0, red_cards=0)

def enter_football_player():

    print("Enter players data!")
    f_name = input("Enter name?")
    l_name = input("Enter last name?")
    height = input("Height?")
    weight = input("Weight?")
    goals = input("Goals?")
    y_cards = input("Yellow cards?")
    r_cards = input("Red cards?")

    new_player  =FootballPlayer(first_name=f_name, last_name=l_name, weight_kg=weight, height_cm=height, goals=goals, yellow_cards=y_cards, red_cards=r_cards)

    with open("football_players.json", "w") as football_file:
        football_file.write(str(new_player.__dict__))

    print("Player added")
    print("Players data {0}:".format(new_player.__dict__))

def enter_basketball_player():
    
    print("Enter players data!")
    f_name = input("Enter name?")
    l_name = input("Enter last name?")
    height = input("Height?")
    weight = input("Weight?")
    points = input("points?")
    rebounds = input("Rebounds?")
    assists = input("Assists?")

    new_player  =BasketballPlayer(first_name=f_name, last_name=l_name, weight_kg=weight, height_cm=height, points=points, rebounds=rebounds, assists=assists)

    with open("basketball_players.json", "w") as basketball_file:
        basketball_file.write(str(new_player.__dict__))

    print("Player added")
    print("Players data {0}:".format(new_player.__dict__))

choice = input("Chose sport! A) Football B) Basketball")

if choice.upper() == "A":
    enter_football_player()
elif choice.upper() == "B":
    enter_basketball_player()
else:
    print("Wrong entry")