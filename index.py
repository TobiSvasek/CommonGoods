import random
import matplotlib.pyplot as plt

class Player:
    def __init__(self, name):
        self.name = name
        self.units = 10

    def contribute(self, amount):
        if amount > self.units:
            raise ValueError("Cannot contribute more units than available")
        self.units -= amount
        return amount

    def decide_contribution(self, previous_contributions):
        raise NotImplementedError("This method should be overridden by subclasses")

class AlwaysFairPlayer(Player):
    def decide_contribution(self, previous_contributions):
        return self.contribute(self.units // 2)

class AlwaysSelfishPlayer(Player):
    def decide_contribution(self, previous_contributions):
        return self.contribute(0)

class ReactivePlayer(Player):
    def decide_contribution(self, previous_contributions):
        if previous_contributions:
            average_contribution = sum(previous_contributions) // len(previous_contributions)
            return self.contribute(min(average_contribution, self.units))
        return self.contribute(0)

class RandomPlayer(Player):
    def decide_contribution(self, previous_contributions):
        return self.contribute(random.randint(0, int(self.units)))

class Game:
    def __init__(self, players):
        self.players = players
        self.previous_contributions = []
        self.total_fund_history = []

    def play_round(self):
        contributions = [player.decide_contribution(self.previous_contributions) for player in self.players]
        self.previous_contributions = contributions

        total_fund = sum(contributions)
        self.total_fund_history.append(total_fund)
        multiplied_fund = total_fund * 1.5
        share = multiplied_fund / len(self.players)

        for player in self.players:
            player.units += share

        return contributions

    def get_player_units(self):
        return {player.name: player.units for player in self.players}

    def get_total_fund_history(self):
        return self.total_fund_history

# Create players with different strategies
players = [
    AlwaysFairPlayer("Fair Player"),
    AlwaysSelfishPlayer("Selfish Player"),
    ReactivePlayer("Reactive Player"),
    RandomPlayer("Random Player 1"),
    RandomPlayer("Random Player 2")
]

# Create game
game = Game(players)

# Print initial units of each player
print("Initial units of each player:")
print(game.get_player_units())
print()

# Simulate multiple rounds
num_rounds = 10
for round_number in range(num_rounds):
    contributions = game.play_round()
    print(f"After round {round_number + 1}:")
    print("Player units:", game.get_player_units())
    print("Contributions:", {player.name: contribution for player, contribution in zip(game.players, contributions)})
    print("Total fund history:", game.get_total_fund_history())
    print()

# Plot the total fund history
total_fund_history = game.get_total_fund_history()
plt.plot(total_fund_history, marker='o', color='red')
plt.title('Total Fund Over Time')
plt.xlabel('Round')
plt.ylabel('Total Fund')
plt.grid(True)
plt.show()

# Strategie, která je nejúspěšnější, závisí na tom, kolik jednotek má každý hráč na konci hry.
# Můžeme porovnat jednotky každého hráče po všech kolech a zjistit, který hráč má nejvíce jednotek.
# Většinou jsou dle testování nejúspěšnější "selfish" hráči, neboli hráči chamtiví, na konci mají většinou nejvíc bodů.