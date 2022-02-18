import random

import yappi


def a():
    result = []
    for _ in range(10000):  # do something CPU heavy
        result.append(_ * random.randint(1, 100))

    return result


yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
yappi.start()
a()

func_stats = yappi.get_func_stats()
thread_stats = yappi.get_thread_stats()

func_stats.save('yappi_results.prof', type='callgrind')
func_stats.print_all()
