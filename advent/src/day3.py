from advent import Open


class Day3:
    def __init__(self):
        self.data = Open(3)
        self.main()

    def main(self):
        counter = 0
        for i in range(0,len(self.data),3):
            x = self.data[i]
            y = self.data[i+1]
            z = self.data[i+2]
            a,a1,a2 = [int(x) for x in x.split(' ') if x]
            b,b1,b2 = [int(x) for x in y.split(' ') if x]
            c,c1,c2 = [int(x) for x in z.split(' ') if x]
            if ((a+b) > c and 
                (a+c) > b and
                (c+b) > a ): counter += 1
            if ((a1+b1) > c1 and 
                (a1+c1) > b1 and
                (c1+b1) > a1 ): counter += 1
            if ((a2+b2) > c2 and 
                (a2+c2) > b2 and
                (c2+b2) > a2 ): counter += 1
        print(counter)

# 253 is too low
# 1381 is ... high
# 862 is right

# PART 2
# 909 is too low
# 1635 is too high
# 1577 is the right answer