# Crear la funcion weighted_lottery(weights)


import random

def weighted_lottery(weights):
    total = sum(weights.values())
    rand = random.randint(1, total)

    current = 0

    for key, value in weights.items():
        current += value
        if rand <= current:
            return key


weights = {
    'winning': 1,
    'losing': 1000
}

print(weighted_lottery(weights))

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}
print(weighted_lottery(other_weights))



print("*********************************************")

import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

print(weighted_lottery(weights))

print(weighted_lottery(other_weights))