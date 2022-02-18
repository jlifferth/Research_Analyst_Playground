# 1 - Profile few lines in your code.
import cProfile

filename = 'filename.prof'
pr = cProfile.Profile()
pr.enable()
# ... lines to profile ...

import random


def a():
    result = []
    for _ in range(10000):  # do something CPU heavy
        result.append(_ * random.randint(1, 100))

    return result


a()

pr.disable()
pr.dump_stats(filename)
