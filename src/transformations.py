from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, split
from pyspark.sql.types import IntegerType

sc = SparkSession.builder.appName("sample").getOrCreate()

sc.sparkContext.setLogLevel("debug")

df = sc.read.load(
    "datasets/medium/order_items.csv", format="csv", sep=",", header="true"
)

df = df.withColumn("quantity", col("quantity").cast(IntegerType()))
df = df.withColumn("received", col("received").cast(IntegerType()))

df = df.withColumn(
    "unit",
    when(col("unit").like("Nos"), "Numbers")
    .when(col("unit").like("Units"), "Numbers")
    .when(col("unit").like("Ltr"), "Litre")
    .when(col("unit").like("Kgs"), "Kilogram")
    .otherwise("NA"),
)

df = df.withColumn("status", split("status", "_").getItem(1))

# Calculate final cost
df = df.withColumn(
    "total_rate", col("rate").cast(IntegerType()) * col("received").cast(IntegerType())
)

df = df.dropna()

df.show()
df.printSchema()
