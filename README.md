# CommonGoods

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