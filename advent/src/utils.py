def Open(day):
    with open(f'advent/data/day{day}.txt', 'r', encoding='utf8') as f:
        return [x.strip() for x in f.readlines()]




class Day:
    """lets go"""

    def __init__(self) -> None: pass
        

    def open(self, day):
        """Lets Generically open a file."""
        with open(f'advent/data/day{day}.txt', 'r', encoding='utf8') as file:
            return [x.strip() for x in file.readlines()]
