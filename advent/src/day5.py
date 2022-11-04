from timeit import default_timer as timer
import hashlib
from advent import Day, Open


class Day5(Day):
    def __init__(self):
        # self.data = Open(5)
        # self.data = 'ugkcyxxp'
        self.data = 'abc'
        self.main()

    def part1(self):
        result = ['_','_','_','_','_','_','_','_']
        counter = 0
        start_time = timer()
        while True:
            if not [x for x in result if x == '_']: break
            proc = hashlib.md5(bytes('{}{}'.format(self.data, counter), encoding='utf8')).hexdigest()
            counter+=1
            if proc[:5] != '00000': continue
            try:
                result_idx = int(proc[5])
                if not result[result_idx] == '_':continue
                result[result_idx] = proc[6]
                runtime = timer() - start_time
                print(''.join(result), f'runtime: {runtime:.6f}')
            
            except KeyboardInterrupt:
                print(result)
                break
            except:
                pass
        return ' '.join(result)
    
    def main(self):
        password = self.part1()
        print(password)

# f2c730e55 is wrong.