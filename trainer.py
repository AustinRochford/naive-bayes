from mrjob.job import MRJob

from collections import Counter, defaultdict

def repeat(x):
    while True:
        yield x

class NaiveBayes(MRJob):
    def category_reducer(self, key, values):
        if key is not None:
            yield (key, values.next())
        else:
            for category, count in values:
                self.counts[category] += count

    def category_reducer_final(self):
        total = sum(self.counts.values())

        for category, count in self.counts.iteritems():
            yield ((category, None), count / total)

    def category_reducer_init(self):
        self.counts = defaultdict(int)

    def feature_reducer(self, category, feature_counts):
        for feature, count in feature_counts:
            self.category_counts[category] += count
            self.feature_counts[(category, feature)] += count

    def feature_reducer_final(self):
        for pair, count in self.feature_counts.iteritems():
            category, _ = pair

            yield (pair, count / self.category_counts[category])

        for pair in self.category_counts.iteritems():
            yield (None, pair)

    def feature_reducer_init(self):
        self.category_counts = defaultdict(int)
        self.feature_counts = defaultdict(int)

    def mapper(self, _, line):
        split_line = line.split()

        category = split_line[0]
        self.counts.update(zip(repeat(category), split_line[1:]))

    def mapper_final(self):
        for (category, feature), count in self.counts.iteritems():
            yield (category, (feature, count))

    def mapper_init(self):
        self.counts = Counter()

    def steps(self):
        return [self.mr(mapper_init=self.mapper_init, mapper=self.mapper, mapper_final=self.mapper_final, reducer_init=self.feature_reducer_init, reducer=self.feature_reducer, reducer_final=self.feature_reducer_final),
            self.mr(reducer_init=self.category_reducer_init, reducer=self.category_reducer, reducer_final=self.category_reducer_final)]

if __name__ == "__main__":
    NaiveBayes.run()
