import statistics
import sys

vals = []
for val in sys.stdin:
    vals.append(float(val))
print(statistics.mean(vals), statistics.stdev(vals))



