# Data Pipelines
# In this lesson, you will learn about data pipelines.

# What are data pipelines?
# Data pipelines are the core component of a data processing infrastructure. They facilitate the efficient flow of data from one point to another and enable developers to apply filters on the data streaming-in in real-time.

# Today’s enterprise is data-driven, and data pipelines are key in implementing scalable analytics systems.

# Features of data pipelines
# Speaking of some more features of the data pipelines -

# They ensure a smooth flow of data.
# They enable the business to apply filters and business logic on streaming data.
# They avert any bottlenecks and redundancy in the data flow.
# They facilitate parallel processing of the data.
# They protect data from being corrupted and so on.
# Data pipelines work on a set of rules predefined by the engineering teams, and the data is routed accordingly without any manual intervention. The entire flow of data: extraction, transformation, combination, validation and the convergence of data from multiple streams into one is automated.

# Data pipelines facilitate the parallel processing of data via managing multiple streams. I’ll talk more about distributed data processing in the upcoming lesson.

# Traditionally we used ETL systems to manage all of the data’s movement across the system, but one major limitation with the technology is that it doesn’t support the management of real-time streaming data, which on the contrary is possible with the new era data processing infrastructure powered by the data pipelines.

# What is ETL?
# If you haven’t heard of ETL before, it means Extract Transform Load.

# Extract means fetching data from single or multiple data sources.

# Transform means transforming the extracted heterogeneous data into a standardized format based on the rules set by the business.

# Load means moving the transformed data to a data warehouse or another data storage location for further processing of data.

# The ETL flow is the same as the data ingestion flow. The difference is just that the entire movement of data is done in batches as opposed to streaming it through the data pipelines in real-time.

# Though real-time data processing offers fast results, it doesn’t undermine the importance of the batch processing approach. Moreover, companies leverage both data processing techniques in their projects to get the best of both worlds.

# You’ll gain more insight into it when we go through the Lambda and Kappa architectures of distributed data processing in the upcoming lessons.

# In the previous lesson, I brought up a few popular data processing tools, such as Apache Flink, Storm, Spark, Kafka, etc. All these tools have one thing in common they facilitate processing data in a cluster in a distributed environment via data pipelines.

# What is distributed data processing? How does it work? We are going to look into this in the next lesson. Stay tuned.
