import quantumrandom


for _ in range(1000):
    rand = int(quantumrandom.randint(1,7))
    if (rand >=1) and (rand <= 6):
        print(rand)

