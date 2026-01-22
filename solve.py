# A modular number line going from 1-12.
# Start on 12.
# Randomly move left or right. 
# Repeat until every number has been reached. 
# What is the probability that the last number to be reached is 6?

import random, time

def play():
        
        n = 12
        
        valset = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 }

        while valset:
                move = random.choice([-1, 1])
                n = (n + move) % 12
                if n == 0:
                        n = 12
                valset.discard(n)
                
        return n

# Play lots of times and count how many times a 6 is returned.
# E.g. 10/100 times means the probability is 10%.

start = time.perf_counter()

sixes = 0
limit = 1000000
for i in range(limit):
        m = play()
        if m == 6:
                sixes += 1

pct = sixes / limit * 100
print(f"{pct:.2f}")

end = time.perf_counter()
elapsed_time = end - start
print(f"Execution time: {elapsed_time:.4f} seconds")
