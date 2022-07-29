# Data Ingestion Use Cases
# In this lesson, we will discuss some of the industry's common data ingestion use cases.

# This is where I talk about some of the data streaming use cases commonly implemented in the industry.

# Moving Big Data into Hadoop
# This is data ingestion’s most popular use. As discussed before, Big Data from IoT devices, social apps, and other sources streams through data pipelines and moves into the most popular distributed data processing framework Hadoop for analysis.

# Streaming data from databases to Elasticsearch server
# Elasticsearch is an open-source framework for implementing search in web applications. It is a de facto search framework used in the industry simply because of its advanced features and it being open source. Being open-source enables businesses to write their own custom solutions when they need them.

# In the past, I wrote a product search as a service using Java, Spring Boot, and Elastic search. A large amount of data was streamed from the legacy storage solutions to the Elasticsearch server and indexed to make the products come up in the search results.

# All the data intended to show up in the search was replicated from the main storage to the Elasticsearch storage. Also, as the new data was persisted in the main storage, it was asynchronously delivered to the Elastic server in real-time for indexing.

# Log processing
# If your project isn’t a hobby project, chances are it’s running on a cluster. When we talk about running a large-scale service, monolithic systems don’t cut it. With so many microservices running concurrently, there is a massive number of logs, which are generated over a period of time. Logs are the only way to move back in time, track errors, and study the system’s behavior.

# So, to study the behavior of the system holistically, we have to stream all the logs to a central place. All the logs are ingested to a central server to run analytics with the help of solutions like the ELK(Elastic Logstash Kibana) stack, etc.

# Stream processing engines for real-time events
# Real-time streaming and data processing are the core components in systems handling LIVE information such as sports. It’s imperative that the architectural setup in place is efficient enough to ingest data, analyze it, figure out the behavior in real-time, and quickly push the updated information to the fans.

# Message queues like Kafka and stream computation frameworks like Apache Storm, Apache Nifi, Apache Spark, Samza, Kinesis, etc., are used to implement the real-time large-scale data processing features in online applications.

# Here is a good read on the topic: An insight into Netflix’s real-time streaming platform.

# Let’s look into data pipelines in the next lesson.
