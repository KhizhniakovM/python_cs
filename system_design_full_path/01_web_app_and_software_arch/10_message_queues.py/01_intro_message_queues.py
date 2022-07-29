# Introduction to Message Queues
# In this lesson, you will learn about message queues and their functionalities.

# What is a message queue?
# A message queue, as the name says, is a queue that routes messages from the source to the destination or the sender to the receiver following the FIFO (First in , first out) policy.

# The message that is added to the queue first is delivered first. Besides FIFO, messages queues also support priority-based message delivery. Messages have a priority assigned to them and the queue processes the messages based on the priority set. These message queues are called priority queues.

# system_design_full_path/images/055.png

# Features of a message queue
# Message queues facilitate asynchronous behavior. We have already learned what asynchronous behavior is in the AJAX lesson. Asynchronous behavior allows the modules to communicate in the background without hindering their primary tasks.

# Message queues facilitate cross-module communication, which is key in service-oriented and microservices architecture. They enable communication in a heterogeneous environment, providing temporary storage for storing messages until they are processed and consumed by the consumer.

# Let’s look at a real-world example to understand message queues.

# Real-world example of a message queue
# Take an email service as an example. Both the sender and receiver of the email don’t have to be online at the same time to communicate with each other. The sender sends an email, and the message is temporarily stored on the message server until the recipient comes online and reads the message.

# Message queues enable us to run background processes, tasks, and batch jobs. Speaking of background processes, let’s understand this better with the help of a use case.

# Think of a user signing up on a portal. After they sign up, they are immediately allowed to navigate to the application’s homepage, but the sign-up process isn’t complete yet. The system has to send a confirmation email to the user’s registered email id. Then, the user has to click on the confirmation email to confirm the sign-up event.

# However, the website cannot keep the user waiting until it sends the email to the user. They are immediately allowed to navigate to the application’s home page to avert them from bouncing off.

# So, the task of sending a sign-up confirmation email to the user is assigned as an asynchronous background process to a message queue. It sends an email while the user continues to browse the website.

# This is how message queues are leveraged to add asynchronous behavior to an application. Message queues are also used to implement notification systems similar to Facebook notifications. I’ll discuss this in the upcoming lessons.

# Moving on to the batch jobs.

# Message queue in running batch jobs
# Do you remember the stock market game use case from the caching lesson where I discussed how I leveraged a cache to reduce application hosting costs?

# The batch job, which updated the stock prices at regular intervals in the database, was run by a message queue.

# So, we now know what a message queue is and why we use it in applications. In a message queue, there is a message sender called the producer, and there is a message receiver called the consumer.

# Both the producer and the consumer don’t have to reside on the same machine to communicate. This is pretty obvious.

# While routing messages through the queue, we can define several rules based on our business requirements. Adding priority to the messages is one that I pointed out. Other essential queuing features include message acknowledgments, retrying failed messages, etc.

# Speaking of the size of the queue, how big can it get, how many messages it can contain? Well, there is no definite size to it, and it can be an infinite buffer, considering the business has unlimited resources to run its infrastructure.

# Now, let’s look into the messaging models widely used in the industry, beginning with the publish-subscribe message routing model, which is responsible for how we consume information at large.
