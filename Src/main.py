import os
import pyspark
import numpy as np
import math
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType
import sys
from random import random 
import timeit
from operator import add
import shutil
import os

if os.path.exists("./../OUTPUT"):
	shutil.rmtree("./../OUTPUT") 
#on supprime le dossier OUTPUT si il existe pour ne pas avoir d erreur lors de la creation des fichiers output

spark = SparkSession.builder.appName("Pi_estimator").getOrCreate()
sc = spark.sparkContext


def is_point_inside_unit_circle(p):
    x, y = random(), random() #simuler les point x et y 
    return 1 if x*x + y*y < 1 else 0 #verifier si les deux points sont dans le cercle
    
def pi_estimator_spark(n): 
	start = timeit.timeit()
	count = sc.parallelize(range(0, n))
	temp = count.map(is_point_inside_unit_circle)
	nin = temp.reduce(add)
	end = timeit.timeit()
	esti_pi = (4.0 * nin / n)
	tps_spark = end-start
	return tps_spark, esti_pi


def pi_estimator_numpy(n):
	start = timeit.timeit()
	nin=0
	for i in range (0,n):
		nin=nin+is_point_inside_unit_circle(1)
		
	esti_pi=4*nin/n
	end = timeit.timeit()
	tps_numpy=end-start
	return tps_numpy, esti_pi
	
n = 1000000


[tps_spark, pi_spark]=pi_estimator_spark(n)
[tps_numpy, pi_numpy]=pi_estimator_numpy(n)

pourcent_spark=abs((pi_spark-math.pi)*100/math.pi)
pourcent_numpy=abs((pi_numpy-math.pi)*100/math.pi)

print('temps de calcul avec numpy',tps_numpy)
print('temps de calcul avec spark',tps_spark)
print('estimation de pi avec spark=',pi_spark)
print('estimation de pi avec numpy=',pi_numpy)
print('pourcentage d erreur avec numpy',pourcent_numpy)
print('pourcentage d erreur avec spark',pourcent_spark)

sc.parallelize([tps_spark]).saveAsTextFile("./../OUTPUT/Spark/Temps")
sc.parallelize([pi_spark]).saveAsTextFile("./../OUTPUT/Spark/Estimation_pi")
sc.parallelize([pourcent_spark]).saveAsTextFile("./../OUTPUT/Spark/Erreur")

sc.parallelize([tps_numpy]).saveAsTextFile("./../OUTPUT/Numpy/Temps")
sc.parallelize([pi_numpy]).saveAsTextFile("./../OUTPUT/Numpy/Estimation_pi")
sc.parallelize([pourcent_numpy]).saveAsTextFile("./../OUTPUT/Numpy/Erreur")