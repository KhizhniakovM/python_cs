# Federated Architecture
# In this lesson, we will discuss federated architecture.

# What Is federated architecture?
# Federated architecture is an extension of decentralized architecture. It powers social networks like Mastodon, Minds, Diaspora, etc.

# The term federated in a general sense means a group of semi-autonomous entities that exchange information with each other. A real-world example of this is looking at different states in a country managed by the state governments. They are partially self-governing and exercise power to keep things running smoothly. Then, those state governments share information with each other and with a central government making a complete autonomous government.

# This is just an example. From a technical standpoint, the federated model is under continual research, development, and evolution. There are no standard rules. Developers and architects can have their own designs in place.

# How is federated architecture implemented in decentralized social networks?
# As shown in the illustration below, a federated network has entities called servers or pods. A large number of nodes subscribe to the pods. There are several pods in the network that are linked to each other and share information.

# The pods can be hosted by individuals and as new pods are hosted and introduced to the network, the network keeps growing.

# In case the link between a few pods breaks temporarily, the network is still up. Nodes can still communicate with each other via the pods they are subscribed to.

# system_design_full_path/images/074.png

# What is the need for Pods? Can’t the nodes just be linked to each other like in a regular peer-to-peer network?

# What is the need for pods?
# Pods facilitate node discovery. In a peer-to-peer network, there is no way of discovering other nodes, and we would just sit in the dark if it weren’t for a centralized node registry or something.

# The other way is to run a scan through the network to discover other nodes. This is a time-consuming and tedious task. Why not just have a pod instead?

# Well, I believe you now have a fundamental understanding of the p2p architecture and the decentralized web. Let’s move on to the next lesson, where we talk about picking the right server-side technology.
