from collections import defaultdict
import sys
from mrjob.protocol import JSONProtocol
from numpy import product

def classify(category_probs, cond_probs, features):
    posteriors = defaultdict(float)

    for category in category_probs:
        posteriors[category] = compute_posterior(category, category_probs[category], cond_probs, features)

    return max(posteriors, key=posteriors.get)

#not the actual posterior, but proportional to it independent of the category
def compute_posterior(category, category_prob, cond_probs, features):
    return category_prob * product([cond_probs[(category, feature)] for feature in features])

def parse_in_file(name):
    source = open(name, 'r')
    parsed = [parse_in_line(line)for line in source]
    source.close()

    return parsed

def parse_in_line(line):
    return line.split()

def parse_prob_file(name):
    cond_probs = defaultdict(float)
    category_probs = defaultdict(float)

    source = open(name, 'r')

    for line in source: 
        pair, prob = read(line)
        category, feature = pair

        if feature is None:
            category_probs[category] = prob
        else:
            cond_probs[pair] = prob

    source.close()

    return category_probs, cond_probs

def read(string):
    list_, prob = JSONProtocol.read(string)

    return tuple(list_), prob

if __name__ == "__main__":
    prob_file = sys.argv[1]
    in_file = sys.argv[2]

    category_probs, cond_probs = parse_prob_file(prob_file)
    data = parse_in_file(in_file)

    for features in data:
        print(classify(category_probs, cond_probs, features))
