from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType, IntegerType
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName(
    "UnstructuredDataProcessing").getOrCreate()

# Define schema explicitly
schema = StructType([
    StructField("CustomerID", IntegerType(), True),
    StructField("interaction_type", StringType(), True),
    StructField("value", FloatType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Load unstructured data from HDFS with schema and multiline option
unstructured_data = spark.read.schema(schema)\
    .option("multiline", "true")\
    .json("hdfs://localhost:9000/data/raw/unstructured_data.json")

# Display schema and a sample of the data
unstructured_data.printSchema()
unstructured_data.show(truncate=False)

# Convert to Pandas for further processing
unstructured_df = unstructured_data.toPandas()

# Save processed data to a CSV file
unstructured_df.to_csv('./data/unstructured_data.csv', index=False)
