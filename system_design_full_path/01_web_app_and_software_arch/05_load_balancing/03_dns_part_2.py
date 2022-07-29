# Understanding DNS – Part 2
# This lesson continues our discussion on the domain name system.

# In this lesson, you will get an insight into the complete DNS query lookup process and understand the role of different servers in the DNS infrastructure.

# Lets’ begin.

# When the user hits enter after typing in the domain name into their browser, the browser sends a request to the DNS Recursive nameserver, also known as the DNS Resolver.

# The role of DNS Resolver is to receive the client request and forward it to the Root nameserver to get the address of the Top-Level domain nameserver.

# The DNS Recursive nameserver is generally managed by our ISP(Internet service provider). The whole DNS system is a distributed system setup in large data centers managed by internet service providers.

# These data centers contain clusters of servers optimized to process DNS queries in minimal time in milliseconds.

# Once the DNS Resolver forwards the request to the Root nameserver, the Root nameserver returns the address of the Top-Level domain nameserver in response. As an example, the top-level domain for amazon.com is .com.

# Once the DNS Resolver receives the address of the top-level domain nameserver, it sends a request to it to fetch the details of the domain name. Top Level domain nameservers hold the data for domains using their top-level domains.

# For instance, the .com top-level domain nameserver will contain information on domains using .com. Similarly, a .edu top-level domain nameserver will hold information on domains using .edu.

# Since our domain is amazon.com, the DNS Resolver will route the request to the .com top-level domain name server.

# Once the top-level domain name server receives the request from the Resolver, it returns the IP address of the amazon.com domain name server.

# amazon.com domain nameserver is the last server in the DNS query lookup process. This nameserver is responsible for the amazon.com domain and is also known as the Authoritative nameserver. The owner of the domain name owns this nameserver.

# Then, DNS Resolver fires a query to the Authoritative nameserver, and it returns the IP address of the amazon.com website to the DNS Resolver.

# DNS Resolver caches the data and forwards it to the client.

# On receiving the response, the browser sends a request to the amazon.com website’s IP address to fetch data from their servers.

# Often all this DNS information is cached, and the DNS servers don’t have to do so much rerouting every time a client requests an IP of a certain website.

# The DNS information of websites that we visit also gets cached in our local machines, that is , our browsing devices with a TTL (Time to live).

# All modern browsers do this automatically to cut down the DNS query lookup time when revisiting a website.

# This is how the entire DNS query lookup process works.

# system_design_full_path/images/031.png

# In the next lesson, let’s get an insight into DNS load balancing.
