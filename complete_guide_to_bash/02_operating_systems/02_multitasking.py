# Multitasking
# Learn why multitasking is so important.

# * MARK: - Multitasking
# All modern OSs support multitasking. This means they can execute multiple programs in parallel. The systems
# with this feature displaced the OSs without it. Why is multitasking so important?

# * MARK: - Efficient usage of computers
# The challenge of efficient usage of computers arose in the 1960s. Computers were relatively expensive
# at that time. Only large companies and universities were able to buy them. These organizations counted
# every minute they worked with their machines. They could not accept any idle time of the hardware because
# of its huge cost.

# * MARK: - Batch processing
# Earlier operating systems executed programs one after another without delays. This approach saved time
# originally spent switching computer tasks. If we were to use such an OS, we would need to prepare several
# programs and their input data in advance. Then, we would have to write the programs and their data onto a
# storage device, like a magnetic tape, and load the tape into the computer’s reading device. Afterward, the
# computer would execute the programs sequentially and print their results to an output device—for example, a
# printer. This mode of operation is called batch processing.

# ../images/002.png
# ../images/003.png
# ../images/004.png
# ../images/005.png
# ../images/006.png
# ../images/007.png
# ../images/008.png
# ../images/009.png

# Batch processing increased the efficiency of computers in the 1960s. by automating program loading.
# Therefore, human operators became unnecessary for this task. However, the computers still faced bottlenecks.

# A bottleneck is a component or resource of an information system that limits its overall performance or bandwidth.

# The computational power of processors increased significantly every subsequent year. However, the
# speed of peripherals remained almost the same. This difference in speed led to CPUs often idling while
# waiting for input or output.

# * MARK: - Why the CPU waits
# Why did the CPU idle and wait for peripheral devices? Let’s go over an example that can clarify this.
# Imagine that a computer from the 1960s runs programs one by one. It reads data from a magnetic tape and
# prints the results on the printer. The OS loads each program and executes its instructions. Then, it loads
# the next one, and so on.

# The problem occurs when the computer reads the data and prints the results. At the CPU’s scale, a huge
# amount of time is required to read the data on the magnetic tape. This time is enough for the processor
# to perform many calculations. However, the processor does not do that. The reason is that the currently
# loaded program occupies all computer resources. The same CPU idling happens when the computer prints the
# results because the printer is a slow mechanical device.

# ../images/009.png
# ../images/010.png
# ../images/011.png
# ../images/012.png

