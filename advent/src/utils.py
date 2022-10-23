def Open(day):
    with open(f'advent/data/day{day}.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]