import random


# Generate the result of rolling n dice with m sides
def roll(num_dice: int, num_sides: int) -> []:
    random.seed()
    dice = []
    for i in range(0, num_dice):
        result = random.randint(1, num_sides)
        dice.append(result)
    return dice
