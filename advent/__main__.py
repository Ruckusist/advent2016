from timeit import default_timer as timer
from advent import Day1

startTime = timer()
Day1()
runTime = timer() - startTime
print(f"Runtime: {runTime}")