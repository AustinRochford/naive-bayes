import sys
import random

def has_property(ns):
    return len(list(filter(lambda n: n % 2 == 0, ns))) > len(ns) / 2

if __name__ == "__main__":
    num_data = int(sys.argv[1])
    max_length = int(sys.argv[2])

    for i in range(num_data):
        length = random.randrange(1, max_length + 1)

        ns = []

        for j in range(length):
            n = random.randrange(1, 11)
            ns.append(n)

        if has_property(ns):
            result = 'T'
        else:
            result = 'F'

        print(result + ' ' + ' '.join(map(str,ns)))
