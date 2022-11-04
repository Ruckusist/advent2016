from advent import Open


class Day2:
    def __init__(self):
        self.data = Open(2)
        self.arena = [[0,0,1,0,0],
                      [0,2,3,4,0],
                      [5,6,7,8,9],
                      [0,'A','B','C',0],
                      [0,0,'D',0,0]]
        self.arena = [[1,2,3],[4,5,6],[7,8,9]]
        self.main()

    def main(self):
        output = ""
        x,y = (1,1)
        for line in self.data:
            for d in line:
                get_dir = lambda x: 0 if x == 'U' else (1 if x == 'R' else (2 if x == 'D' else 3))
                get_xy = lambda x,y,dir: [(x-1,y),(x,y+1),(x+1,y),(x,y-1)][dir]
                dir = get_dir(d)
                px,py = (x,y)
                x,y = get_xy(x,y,dir)
                if x < 0: x=0
                if x > len(self.arena)-1: x=len(self.arena)-1
                if y < 0: y=0
                if y > len(self.arena[x])-1: y=len(self.arena[x])-1
                if self.arena[x][y] == 0: x,y = (px,py)
            output += str(self.arena[x][y])
            # break
        print(output)
# AA6D1 is the wrong answer