# Shared-Nothing Architecture
# In this lesson, we will briefly discuss the shared-nothing architecture.

# When working with distributed systems, you’ll often hear the term shared-nothing architecture. So, I thought I’d just quickly bring it up in this lesson. Though, there is nothing really unique about this. I’ve already talked about it in the course.

# When several modules work in conjunction, they often share RAM, which is also known as the shared memory. They share the disk, that is , sharing the database, and then they share nothing. The system’s architecture where the modules or services share nothing is called the shared-nothing architecture.

# Shared-nothing architecture means eliminating all single points of failure. Every module has its own memory and disk. So, even if several modules in the system go down, the other modules online stay unaffected. It helps with scalability and performance.

# Moving on!! Let’s discuss hexagonal architecture in the next lesson.
