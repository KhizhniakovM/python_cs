# A Baseball Game Ticket Booking Web Portal
# In this lesson, we'll discuss the case study of a baseball game ticket booking application.

# In this lesson, you’ll gain an understanding of the architecture and key points to consider when designing an application like a baseball game ticket booking portal.

# Let’s get started.

# Database
# Starting with the database, the sale of tickets online is key in this particular use case. We need to set up a foolproof payment system for the fans to buy tickets for their most awaited baseball game.

# For setting up payments, what database should we pick and why? You know it: ) Implementing an online payment system makes transactions and strong consistency vital. The database needs to be ACID compliant. This makes a relational database like MySQL an obvious pick for us.

# Handling concurrency
# Another essential thing to note is that the application should be designed to handle a high number of concurrent connections. There will be a surge of fans on the portal to buy tickets for the baseball game as soon as they are made available.

# Also, the number of requests will naturally be a lot more than the number of tickets available. At a point, there will be n requests to buy one ticket. We need to make sure the system handles this concurrent scenario well. How will you implement this scenario? Think about it.

# Message queue
# One way is to queue all the ticket buy requests using a message queue. Apply the FIFO principle. We talked about handling concurrent requests with the help of a message queue in the message queue lesson.

# Database locks and Caching
# Another approach is to use database locks. Use the correct transaction isolation level.

# A transaction isolation level ensures consistency in a database transaction. It ensures that at one point, only one transaction has access to a resource in the database. You can read more on isolation in database systems here. Also, read snapshot isolation.

# Transaction isolation levels can only be implemented with a transactional ACID-compliant database like MySQL.

# Generally, on e-commerce sites or travel booking websites, the number of tickets/products shown on the website is not accurate, and they are inconsistent cached values. When a user moves on to buy a particular ticket/product and checks out the cart, the system polls the database for the accurate count and locks the resource for the transaction.

# We will do the same for our website. There will be a lot of user events on the portal where the users just browse the website to look at the current price of the tickets and not buy them. Caching will avert the load on the database in this scenario.

# To implement caching, we can pick any of the popular caches, like Redis, Memcached or Hazelcast.

# Backend tech
# Speaking of the backend technology, we can pick from Java, Scala, Python, Go, etc.

# To send notifications to the users, we can pick a message queue like RabbitMQ or Kafka.

# Let’s move to the UI.

# User interface
# We don’t really need to establish a persistent connection with the server because the application is a CRUD-based app. Simple Ajax queries will work well.

# It’s a good idea to make the UI responsive, as fans will access it via devices with different screen sizes. The UI should be smart enough to adjust itself based on the screen size.

# We can either design the responsive behavior from the ground up using CSS3 or leverage a popular open-source responsive framework like Bootstrap JS.

# If you are fond of JavaScript frameworks, you can use React, Angular, Vue, etc. These frameworks are pretty popular in the industry, and businesses prefer to use them to standardize the behavior and the implementation of their applications.

# Well, this pretty much sums up the case study on a baseball ticket booking web portal. In the next chapter, let’s delve into mobile applications.
