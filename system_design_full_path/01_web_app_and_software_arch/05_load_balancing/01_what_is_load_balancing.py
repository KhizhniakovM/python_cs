# Introduction to Load Balancing
# In this lesson, you will understand load balancing and the need for it in web applications.

# What is load balancing?
# Load balancing enables our service to scale well and stay highly available when the traffic load increases. Load balancing is facilitated by load balancers, making them a key component in the web application architecture.

# Load balancers distribute heavy traffic load across the servers running in the cluster based on several different algorithms. This averts the risk of all the traffic converging to a single or a few machines in the cluster.

# If the entire traffic on a particular service converges only to a few machines, this will cause an overload, subsequently spiking the latency, also bringing down the application’s performance. The excess traffic might also result in the server nodes going offline. Load balancing helps us avoid all this mess.

# While processing a user request, if a server goes down, the load balancer automatically routes the future requests to other up and running server nodes in the cluster. This enables the service as a whole to stay available.

# Load balancers act as a single point of contact for all the client requests.

# system_design_full_path/images/027.png

# They can also be set up at the application component level to efficiently manage traffic directed towards any application component, be it the backend application server, database component, message queue, or any other. This is done to uniformly spread the request load across the machines in the cluster powering that particular application component.

# system_design_full_path/images/028.png

# Performing health checks of the servers with load balancers
# To intelligently route all the user requests to the active nodes in the cluster, a load balancer should be well aware of their running status.

# To ensure that the user request is always routed to the machine that is up and running, load balancers regularly perform health checks on the machines in the cluster.

# system_design_full_path/images/029.png

# Ideally, a load balancer maintains a list of machines that are up and running in the cluster in real-time, and the user requests are forwarded to only those machines in service. If a machine goes down, it is removed from the list.

# Machines that are up and running in the cluster are known as in -service machines, and the servers that are down are known as out-of-service instances.

# For the record, Node, Server, Server Node, Instance, and Machine all mean the same thing and can be used interchangeably.

# After the out-of-service instance comes back online and becomes in -service, the load balancer updates its list and starts routing the future requests to that particular instance all over again.

# Okay! In the next few lessons, you will discover how load balancers work. To understand that well, you need to first understand the Domain Name System(DNS) that we will discuss in the lesson up next.
