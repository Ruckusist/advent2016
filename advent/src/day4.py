import string
from collections import Counter
from advent import Day

class Day4(Day):
    def __init__(self):
        self.d = self.Open(4)
        self.main()

    def validate(self, line):
        result = ""
        sq = line.index('[')
        checksum = line[sq:].strip('[').strip(']')
        line = line[:sq]
        sector_id = line.split('-')[-1]
        line = line.split('-')[:-1]
        line_str = ''.join(line)
        most_common = list(reversed(sorted(Counter(line_str).most_common(), key=lambda x: x[1])))
        while True:
            if len(result)>=5: break
            idx = most_common[0][1]
            all_common = sorted([x[0] for x in most_common if x[1] == idx])
            for letter in all_common:
                if len(result)>=5: break
                result += letter
                idx_letter = most_common.index((letter,idx))
                most_common.pop(idx_letter)
        if result == checksum:
            return True
        return False

    def sector_id(self, line):
        sq = line.index('[')
        checksum = line[sq:].strip('[').strip(']')
        line = line[:sq]
        sector_id = line.split('-')[-1]
        return int(sector_id)

    def translate(self, line):
        result = ""
        sq = line.index('[')
        checksum = line[sq:].strip('[').strip(']')
        line = line[:sq]
        sector_id = line.split('-')[-1]
        line = line.split('-')[:-1]
        result = []
        for sub in line:
            sub_result = ""
            for letter in sub:
                # print(letter)
                x = string.ascii_letters.index(letter)
                y = x+int(sector_id) % 26
                # print(letter, x, y)
                if y >= 26:
                    y -= 26
                z = string.ascii_lowercase[y]
                sub_result += z
            result.append(sub_result)
        answer = ' '.join(result)
        return answer

    def main(self):
        data = self.d
        all_valid = 0
        all_translated = []
        for line in data:
            sec_id = self.sector_id(line)
            if self.validate(line):
                all_valid += sec_id
            
            all_translated.append((self.translate(line), sec_id))
        answer1 = all_valid
        answer2 = [x for x in all_translated if 'north' in x[0]][0]
        print(f"Answer1: {answer1} | Answer2: {answer2}")
