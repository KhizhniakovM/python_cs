# Reasons For System Failures
# In this lesson, we will understand the common reasons for system failure.

# Before delving into the HA system design, fault-tolerance, and redundancy, we will first discuss the common reasons why systems fail.

# Software crashes
# I am sure you are pretty familiar with software crashes. Applications crash all the time, be it on a mobile phone or a desktop.

# We also have to deal with corrupt software files. Remember the BSOD blue screen of death in Windows? OS crashing, memory-hogging unresponsive processes. Likewise, software running on cloud nodes crashes unpredictably and takes down the entire node.

# Hardware failures
# Another reason for system failure is hardware crashes, including overloaded CPU and RAM, hard disk failures, nodes going down, and network outages.

# Human errors
# This is the biggest reason for system failures. It includes flawed configurations and whatnot. Google made a tiny network configuration error, and it took down almost half of the internet in Japan. An interesting read.

# Planned downtime
# Besides the unplanned crashes, there are planned downtimes that involve routine maintenance operations, patching software, hardware upgrades, etc.

# These are the primary reasons for system failures. Now, let’s talk about how HA systems are designed to overcome these system downtime scenarios.
