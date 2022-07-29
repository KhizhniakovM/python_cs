# DNS Load Balancing
# In this lesson, we will cover DNS load balancing.

# DNS load balancing
# In the previous lesson, we discussed how the DNS query lookup process works and the role of different servers in the domain name system. The end server, in the lookup chain, is the authoritative server, which returns the IP address of the domain.

# When a large-scale service such as amazon.com runs, it needs way more than a single machine to run its services. A service as big as amazon.com is deployed across multiple data centers in different geographical locations across the globe.

# To spread the user traffic across different clusters in different data centers. There are various ways to set up load balancing. In this lesson, we will discuss DNS load balancing, which is set up at the DNS level on the authoritative server.

# system_design_full_path/images/032.png

# DNS load balancing enables the authoritative server to return different IP addresses of a particular domain to the clients. Every time it receives a query for an IP, it returns a list of IP addresses of a domain to the client.

# With every request, the authoritative server changes the order of the IP addresses in the list in a round-robin fashion.

# As the client receives the list, it sends out a request to the first IP address on the list to fetch the data from the website. The reason for returning a list of IP addresses to the client is to enable it to use other IP addresses in the list in case the first doesn’t return a response within a stipulated time.

# When another client sends out a request for an IP address to the authoritative server, it re-orders the list and puts another IP address at the top of the list following the round-robin algorithm.

# Also, when the client hits an IP, it may not necessarily hit an application server. Instead, it may hit another load balancer implemented at the data center level that manages the clusters of application servers.

# Limitations of DNS load balancing
# DNS load balancing is largely used by companies to distribute traffic across multiple data centers that the application runs in . However, this approach has several limitations.

# For instance, it does not take into account the current load on the servers, the content they hold, their request processing time, their in -service status, and so on.

# Also, since these IP addresses are cached by the client’s machine and the DNS Resolver, there is always a possibility of a request being routed to a machine that is out of service.

# DNS load balancing, despite its limitations, is preferred by companies because it is an easy and less expensive way of setting up load balancing on their services.

# Recommended Read – Round Robin DNS
