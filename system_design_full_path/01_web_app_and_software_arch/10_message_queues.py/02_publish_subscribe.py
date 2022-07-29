# Publish-Subscribe Model
# In this lesson, you will learn about the publish-subscribe model, including when it is used and what exchanges are in messaging.

# What is a publish-subscribe model?
# A publish-subscribe model, aka pub-sub, is a model that enables a single or multiple producers to broadcast messages to multiple consumers.

# system_design_full_path/images/056.png

# A good analogy of this model is a newspaper service. Consumers subscribe to a newspaper service, and the service delivers the news to multiple consumers of its service every single day.

# In the online world, we often subscribe to various topics, such as sports, politics, economics, etc., in applications to be continually notified of the latest updates on that particular segment.

# Exchanges
# To implement the pub-sub pattern, message queues have exchanges that push the messages to the message queues based on the exchange type and the set rules. Exchanges here are just like telephone exchanges that route messages from the sender to the receiver through the infrastructure based on certain logic.

# system_design_full_path/images/057.png

# There are different types of exchanges available in message queues, some of which are: direct, topic, headers, and fanout. Each exchange type has specific functionality and a use case.

# Different message queue technologies have different implementations of exchange types. I just brought up the commonly used exchange types in message queues.

# The fanout exchange will fit best for implementing a pub-sub pattern. It will push the messages to the queue and the consumers will receive the message broadcast. The relationship between the exchange and the queue is known as binding.

# Message queues and publish-subscribe pattern are responsible for delivering real-time news, updates, notifications on social apps to the end-users. The end-users follow certain pages, and they start receiving updates on the content published by those pages continually.

# In the upcoming lessons, I will discuss how real-time feeds and notification systems work in social networks powered by the message queues in detail.

# In the next lesson, let’s move on to the point-to-point messaging model.
