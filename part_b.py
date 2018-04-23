from pyspark import SparkContext
from numpy import array
from pyspark.mllib.clustering import KMeans, KMeansModel

sc =SparkContext()
# do NOT change this line
data=sc.textFile("dataset/cars.data")

# TODO

f=open('py_part_b.txt','w+')
# TODO
f.close()
