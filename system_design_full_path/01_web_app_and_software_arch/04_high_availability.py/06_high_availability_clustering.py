# High Availability Clustering
# In this lesson, you will cover high availability clustering.

# Now that we have a clear understanding of high availability, let’s talk a bit about the high-availability cluster.

# A high availability cluster, also known as the fail-over cluster, contains a set of nodes running in conjunction with each other that ensures the high availability of the service.

# The nodes in the cluster are connected by a private network called the heartbeat network that continuously monitors the health and the status of each node in the cluster.

# A single state across all the nodes in a cluster is achieved with the help of a shared distributed memory and a distributed coordination service like the Zookeeper.

# system_design_full_path/images/026.png

# To ensure availability, HA clusters use several techniques such as disk mirroring/Redundant Array of Independent Disks(RAID), redundant network connections, redundant electrical power, etc. All the possible components having a single point of failure are made redundant to ensure the availability of the service.

# Multiple HA clusters run together in one geographical zone ensuring minimum downtime and continual service. If you wish to delve more into clustering please go through my cloud course.

# Alright, Folks! So now we have a pretty good understanding of scalability and high availability. These two concepts are crucial to software system design.

# Let’s move on to the next chapter, where we discuss load balancing in web applications.
