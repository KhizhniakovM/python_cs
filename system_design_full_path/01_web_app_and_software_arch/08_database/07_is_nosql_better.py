# Is NoSQL More Performant Than SQL?
# In this lesson, we will learn if a NoSQL database is more performant than an SQL database.

# Is NoSQL more performant than SQL? Developers ask this question all the time when trying to decide between an SQL and a NoSQL database. And I have a one-word answer for this.

# No!!

# From a technology performance benchmarking standpoint, both relational and non-relational databases are equally performant.

# More than the technology, it’s how we design our systems using a certain technology that decides the performance.

# Both SQL and NoSQL tech have their use cases. We have already gone through them in the former lessons. So, don’t get caught up in the hype. Understand your use case and pick the fitting technology.

# Why do popular tech stacks always pick NoSQL databases?
# Picking the technology based on the use case makes sense, but why do the popular tech stacks always prefer NoSQL databases? For instance, look at the MEAN(MongoDB, ExpressJS, AngularJS/ReactJS, NodeJS) stack.

# Well, most of the online applications have standard use cases, and these tech stacks have them covered. There are also commercial reasons behind this.

# There are a plethora of tutorials available online and a mass promotion of popular tech stacks. With these resources available, it’s easy for beginners to pick them up and write their applications as opposed to researching technologies fitting their use case.

# We don’t always need to pick the popular stacks. Rather, we should pick what fits best with our use case.

# This course has a separate lesson on how to pick the right tech stack for our app. We will continue this discussion there.

# Coming back to performance, as opposed to technology, the performance of an application is more dependent on factors like application architecture, database design, bottlenecks, network latency, etc.

# If we use multiple joins in a relational database, the response will inevitably take more time. If we remove all the complex relationships and joins, a relational database will be as quick as a NoSQL one.

# Real-world case studies
# Facebook uses MySQL for storing its social graph of millions of users. Although it did have to change the DB engine and make some tweaks, MySQL fits best with its use case.

# Quora uses MySQL pretty efficiently by partitioning the data at the application level. Here is an interesting read on it.

# Note: A well-designed SQL data store will always be more performant than a not so well-designed NoSQL store.

# Using both SQL and NoSQL databases in an application
# You may be wondering, can’t I use both SQL and a NoSQL datastore in my application? What if I have a requirement fitting both?

# You can!! Moreover, all the large-scale online services use a mix of both to achieve the desired persistence behavior.

# The term for leveraging the power of multiple databases clubbed together is polyglot persistence. We will discuss this in the next lesson.
