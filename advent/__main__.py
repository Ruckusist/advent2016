from timeit import default_timer as timer
from advent import Day1,Day2,Day3,Day4,Day5,Day7,Day8

from rich import print
from rich.prompt import Prompt

def main():
    # CHOOSE THE DAY TO RUN.
    print("Advent of Code2016.")
    choice = Prompt.ask("What day would you like to run(1-8)?", default=1)
    startTime = timer()
    days = [Day1,Day2,Day3,Day4,Day5,None,Day7,Day8]
    runner = days[int(choice)+1]
    startTime = timer()
    runner()
    runTime = timer() - startTime
    print(f"Runtime: {runTime:.6f}")

main()