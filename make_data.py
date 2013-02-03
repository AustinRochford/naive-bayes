import sys
import random

if __name__ == "__main__":
    num_data = int(sys.argv[1])
    max_length = int(sys.argv[2])

    for i in range(num_data):
        length = random.randrange(1, max_length + 1)

        num_even = 0
        num_odd = 0
        ns = []

        for j in range(length):
            n = random.randrange(1, 11)
            ns.append(n)

            if n % 2 == 0:
                num_even += 1
            else:
                num_odd += 1

        if num_odd > num_even:
            result = 'F'
        else:
            result = 'T'

        print(result + ' ' + ' '.join(map(str,ns)))
