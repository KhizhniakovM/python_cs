# Types of Scalability
# In this lesson, we will explore the two types of scaling: Vertical and Horizontal.

# To scale well, an application needs solid computing power. The servers should be powerful enough to handle increased traffic loads.

# There are two ways to scale an application:

# Vertically
# Horizontally

# What is vertical scaling?
# Vertical scaling means adding more power to our server. Let’s say our app is hosted by a server with 16 gigs of RAM. To handle the increased load, we now augment the RAM to 32 gigs. Here, we have vertically scaled the server.

# ../../images/019.png

# Ideally, when the traffic starts to build on the app, the first step should be to scale vertically. Vertical scaling is also called scaling up.

# In this type of scaling, we augment the power of the hardware running the app. This is the simplest way to scale as it doesn’t require any code refactoring or the need to make any complex configurations and so on. I’ll discuss in the next lesson why code refactoring is needed when we horizontally scale our app.

# However, there is only so much we can do when scaling vertically. There is a limit to the compute power we can augment for a single server.

# A good analogy would be to think of a multi-story building. We can keep adding floors to it but only up to a certain point. What if the number of people in need of a flat keeps rising? We can’t scale the building up to the moon for obvious reasons.

# Now is the time to build more buildings. This is where horizontal scalability comes in .

# When the traffic is too large to be handled by a single server, we bring in more servers to work together.

# What is horizontal scaling?
# Horizontal scaling, also known as scaling out, means adding more hardware to the existing hardware resource pool. This increases the computational power of the system as a whole.

# ../../images/020.png

# With this, the increased traffic influx can be efficiently dealt with. And there is no limit to how much we can scale horizontally, assuming we have infinite resources. We can keep adding servers after servers, setting up data centers after data centers.

# Horizontal scaling also allows us to scale dynamically in real-time as the traffic on our website climbs and drops over a period of time. Dynamic scaling is not possible when scaling vertically.

# Cloud elasticity
# The most prominent reason cloud computing became mainstream in the industry is the ability of the cloud to scale dynamically. In case of the traffic climb, the cloud adds additional servers to the hardware resource pool and when it drops, the servers added are removed.

# The ability to use and pay only for the hardware resources used by the website got popular with businesses for obvious economic reasons.

# The process of adding and removing servers, stretching and returning to the original infrastructural computational capacity, on the fly is popularly known as cloud elasticity. It saves businesses truckloads of money every single day.

# If you wish to know in detail how cloud platforms scale our apps and make them highly available. I’ve discussed the concept in my cloud computing 101 course how clustering works and how cloud companies deploy our apps across continents.

# Having multiple server nodes on the backend also helps the website stay online even if a few server nodes crash. This is known as high availability. We’ll get to that in the upcoming lessons.
