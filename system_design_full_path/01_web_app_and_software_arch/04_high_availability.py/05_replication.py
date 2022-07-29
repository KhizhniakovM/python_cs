# Replication
# In this lesson, you will learn about replication as a high availability mechanism.

# Replication – Active-active HA mode
# Replication means having a number of similar nodes running the workload together. There are no standby or passive instances. When a single or a few nodes go down, the remaining nodes bear the load of the service.

# system_design_full_path/images/025.png

# This approach is also known as the Active-active high availability mode. In this approach, all the server instances are active at any point in time.

# Geographical distribution of workload
# As a contingency for natural disasters, regional power outages, and other big-scale failures, data center workloads are spread across different data centers across the world in different geographical locations.

# This eliminates a single point of failure in the context of data center zones. If a natural disaster wipes out a few data centers in a certain zone, other data centers in different geographical zones are still powering the application. Also, the latency is reduced significantly due to the proximity of data to the user due to the global replication of data centers.

# All highly-available fault-tolerant design decisions are subjective to how critical the system is? The odds of components failing and so on.

# Businesses often use multi-cloud platforms to deploy their workloads which ensures further availability. If things go south with one cloud provider, they have another to fail back over.
