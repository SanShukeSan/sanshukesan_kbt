import random
a = [int(random.random()*10000) for i in range(5)]
b = (random.sample(a, 5))
print(min(b), max(b))