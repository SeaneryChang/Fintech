import random
beta = [0.5]*32
theta = 0.002
partical = 4
generation = 5
pm = [[0]*32 for _ in range(partical)]
for g in range(generation):
    for p in range(partical):
        for s in range(32):
            if random.random() > beta[s]:
                pm[p][s] = 0
            else:
                pm[p][s] = 1
    print(pm)            

