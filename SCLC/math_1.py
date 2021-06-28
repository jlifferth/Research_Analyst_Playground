import timeit

start = timeit.default_timer()

for i in range(10**7 + 1):
    current_time = timeit.default_timer()
    print(i)
    print('Time elapsed: ', current_time)

stop = timeit.default_timer()

print('Time: ', stop - start)
