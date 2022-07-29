# Introduction
# In this lesson, you will be introduced to the concept of caching and why it is important for application performance.

# Before getting on with the lesson, I want to ask you a question. When you visit a website and request certain information from the server, how long do you wait for the response?

# 5 seconds? 10? … 15 seconds? … 30? I know, I know, I am pushing it … 45 seconds? What? Still no response?

# What option are you left with than to bounce off and visit another website for your information. We are impatient creatures, and we want our answers quick. Our application needs to have minimum latency and implementing caching enables us to stop users from bouncing off to other websites.

# What is caching?
# Caching is key to the performance of any kind of application. It ensures low latency and high throughput. An application with caching will undoubtedly do better than an application without caching, simply because a cache intercepts all the requests darting towards the database and provides the response in no time.

# Intercepting the database requests allows the database to free its resources to work with other requests, requesting uncached data, for open connections or write operations.

# Implementing caching in a web application means copying frequently accessed data from the database, which is disk-based hardware, and storing it in RAM(Random access memory) for quick response.

# system_design_full_path/images/052.png

# RAM provides faster access than disk-based hardware, ensuring low latency and high throughput. Throughput means the number of network calls or request-response cycles between the client and the server within a stipulated time.

# When an application server requests data from the database, it can be called the client and the database would be the server.

# A cache can always handle more read requests than a database since it stores the data in a key-value pair and does not have to do much computation when returning the data in contrast to a database.

# Frequently requested data queried from the database with the help of several table joins can be cached to avert the same joins query to be run every time the same data is requested. This increases throughput, improves performance and saves resources.

# Caching dynamic data
# With caching, we can cache both the static and the dynamic data. Dynamic data changes more often and has an expiry time or a TTL(Time to live). After the TTL ends, the data is purged from the cache, and the newly updated data is stored in it. This process is known as cache invalidation.

# Though the data TTL should be long enough to make effective use of caching, caching won’t help much if the data changes too often, for instance, the price of a stock, the score of a cricket or a baseball match.

# Caching static data
# Static data consists of images, font files, CSS, and similar files. It also includes data such as customer data, their name, age, address, social id, photos, etc. This is the kind of data that doesn’t change often and can easily be cached either on the client-side in their browser, CDN or on the server, depending on the sensitivity.

# In the next lesson, we will cover how to decide if we really need a cache in our application.
