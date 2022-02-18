import cProfile
import io
import pstats
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()
# ... do something ...

a = []
for i in range(1000000):
    i = i ** 10
    a.append(i * 1000)

b = []
for item in a:
    b_value = item % 2
    b.append(b_value)

for item in b:
    print(item)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

results = [s.getvalue()]
print(results)
