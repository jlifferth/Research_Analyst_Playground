import cProfile
import io
import math
import pstats
import random
import datetime as dt

pr = cProfile.Profile()
pr.enable()


def a():
    result_list = []
    for _ in range(100000):  # do something CPU heavy
        result_list.append(_ * random.randint(1, 100))

    return result_list


a()
pr.disable()

result = io.StringIO()
pstats.Stats(pr, stream=result).print_stats()
result = result.getvalue()
# chop the string into a csv-like buffer
result = 'ncalls' + result.split('ncalls')[-1]
result = '\n'.join([','.join(line.rstrip().split(None, 5)) for line in result.split('\n')])
# save it to disk

dt_string = dt.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
filename = 'profiles/profile_{}.csv'.format(dt_string)
with open(filename, 'w') as f:
    # f=open(result.rsplit('.')[0]+'.csv','w')
    f.write(result)
    f.close()
