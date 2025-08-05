from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count, window
from pyspark.sql.types import StructType, StringType, TimestampType

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1") \
    .getOrCreate()

schema = StructType() \
    .add("user_id", StringType()) \
    .add("event_type", StringType()) \
    .add("event_time", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "events") \
    .option("startingOffsets", "latest") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

metrics_df = parsed_df \
    .withColumn("event_time", col("event_time").cast(TimestampType())) \
    .groupBy(window(col("event_time"), "1 minute"), col("event_type")) \
    .agg(count("*").alias("event_count"))

query = metrics_df.writeStream \
    .format("parquet") \
    .option("path", "output/metrics") \
    .option("checkpointLocation", "output/checkpoint") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
