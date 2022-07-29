# Point-to-Point Model
# In this lesson, we will learn about the point-to-point messaging model.

# What is a point-to-point model?
# In a point-to-point model, a message from the producer is consumed by only one consumer.

# It’s like a one-to-one relationship, while a publish-subscribe model is a one-to-many relationship.

# system_design_full_path/images/058.png

# Though based on the business requirements, we can set up multiple combinations in this messaging model, including adding multiple producers and consumers to a queue. However, only one consumer will consume a message sent by the producer. This is why this model is called a point-to-point queuing model. It’s not a broadcast of messages rather an entity to entity communication.

# Messaging protocols
# There are two popular protocols when working with message queues: AMQP Advanced Message Queue Protocol and STOMP Simple or Streaming Text Oriented Message Protocol.

# Since they are protocols, I won’t be delving into them further. Every messaging technology, RabbitMQ, ActiveMQ, Apache Kafka, will have its own implementations of these protocols.

# Well, this is pretty much it on the queuing models. In the lesson up next, we will get an insight into how notification systems work with message queues.
