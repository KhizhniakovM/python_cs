# Do I Need A Cache?
# In this lesson, we will discuss how to tell if we need caching in our application.

# It’s always a good idea to use a cache as opposed to not using it, especially if we have static data in our application. You’ll come across very few use cases where caching doesn’t help. We also need to remember that caching should be implemented wisely. If not, it can cause data inconsistency issues.

# It can be used at any layer of the application, with any component and there are no ground rules as to where it can and cannot be applied.

# The most common usage of caching is database caching. Caching helps alleviate the stress on the database by intercepting the requests being routed to it.

# Different components in the application architecture where the cache can be used

# system_design_full_path/images/053.png

# Across the architecture of our application, we can use caching at multiple places, right from the browser to the database component. Caching is used in the client browser to cache static data. It is used with the database to intercept all the data requests. It is used in the REST API implementation, also in cross-module communication in a microservices architecture, etc.

# Besides these components, I suggest you look for patterns. We can always cache the frequently accessed content on our website, be it from any component. There is no need to repeatedly poll any component for the same data when it can be cached.

# Think of joins in relational databases. They are notorious for making the response slow. More joins mean more latency. A cache can avert the need for running joins every time by storing the data in demand. Imagine how much this mechanism would speed up our application.

# Also, even if the database goes down for a while, the users won’t notice it since the cache would continue to serve the data requests.

# Caching is also the core of the HTTP protocol. We can store user sessions in a cache. Key-value data stores are primarily used to implement caching in web applications.
