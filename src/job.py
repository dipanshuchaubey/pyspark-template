"""
Sample job to test the Spark cluster
"""
from pyspark.sql import SparkSession

sc = (
    SparkSession.builder.appName("Python Spark SQL basic example")
    .config("spark.some.config.option", "some-value")
    .getOrCreate()
)

df = sc.createDataFrame([(1, 2, 3)], ["a", "b", "c"])


df.show()
df.printSchema()
