# Different Ways of Ingesting Data and the Challenges Involved
# In this lesson, we will discuss the different ways we can ingest data. We will also cover the challenges involved in the process.

# Different ways to ingest data
# There are two primary ways to ingest data: in real-time and in batches that run at regular intervals. Which of the two to pick depends entirely on the business requirements.

# Data ingestion in real-time is typically preferred in systems reading medical data, like heartbeat or blood pressure, via wearable IoT sensors. It is also preferred in systems handling financial data like stock market events, etc. These are a few instances where time, lives, and money are closely linked, and we need information as soon as we can get it.

# On the contrary, in systems that read trends over time, we can always ingest data in batches. For instance, a system that shows data on the popularity of a sport in a region over a period of time. Real-time data in this use case isn’t critical.

# Let’s talk about some of the challenges developers face when ingesting massive amounts of data. I have added this lesson just to give you a deeper insight into the entire process. In the upcoming lesson, I’ll talk about the general use-cases of data streaming in the application development domain.

# Challenges with data ingestion
# Slow process
# Data ingestion is a slow process. Why? When the data is streamed from several different sources into the system, data coming from each source has a different format, different syntax, attached metadata, etc. The data as a whole is heterogeneous. It has to be transformed into a standard format like JSON or something to be understood well by the analytics system.

# This conversion of data is a tedious process. It takes a lot of computing resources and time. Flowing data has to be staged at several stages in the pipeline, processed, and then moved ahead.

# Also, data has to be authenticated and verified at every stage to meet the organization’s security standards. With the traditional data cleansing processes, it takes weeks, even months, to get useful information on hand. Traditional data ingestion systems like ETL ain’t that effective anymore.

# Okay! But I just said data can be ingested in real-time right? So, how could it be slow?

# I want to bring up two things here. First, the modern data processing tech and frameworks are continually evolving to beat the limitations of the legacy, traditional data processing systems. Real-time data ingestion wasn’t even possible with the traditional systems.

# Second, analytics information obtained from real-time processing is not that accurate or holistic since the analytics continually runs on a limited set of data. On the contrary, in batch processing, the entire data set is taken into account. The more time we spend studying the data, the more accurate results we get.

# You’ll learn more about this when we go through the Lambda and the Kappa architectures of data processing.

# Complex and Expensive
# The entire data flow process is resource-intensive. Much heavy lifting has to be done to prepare the data before being ingested into the system. Also, this isn’t a side process. A dedicated team is required to pull off something like this.

# Engineering teams often come across scenarios where the tools and frameworks available in the market fail to serve their needs. They have no option other than to write a custom solution from the bare bones.

# Goblin is a data ingestion tool by LinkedIn. At one point, LinkedIn had fifteen data ingestion pipelines running, which created several data management challenges. To tackle this problem, LinkedIn wrote Goblin in -house.

# Today the IoT machines in the industry are evolving at a rapid pace. The semantics of the data coming from external sources also changes sometimes because the data sources are not always under our control, which warrants a change in the backend data processing code.

# Moving data around is risky
# When data is moved around, it opens up the possibility of a breach. Moving data is vulnerable. It goes through several different staging areas, and the engineering teams have to put in additional effort and resources to ensure their system meets the security standards at all times.

# These are some of the challenges developers face when working with streaming data.
