# KafkaSparkStructuredStreaming
Application to process Spark Structured Streaming data using Pyspark where one Kafka Topic is a Source and another one is a Sink.

## Kafka
producer.py - Generate Streaming data into Kafka Topic to be further used by PySpark for prcessing streaming data

consumer.py - Get processed data from Sink Kafka Topic

data.py - Used to generate fake streaming data

## PySpark
PySpark-Kafka-Streaming.ipynb - Jupyter notebook containing Pypark code to process streaming data from Source KAfka Topic(Producer) to Sink Kafka Topic(Consumer). 
