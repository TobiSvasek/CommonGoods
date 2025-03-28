﻿# CommonGoods

Tento projekt simuluje hru, ve které hráči s různými strategiemi přispívají do společného fondu. Hra se skládá z několika kol, ve kterých hráči rozhodují, kolik jednotek přispějí na základě své strategie a předchozích příspěvků ostatních hráčů.

## Třídy a jejich popis

### Player
Abstraktní třída, která reprezentuje hráče. Každý hráč má jméno a určitý počet jednotek. Metoda `decide_contribution` musí být přepsána v podtřídách.

### AlwaysFairPlayer
Třída, která reprezentuje hráče, který vždy přispívá polovinu svých jednotek.

### AlwaysSelfishPlayer
Třída, která reprezentuje hráče, který nikdy nepřispívá žádné jednotky. Většinou nejúspešnější strategie.

### ReactivePlayer
Třída, která reprezentuje hráče, který přispívá na základě průměrného příspěvku ostatních hráčů v předchozím kole.

### RandomPlayer
Třída, která reprezentuje hráče, který přispívá náhodný počet jednotek.

### Game
Třída, která reprezentuje hru. Obsahuje seznam hráčů, historii předchozích příspěvků a historii celkového fondu. Metoda `play_round` simuluje jedno kolo hry.

## Použití

1. Vytvořte hráče s různými strategiemi.
2. Vytvořte instanci hry s těmito hráči.
3. Simulujte několik kol hry a sledujte, jak se mění počet jednotek jednotlivých hráčů a celkový fond.

## Jak poznám, že program funguje?
To, že program funguje, dokazuje graf, který se v průběhu hry nějak hýbe.

## Interpretace hry 
Hru jsem pochopil jako nástroj, který dokazuje, že společné cíle se dají dosáhnout i přesto, že lidé mají odlišné názory či incentývy, a že každé rozhodnutí má nějakou váhu. Hráči stojí před rozhodnutím, zda přispět (a riskovat, že ostatní nepřispějí) nebo nechat ostatní přispívat a profitovat bez vlastního vkladu. Pokud ale všichni přispějí maximální částku, celkový zisk je nejvyšší.

## Co jsem si odnesl?
Každé rozhodnutí má svojí váhu, třeba i rozhodnutí nepřispívat a těžit ze společného dobra (příkladem je neplacení daní nebo třeba pirátění obsahu). Reálné aplikace veřejných statků jsou školy, nemocnice a silnice. Spolupráce je klíčová pro každodenní fungování společnosti, vyžaduje důvěru, ale třeba i tresty, které jsem sice v této hře neimplementoval, ale beru je v dnešním moderním světě jako nutnost.

## Příklad

```python
# Vytvoření hráčů
players = [
    AlwaysFairPlayer("Fair Player"),
    AlwaysSelfishPlayer("Selfish Player"),
    ReactivePlayer("Reactive Player"),
    RandomPlayer("Random Player 1"),
    RandomPlayer("Random Player 2")
]

# Vytvoření hry
game = Game(players)

# Simulace několika kol
num_rounds = 10
for round_number in range(num_rounds):
    game.play_round()

# Výpis výsledků
print("Jednotky hráčů po všech kolech:")
print(game.get_player_units())
print("Historie celkového fondu:")
print(game.get_total_fund_history())
