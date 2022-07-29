# Event-Driven Architecture - Part 2
# This lesson is part two of the discussion on event-driven architecture.

# What are events?
# There are typically two kinds of processes in applications: CPU intensive and IO intensive. In the context of web applications, IO means events. A large number of IO operations mean a lot of events occurring over a period of time, and an event can be anything from a tweet to a click of a button, an HTTP request, an ingested message, a change in the value of a variable, and so on.

# We know that web 2.0 real-time applications have a lot of events. For instance, there are a lot of request-response cycles between the client and the server, typically in an online game, messaging app and so on. Events happening too often is called a stream of events. And we know how streams are managed from the previous stream processing chapter.

# Event-driven architecture
# Non-blocking architecture is also known as reactive or event-driven architecture. Event-driven architectures are pretty popular in modern web application development.

# Technologies like NodeJS, frameworks in the Java ecosystem like Play, Akka are non-blocking in nature and are built for modern high IO applications.

# They are capable of handling a big number of concurrent connections with minimal resource consumption. Modern applications need a fully asynchronous model to scale. These modern web frameworks provide more reliable behavior in a distributed environment. They are built to run on a cluster, handle large-scale concurrent scenarios, and tackle problems that generally occur in a clustered environment. They enable us to write code without worrying about handling multi-threads, thread lock, out-of-memory issues due to high IO, etc.

# Reactive architecture simply means reacting to the events occurring regularly. The code is written to react to the events. And to react to the events, the system has to continually monitor the stream. Event-driven architecture is all about processing asynchronous data streams. The application becomes inherently asynchronous.

# system_design_full_path/images/067.png

# Technologies for implementing the event-driven architecture
# With the advent of Web 2.0, people in the tech industry felt the need to evolve the technologies to be powerful enough to implement modern web application use cases. Spring Framework added the Spring Reactor module to the core Spring repo. Developers wrote NodeJS, Akka, Play, etc.

# You would have figured that reactive, event-driven applications are challenging to implement with thread-based frameworks because when trying to write non-blocking code with threads, we have to deal with shared mutable state and locks and whatnot that make things pretty complex.

# In an event-driven system, everything is treated as a stream. The level of abstraction is good, and developers don’t have to worry about managing the low-level memory stuff.

# Typical event streaming use cases that apply here are: handling a large number of transactional events, a timeline of changing stock prices, user events on an online shopping application, etc.

# NodeJS is a single-threaded non-blocking framework written to handle more IO-intensive tasks. It has an event loop architecture. More on NodeJS event loop architecture here.

# LinkedIn uses the Play framework for identifying the online status of its users.

# Now the emergence of non-blocking tech does not mean that traditional tech becomes obsolete and every app has to have an asynchronous non-blocking model. Again, every tech has its use cases and trade-offs.

# NodeJS is not fit for CPU-intensive tasks. CPU-intensive operations are operations that require a good amount of computational power like for graphics rendering, running ML algorithms, handling data in enterprise systems, etc. It would be a mistake to pick NodeJS for these purposes.

# In the upcoming lessons, I will discuss the general guidelines to consider when picking the fitting server-side technology. Let’s move on to the next lesson.
