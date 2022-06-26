# How the OS Works
# An overview of how the OS allows the interaction of application software with hardware.

# Why did we start to study programming by considering the OS? This is because OS features form the basis
# of an application. So, let’s consider how the OS works.

# * MARK: - OS operation
# The figure on the right side demonstrates the interaction between the OS, an application,
# and the computer hardware.

# Applications are programs that solve practical user tasks. Examples include text editors,
# calculators, and browsers. Hardware refers to all electronic and mechanical components of a computer.
# For example, hardware includes keyboards, monitors, central processors, and video cards.

# According to the figure on the right, an application does not directly interact with the hardware.
# Instead, it works through system libraries. The system libraries are part of the OS. There are rules
# to access the system libraries, and each application should follow them.

# ../images/001.png

# * MARK: - Application Programming Interface
# Learn how the OS acts as an API in a computer.

# API
# The Application Programming Interface (API) is the interface the OS provides to an application to interact
# with system libraries. In general, an API refers to a set of agreements between the interacting components
# of an information system. These agreements often become a well-known standard. For example, the POSIX standard
# describes the API for a portable OS. The standard guarantees the compatibility of the OS and applications.

# The OS’s kernel and device drivers are part of the OS. They dictate which hardware features the
# application can access. The kernel of the OS provides a mechanism for managing access to the hard drive.
# This mechanism is called a file system. Similarly, the OS manages access to all peripheral and internal
# devices of the computer. Besides the kernel, there are special programs called device drivers that help
# the OS to control devices.

# When the application interacts with system libraries, the libraries request the capabilities of the
# kernel and drivers. If we need a hardware feature and the OS does not support it, we cannot use it.

# When the application accesses the system library, it calls a library’s function. A function is a program
# fragment or an independent block of code that performs a certain task. We can imagine the API as a list
# of all available functions that the application can call. Besides this, the API describes the following
# aspects of the interaction between the OS and applications:

# 1. What action the OS performs when the application calls a specific system function
# 2. What data the function receives as input
# 3. What data the function returns as output?

# Both the OS and application should follow the API agreements. This guarantees the compatibility of their
# current versions and future modifications. Such compatibility is impossible without a well-documented and
# standardized interface.

# * MARK: - Limitations of bare-metal software
# We have discovered that some applications work without an OS. They are called bare-metal software. This
# approach works well in some cases. However, the OS provides ready-made solutions for interaction with
# the computer’s hardware.

# Without an OS, developers must take responsibility to manage hardware. It requires significant effort.
# Let’s imagine the variety of devices of a modern computer. The application should support all popular
# models of each device (for example, different video cards). Without such support, the application won’t
# work for all users.

# * MARK: - OS features via the API
# Let’s now consider the features the OS provides via the API. We can treat the computer’s hardware as
# resources. The application uses these resources to perform calculations. The API reflects the list of
# hardware features that the program can use. Also, the API dictates the order of interaction between
# several applications and the hardware.

# Here is an example. Two programs cannot simultaneously write data to the same area of the hard disk.
# There are two reasons for this:

# 1. A single magnetic head records data on the hard disk. The head can only do one task at a time.
# 2. One program can overwrite the data of another program in the same memory area. This leads to the loss of data.

# Therefore, we should place all requests to write data on the disk in a queue. Then, each request is
# performed separately, and the OS takes care of them.

# * MARK: - Computer Devices
# Learn about internal and peripheral devices. We’ll also discuss a component of the Windows OS.

# * MARK: - Peripheral and internal devices
# What is the difference between peripheral and internal devices?

# Peripherals are all devices that are responsible for permanently inputting, outputting, and storing data.
# Some examples are as follows:

# - Keyboard
# - Mouse
# - Microphone
# - Monitor
# - Speakers
# - Hard drive

# Internal devices are responsible for processing data—in other words, for executing programs. Some examples
# are as follows:

# - Central Processing Unit (CPU)
# - Random-Access Memory (RAM)
# - Video card or graphics processing unit (GPU)

# The OS provides access to the computer’s hardware. At the same time, the OS also provides functionality
# besides the hardware management to share with users’ applications. The system libraries grow from the
# program modules to serve the devices. However, some libraries of modern OSs provide complex algorithms
# for processing data. Let’s consider an example.

# * MARK: - Graphics device interface
# The Graphics Device Interface (GDI) is a component of the Windows OS. It provides algorithms to manipulate
# graphic objects. The GDI lets us create a user interface for our application with minimal effort. Then,
# we can use the monitor to display this interface.

# The system libraries with useful algorithms (like GDI) are the software resources of the OS. These
# resources are already installed on our computer. We just need to know how to use them. Besides this,
# the OS provides access to third-party libraries and their algorithms. We can install these libraries
# separately and use them in our applications.

# * MARK: - OS tasks
# The OS manages hardware and software resources. Also, it organizes the joint work of running programs.
# The OS performs several non-trivial tasks to launch an application. Then, the OS tracks its work. If
# the application violates some agreements, like memory usage, the OS terminates it. It also launches
# and executes programs, which we will later consider in detail.

# * MARK: - OS features
# If the OS is multi-user, it controls access to the data. This is an important security feature. This
# feature lets us access the following file system objects:

# - Files and directories we own
# - Files and directories that somebody shares with us

# A multi-user OS allows several people to use the same computer safely.

# 1. In summary, the modern OS has the following features:
# 2. It provides and manages access to the computer’s hardware resources.
# 3. It provides its own software resources.
# 4. It launches applications.
# 5. It organizes the interaction of applications with each other. It controls access to users’ data.

# It is impossible to launch several applications in parallel without the OS. When we develop an application,
# we have no idea how a user will launch it. The user can launch our application together with another one.
# In such cases, the OS responds by launching all applications. This means that the OS has enough information
# to allocate computer resources properly.

# * MARK: - Modern OSs
# Now, let’s consider modern operating systems. Today, we can pick any OS and get very similar features.
# However, their developers follow different approaches. This leads to implementation differences that can
# be important for some users.

# The software architecture refers to the implementation aspects of specific software and the solutions that
# led to them.

# * MARK: - Features of modern OSs
# All modern OSs have two features that determine the way users interact with them. These features are:

# - Multitasking
# - Graphical user interface
