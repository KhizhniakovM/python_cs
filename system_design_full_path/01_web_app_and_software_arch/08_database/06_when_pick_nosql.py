# When to pick a NoSQL Database?
# In this lesson, we will understand when to choose a NoSQL database over any other kind of database.

# Handling a large number of read-write operations
# NoSQL databases are built to handle a large number of read-write operations due to the eventual consistency model. With the ability to add nodes on the fly, they can handle more concurrent traffic, enabling us to scale fast.

# They are also built to handle big data with minimal latency. Pick a NoSQL database if you are looking to scale fast and willing to give up on strong consistency.

# Flexibility with data modelling
# A NoSQL DB is a good fit if you are not sure about your data model during the initial phases of development and things are expected to change at a rapid pace. NoSQL databases offer us more flexibility.

# Eventual consistency over strong consistency
# NoSQL databases are a good pick when we do not need ACID transactions and are okay to give up strong consistency.

# A good example of this is a microblogging site like Twitter. When a celebrity’s tweet blows up and everyone likes and re-tweets it from across the world, does it matter if the like count goes up or down a tad bit for a short while?

# The celebrity certainly wouldn’t care if instead of the actual 5 million 500 likes, the system shows the like count as 5 million 250 for a short while.

# When a large application is deployed on hundreds of servers spread across the globe, the geographically distributed nodes take some time to reach a global consensus.

# Until they reach a consensus, the value of the entity is inconsistent. The value of the entity eventually becomes consistent after a short while. This is what eventual consistency is .

# However, the inconsistency does not mean any sort of data loss. It just means that the data takes a short while to travel across the globe via the internet cables under the ocean to reach a global consensus and become consistent.

# We experience this behavior all the time, especially on YouTube. Often you might see a video with 10 views and 15 likes. How is this even possible?

# It’s not. The actual views are already more than the likes. It’s just the count of views is inconsistent and takes a short while to get updated. I will discuss eventual consistency in more detail in the upcoming lessons.

# Running data analytics
# NoSQL databases also fit best for data analytics use cases, where we have to deal with an influx of massive amounts of data.

# There are dedicated databases for use cases like this, such as time-series databases, wide-column, document-oriented databases, etc. I’ll talk about each of them later in this chapter.

# In the next lesson, let’s look into the performance comparison of SQL and NoSQL technology.
