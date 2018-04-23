from numpy import array
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext

sc =SparkContext()
# do NOT change these two lines
trainingData=sc.textFile("dataset/training.data")
testData=sc.textFile("dataset/test.data")

# TODO

f=open('py_part_d.txt','w+')
# TODO
f.close()
