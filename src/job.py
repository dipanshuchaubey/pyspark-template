"""
Sample job to test the Spark cluster
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col


sc = (
    SparkSession.builder.appName("Python Spark SQL basic example")
    .config("spark.driver.host", "localhost")
    .getOrCreate()
)


sc.sparkContext.setLogLevel("ERROR")

df = sc.read.load(
    "datasets/large/organizations.csv", format="csv", sep=",", header="true"
)

df = df.withColumn(
    "taxable", when(col("number_of_employees") > 1000, True).otherwise(False)
)

df.show()
df.printSchema()
