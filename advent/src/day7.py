from advent import Day, Open


class Day7(Day):
    def __init__(self):
        self.data = Open(7)
        self.part2()

    def abba(self, line):
        for x in range(0,len(line)-3):
            x1 = line[x]
            x2 = line[x+1]
            x3 = line[x+2]
            x4 = line[x+3]

            if x1 == x4 and x2 == x3 and x1 != x2:
                return True
        return False

    def aba(self, line):
        abas = []
        for x in range(len(line)-2):
            x,y,z = line[x:x+3]
            if x==z and x!=y:
                abas.append((x,y,z))
        return abas

    def bab(self, line, aba):
        for x in range(len(line)-2):
            x,y,z = line[x:x+3]
            if x==z and x!=y: 
                a,b,c = aba
                if (x,y,z) == (b,a,b):
                    return True
        return False

    def build_data(self):
        data = []
        for line in self.data:
            outers = []
            inners = []
            cur = ""
            flag = True
            for letter in line:
                if flag:
                    if letter == '[':
                        flag = False
                        outers.append(cur)
                        cur = ""
                    else:
                        cur += letter
                        
                else:
                    if letter == ']':
                        flag = True
                        inners.append(cur)
                        cur = ""
                    else:
                        cur += letter
            if cur:
                outers.append(cur)
            data.append((line,inners,outers))
        return data

    def part1(self):
        data = self.build_data()
        counter = 0
        for (line, inners, outers) in data:
            flag = False
            for l in inners:
                if flag: break
                if self.abba(l):
                    flag = True
            
            if flag: continue

            for o in outers:
                if flag: break
                if self.abba(o):
                    counter += 1
                    flag = True
        
        print(counter)
        return counter

    def part2(self):
        data = self.build_data()
        counter = 0
        for (line, inners, outers) in data:
            # SSL -- 
            aba = []
            for sub in outers:
                if self.aba(sub):
                    aba.extend(self.aba(sub))
            if not aba: continue
            flag = False
            for sub in aba:
                if flag: break
                for inner in inners:
                    if self.bab(inner,sub):
                        counter += 1
                        flag = True
                        break
        print(counter)

# 412 is too high
# 193 is too low
# 247 .. wrong
# 242 ..