# Peer-to-Peer Architecture – Part 1
# In this lesson, which is part one of the discussion on peer-to-peer architecture, we will take a deep dive into it.

# Peer-to-peer(P2P) architecture is the base of blockchain tech. We’ve all used it at some point in our lives to download files via torrent. So, I guess you have a little idea of what it is . You are also probably familiar with terms like seeding, leeching, etc. Even if you aren’t, you’ll learn everything in this lesson.

# Let’s begin the lesson with a discussion on what a P2P network is .

# What is a peer-to-peer network?
# A P2P network is a network in which computers, also known as nodes, can communicate with each other without a central server. The absence of a central server rules out the possibility of a single point of failure. All the computers in the network have equal rights. A node acts as a seeder and a leecher at the same time. So, even if some of the computers/nodes go down, the network and the communication are still up.

# A seeder is a node that hosts the data on its system and provides bandwidth to upload the data to the network, and a leecher is a node that downloads the data from the network.

# system_design_full_path/images/071.png

# What does a central server mean?
# Think of a messaging app. When two users communicate, the first user sends a message from their device, and the message moves on the server of the organization hosting the messaging service. From there, the message is routed to the destination, that is, the device of the user receiving the message.

# The server of the organization is the central server. These systems are also known as centralized systems.

# Now you might think, Okay, so, what’s the issue when communicating with my friend via a central server? I have never faced any issues that I can recall.

# Downsides of centralized systems
# Here are a few important things to consider:

# First, the central server has access to all your messages. The admin can read them, share them with their associates, laugh about them, and so on. The gist is that our communication is not really secure. Even though the businesses say that their entire message pipeline is encrypted and stuff, data breaches happen, governments get access to our data
# also, it is sold to third parties for fat profits. Do you think these messaging apps are really secure? Should the national security or enterprise officials sitting at the top of the food chain use these central server messaging apps for communication?
# Second, with centralized systems, we are stranded in case of natural disasters, earthquakes, zombie attacks, massive infrastructural failures, or the organization going out of business. There is no way to communicate with our friends across the globe. Think about it.
# Third, let’s say you start creating content on social media. You have built a pretty solid following on it, you spend 100 + hours a week to put out the best content ever, and you have worked years to reach this point of success. Then one fine day, out of the blue, the organization pokes you and says, “Hey!! Good job, but, aaaaa… for some reason, which we can’t talk about, we have to let your data go. We just don’t like your content.” Shift + Del and whoosh… all your data disappears like a ghost when sprinkled holy water. What are you going to do next? If you are already a content creator or are active on social media, this happens all the time, and you know that.
# Fortunately, P2P networks are resilient to all these scenarios due to their design. They have a decentralized architecture.

# system_design_full_path/images/072.png

# What is a decentralized architecture?
# Nobody has control over your data, and nobody has the power to delete it because all the participating nodes in a P2P network have equal rights. During a zombie apocalypse, when the huge corporation servers are dead or on fire, we can still communicate with each other via a peer-to-peer connection.

# Though I’ve nothing against any of the corporations: ) They’ve made our lives really easy. It’s just I am making you aware of all the possible scenarios out there.

# Advantages of a peer-to-peer network
# Here is another use case where a peer-to-peer network rocks!! Imagine you’ve finally returned home from a trekking tour after visiting all seven continents around the world. Things couldn’t seem more beautiful and emotionally satisfying.

# You have documented the entire expedition with state-of-the-art cameras and equipment in super ultra HD 4K quality, which has stacked up the hard drive of your computer. You are super excited to share all the videos and photos of the tour with your friends.

# But how do you really plan to share the data, which is several gigabytes, with your friends?

# Facebook Messenger, WhatsApp?

# Messengers have a memory limit, so they aren’t even an option. Well, you could upload all the stuff on the cloud and share the link with your folks, but hold on. Uploading that much data needs some serious storage space, which would mean some serious money. Would you be in the mood to spend anymore after such a long trip?

# No problem. We can write all the files on a physical memory like a DVD or a portable hard drive and share them with our friends, right?

# Well, yes, we can. However, physical memory has its costs, and writing files for every friend is time-consuming, expensive, and resource-intensive. I get it you are tired already. And, oh!! By the way, we have to courier the disks to our friends put up across the globe. We need to add additional courier expenses and be okay with the time it would take for the courier to be delivered.

# We’ve got this, don’t you worry!! We’ll find out some way. So, now what options do we have remaining? Think about it.

# Hey, why don’t we use peer-to-peer file sharing? That would be awesome. With P2P peer-to-peer file sharing, we can easily share all the content with friends with minimal costs and fuss.

# Beautiful!!

# We can use a P2P protocol like BitTorrent for it. BitTorrent is the most commonly used P2P protocol for distributing data and large electronic files over the internet. It has approx. 25 million concurrent users at any point in time.

# So, we will create a torrent file of our data and share it with all our folks. They just have to put the torrent in their BitTorrent client and start downloading the files to their systems while hosting/seeding the files simultaneously for others to download.

# So, these are a few use cases where a P2P network rocks. In the next lesson, which is the second part of the P2P architecture, we will take a deep dive into the architecture.
