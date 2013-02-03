naive-bayes
===========

Naive Bayes Classifier trained in Hadoop

[Naive Bayes Classifier](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)

trainer.py reads pre-classified training instances and computes the necessary probabilities to classify future data

make\_data.py produces data consisting of a list of random integers in the range 1, 2,..., 10 of random length bounded above by its second argument.  Its first argument specifies the number of lines of data to produce.  It labels whether or not each list of integers has the property defined by the function has\_property.  Currently, this function indicates whether or not at least half of the integers are even.

classify.py takes probabilities computed by trainer.py as its first argument and data to classify as it second argument.  It classifies the data!
