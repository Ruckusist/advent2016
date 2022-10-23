from advent import Open

class Day1:
    def __init__(self):
        self.inp = Open(1)
        self.main()

    def main(self):
        # print(self.inp)
        clean = self.inp[0].split(', ')
        size = 500
        
        # print(clean)
        arena = [[0 for _ in range(size)] for _ in range(size)]
        offset = size//2
        x,y = (offset,offset)
        dir = 0
        dirs = lambda x,y,dir: [(x-1,y),(x,y+1),(x+1,y),(x,y-1)][dir]
        # print(x,y)
        for line in clean:
            c = line[0]
            a = line[1:]
            # print(c, a)
            # print(x,y, dir)
            if c == 'R': 
                dir+=1
                if dir > 3:dir = 0
            elif c == 'L':
                dir-=1
                if dir < 0:dir = 3
            else: print('ERROR in dir.')
            
            for _ in range(int(a)):
                x,y = dirs(x,y,dir)
                # print(x,y, dir)
        print(x-offset+y-offset)
