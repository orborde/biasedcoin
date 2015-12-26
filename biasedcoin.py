# What is the probability that a biased coin will come up heads twice?
# Assume a uniform distribution of possible biases.
#
# Thanks to Pasha for showing me the problem and its surprising
# solution.

import random

RUNS = 1000000

def coin_flip(p_heads):
    roll = random.uniform(0, 1)
    return (roll <= p_heads)

def flip_biased_coin_twice():
    p_heads = random.uniform(0, 1)
    return coin_flip(p_heads) and coin_flip(p_heads)

ct = 0
for i in xrange(RUNS):
    if flip_biased_coin_twice(): ct += 1

print ct, RUNS, float(ct)/RUNS

