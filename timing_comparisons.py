# timing_comparisons.py
import random
import timeit
from dynamic_programming import soccer_dyn_prog
from exhaustive_search import soccer_opponent_avoidance


def generate_test_input(n):
    characters = ['.', 'X', 'O']
    F = [[random.choice(characters) for _ in range(n)] for _ in range(n)]
    return F


input_sizes = [9, 10, 11, 12, 13, 14, 15]
dp_timings = []
es_timings = []

for n in input_sizes:
    print("Running Input size: ", n)
    F = generate_test_input(n)
    elapsed_time_dp = timeit.timeit(lambda: soccer_dyn_prog(F), number=1)
    dp_timings.append(elapsed_time_dp)

    elapsed_time_es = timeit.timeit(lambda: soccer_opponent_avoidance(F, 1), number=1)
    es_timings.append(elapsed_time_es)

print("Dynamic Programming Timings:", dp_timings)
print("Exhaustive Search Timings:", es_timings)
