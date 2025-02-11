import random

# print(" \u25CF  \u250C  \u2500  \u2510  \u2502  \u2514  \u2518")

#          ●      ┌        ─      ┐        │       └        ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"


dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")
}


dice_list = []
total = 0
dice_roll = int(input("Enter total dice rolls you want: "))

for die in range(dice_roll):
    dice_list.append(random.randint(1, 6))
print(dice_list)

for die in range(dice_roll):
    for line in dice_art.get(dice_list[die]):
        print(line)

for die in dice_list:
    total += die
print(f"Sum of {len(dice_list)} Dice Rolls = {total}")