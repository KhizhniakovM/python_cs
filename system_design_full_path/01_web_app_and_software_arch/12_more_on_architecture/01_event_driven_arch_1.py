# Event-Driven Architecture - Part 1
# In this lesson, which is part one of the event-driven architecture lessons, we will cover concepts like blocking and non-blocking.

# When writing modern Web 2.0 applications, chances are you have come across terms like reactive programming, event-driven architecture and concepts like blocking and non-blocking.

# What are they? Should you be aware of them?

# You might have also noticed that tech and frameworks like NodeJS, Play, Tornado, and Akka are gaining more popularity in the developer circles for modern application development compared to traditional tech.

# What is the reason behind this?

# Is it just that we are bored of working on the traditional tech like Java, PHP, etc. and are attracted towards the shiny new stuff, or are there technical reasons behind this?

# In this lesson, we will go through the related concepts step by step to realize the demands of modern software application development.

# So, without further ado, let’s get on with it.

# At this point in the course, we know what persistent connections are, what asynchronous behavior is and why we need them. We can’t really write real-time apps without implementing them.

# Now, let’s find out what blocking is .

# What is blocking?
# In web applications blocking means, the flow of code execution is paused while waiting for a process to complete. Until the process completes, it cannot move on.

# Let’s say we have a block of code of ten lines within a function and every line triggers another external function executing a specific task.

# Naturally, when the flow of execution enters the function, it will start executing the code from the top, from the first line. It will run the first line of code and will call the external function.

# At this point, until the external function returns the response, the flow is blocked. The flow won’t move further. It just waits for the response unless we add asynchronous behavior to it by annotating it and moving the task to a separate thread.

# However, that’s not what happens in regular scenarios, like in regular CRUD-based apps. Right?

# This synchronous behavior of code execution is known as blocking since the flow of execution is blocked until the external function returns the response.

# What is non-blocking?
# In the non-blocking approach, the flow doesn’t wait for the external function that is called to return the response. It just moves on to execute the following lines of code. This approach is a little inconsistent compared to the blocking approach since the external function might not return anything or throw an error. Still, the following code in the sequence is executed.

# The non-blocking approach facilitates IO(Input-Output) intensive operations. IO intensive operations include the disk and other hardware-based operations, communication, network operations, etc.

# We will continue this discussion in part two of the event-driven architecture lesson.
