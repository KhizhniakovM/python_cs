# Understanding DNS – Part 1
# In this lesson, you will learn what the domain name system(DNS) is and how it works.

# Every machine that is online and is a part of the World Wide Web(WWW) has a unique IP address that enables it to be contacted by other machines on the web using that particular IP address.

# IP stands for Internet Protocol. It’s a protocol that facilitates the delivery of data packets from one machine to another using their IP addresses.

# 2001: db8: 0: 1234: 0: 567: 8: 1 - This is an example of a machine’s IP address. The server that hosts our website will have a similar IP address. To fetch content from that server, a user has to type in the unique IP address of the server in their browser’s URL tab and hit enter to interact with the website’s content.

# Naturally, it is not viable to type in the website’s IP address from memory every time we visit a particular website. Even if we try to, how many IP addresses do you think you can remember?

# Typing in domain names, for instance, amazon.com, is a lot easier than working directly with IP addresses. I think we can all agree on this.

# Domain name system
# Domain name system, commonly known as DNS, is a system that averts the need to remember long IP addresses to visit a website by mapping easy-to-remember domain names to IP addresses.

# amazon.com is a domain name that is mapped to its unique IP address by the DNS so that we are not expected to type in the IP address of amazon.com into our browsers every time we visit that website.

# Now let’s explore how DNS works?

# How does a domain name system work?
# When a user types in the URL of the website in their browser and hits enter, this event is known as DNS querying.

# Four key components, or a group of servers, make up the DNS infrastructure. These are:

# DNS Recursive nameserver aka DNS Resolver
# Root nameserver
# Top-Level Domain nameserver
# Authoritative nameserver

# system_design_full_path/images/030.png

# In the next lesson, we will learn how the DNS query lookup process works and the role of these servers in the lookup process.
