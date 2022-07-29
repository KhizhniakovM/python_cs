# Distributed Data Processing
# In this lesson, we will discuss distributed data processing and the technologies used for it.

# This lesson is all about distributed data processing. I’ll talk about what it is, how different it is compared to a centralized data processing system, the architectures involved in it, and more.

# So, without further ado, let’s get on with it.

# What is distributed data processing?
# Distributed-data processing means diverging large amounts of data to several nodes running in a cluster for parallel processing.

# All the nodes in the cluster execute the task allotted parallelly, working in conjunction coordinated by a node-coordinator. Apache Zookeeper is one example of a node coordinator widely used in the industry.

# Since the nodes are distributed and the tasks are executed parallelly, this makes the entire set-up pretty scalable and highly available. The workload can be scaled both horizontally and vertically. Data is made redundant and replicated across the cluster to avoid any sort of data loss.

# system_design_full_path/images/064.png

# Processing data in a distributed environment helps accomplish tasks in significantly less time as opposed to when running it on a centralized data processing system. In a distributed system, the tasks are shared by several nodes. In a centralized system, the tasks are queued to be processed one by one.

# Distributed data processing technologies
# Here are some of the popular technologies used in the industry for large-scale data processing.

# MapReduce – Apache Hadoop
# MapReduce is a programming model written for managing distributed data processing across several different machines in a cluster. This involves distributing tasks to several machines, running work in parallel, and managing all the communication and data transfer within different parts of the system.

# The map part of the programming model involves sorting the data based on a parameter and the reduce part involves summarizing the sorted data.

# The most popular open-source implementation of the MapReduce programming model is Apache Hadoop. The framework is used by all big guns in the industry to manage massive amounts of data in their system. It is used by Twitter for running analytics and by Facebook for storing big data.

# Apache Spark
# Apache Spark is an open-source cluster computing framework. It provides high performance for both batch and real-time in -stream processing. It can work with diverse data sources and facilitates parallel execution of work in a cluster.

# Spark has a cluster manager and distributed data storage. The cluster manager facilitates communication between different nodes running together in a cluster, whereas the distributed storage facilitates storing Big Data. Spark seamlessly integrates with distributed data stores like Cassandra, HDFS, MapReduce File System, Amazon S3, etc.

# Apache Storm
# Apache Storm is a distributed stream processing framework. In the industry, it is primarily used for processing massive amounts of streaming data. It has several different use cases, such as real-time analytics, machine learning, distributed remote procedure calls, etc.

# Apache Kafka
# Apache Kafka is an open-source distributed stream processing and messaging platform. It’s written using Java and Scala and was developed by LinkedIn.

# The storage layer of Kafka involves a distributed scalable pub-sub message queue. It helps read and write streams of data like a messaging system.

# Kafka is used to develop real-time features such as notification platforms, managing streams of massive amounts of data, monitoring website activity and metrics, messaging, and log aggregation.

# Hadoop is preferred for batch data processing, whereas Spark, Kafka, and Storm are the right pick for processing real-time streaming data.

# By now, I am sure you have a good idea of what data processing is and are aware of its use-cases in modern application development and the associated technologies.

# In the lesson up next, let’s take a look at a couple of architectures involved in the process: Lambda and Kappa.
