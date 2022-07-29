# Kappa Architecture
# In this lesson, we will discuss the Kappa architecture of data processing.

# What is Kappa architecture?
# In Kappa architecture, all the data flows through a single data streaming pipeline in contrast to the Lambda architecture, which has different data streaming layers that converge into one.

# system_design_full_path/images/066.png

# The architecture flows the data of both real-time and batch processing through a single streaming pipeline, reducing the complexity of managing separate layers for processing data.

# Layers of Kappa architecture
# Kappa contains only two layers: Speed, which is the streaming processing layer, and Serving, which is the final layer. Also, Kappa is not an alternative for Lambda. Both the architectures have their use cases.

# Kappa is preferred if the batch and the streaming analytics results are fairly identical in a system. Lambda is preferred if they are not.

# Well, this concludes the stream processing chapter. Setting up and running a distributed system is something that is not trivial and requires years of work to perfect the system.

# With this being said, let’s move on to the next chapter, where I talk about different kinds of architectures involved in the software development domain.
