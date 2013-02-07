import argparse
import sys
import random

def half_even_generator(max_length, upper_bound):
    length = random.randrange(1, max_length + 1)
    numbers = [random.randrange(upper_bound) for _ in xrange(length)]

    if len(filter(lambda n: n % 2 == 0, numbers)) >= (length // 2):
        category = 'T'
    else:
        category = 'F'

    return category, numbers

def half_even_generator_arg_types():
    return [int, int]

def make_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generator', action='store', dest='generator', help='the generator to use')
    parser.add_argument('-p', '--passthrough', action='store', dest='generator_args', help='pass this arguments to the generator')
    parser.add_argument( 'num_data', action='store', type=int, help='the number of data points to generate' )

    return parser
    

if __name__ == "__main__":
    args = make_argument_parser().parse_args()
    generator = locals()[args.generator + '_generator']
    generator_arg_types = locals()[args.generator + '_generator_arg_types']()
    generator_args = []

    for type_, arg in zip(generator_arg_types,args.generator_args.split()):
        generator_args.append(type_(arg))

    for i in range(args.num_data):
        category, features = generator(*generator_args)

        print(str(category) + ' ' + ' '.join(map(str, features)))
