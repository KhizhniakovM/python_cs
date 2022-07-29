# Handling Concurrent Requests with Message Queues
# In this lesson, we will explore how concurrent requests are handled with a message queue.

# Using a message queue to handle the traffic surge
# In the distributed NoSQL databases lesson, we learned about eventual consistency and strong consistency. We discussed how both the consistency models come into effect when incrementing a “Like” counter value.

# Here is a quick insight into how we can use a message queue to manage a high number of concurrent requests to update an entity.

# When millions of users around the world update an entity concurrently, we can queue all the update requests in a high throughput message queue. Then, we can process them one by one in a First in First Out(FIFO) approach sequentially.

# This would enable the system to be highly available and open to updates while remaining consistent at the same time.

# Though implementing this approach is not as simple as it sounds, implementing anything in a distributed, real-time environment is not so trivial.

# Facebook handles concurrent requests on its live video streaming service with a message queue
# Facebook’s approach of handling concurrent user requests on its LIVE video streaming service is another good example of how queues can be used to efficiently handle the traffic surge.

# On the platform, when a popular person goes LIVE, there is a surge of user requests on the LIVE streaming server. To avert the incoming load on the server, Facebook uses cache to intercept the traffic.

# However, since the data is streamed LIVE, the cache often is not populated with real-time data before the requests arrive. Now, this would naturally result in a cache-miss, and the requests would move on to hit the streaming server.

# To avert this, Facebook queues all the user requests, requesting the same data. It fetches the data from the streaming server, populates the cache, and then serves the queued requests from the cache.

# Here is a recommended read on Facebook’s Live streaming architecture.

# Okay! Moving on. In the next chapter, we will take a swim into stream processing.
