# Multiprogramming
# Learn what multiprogramming is, and how it works.

# * MARK: - Multiprogramming
# Slow peripheral devices cause the CPU to idle. This problem led OS developers to the concept of
# multiprogramming. This concept implies that the OS loads several programs into the computer memory at
# the same time. The first program works as long as all resources it needs are available. It stops execution
# once a required resource is busy. Then, the OS switches to another program.

# We’ll go over an example. Let’s suppose that our application wants to read data from our hard disk. While
# the disk controller reads the data, it’s busy. It cannot process the following requests from the program.
# So, the application waits for the controller. In this case, the OS stops executing it and switches to the
# second program. The computer then executes the second program to its end or until it has all the required
# resources. When the second program finishes or stops, the OS switches tasks again.

# ../images/014.png
# ../images/015.png
# ../images/016.png
# ../images/017.png
# ../images/018.png
# ../images/019.png
# ../images/020.png
# ../images/021.png
# ../images/022.png

# Multiprogramming differs from modern OSs’ multitasking. Multiprogramming fits the batch processing mode very
# well. However, this load balancing concept is not suitable for interactive systems.

# * MARK: - What is an interactive system?
# An interactive system considers each user action—for example, a keystroke—an event. The system
# should process events as they happen. Otherwise, the user cannot work with the system.

# We’ll go over an example of workflow with an interactive system. Let’s suppose that we type text in a
# document. We press a key and expect to see the corresponding symbol on the screen. If the computer
# requires several seconds to process our keystroke and display the symbol, we cannot work efficiently.
# Most times, we will wait and check if the computer processed our keystroke or not.

# Multiprogramming cannot handle events in the interactive system. This is because we cannot predict when
# task switching occurs. The OS switches tasks when a program finishes or when it requires a busy resource.
# Let’s suppose that our text editor is not an active program now. Then, we don’t know when it will process
# our keystroke. It can happen in a second, or in several minutes. This is unacceptable for a good user interface.

# * MARK: - Task scheduler
# The multitasking concept solves the task of processing events in interactive systems. There were several
# versions of multitasking before it reached its current state. Modern OSs displace multitasking with
# pseudo-parallel task processing. The idea behind it is to allow the OS to choose an appropriate task for
# execution at the given moment. The OS takes into account the priorities of the running programs. Therefore,
# a higher priority program receives hardware resources more often than a lower priority one. The OS kernel
# provides this task-switching mechanism. It is called a task scheduler.

# * MARK: - Pseudo-parallel processing
# Pseudo-parallel processing means that the computer executes one task only at any given time. However,
# the OS switches tasks so quickly that we can suppose the processing of several programs at once. This
# concept allows the OS to react immediately to any event, even though every program and OS component uses
# hardware resources at strictly defined moments.

# There are computers with multiple processors, or with multi-core processors. Only these computers can execute
# several programs at once. The number of the running programs is approximately the number of cores of all processors.

# * MARK: - Computers can have multiple cores
# The preemptive multitasking mechanism with constant task switching works well on such systems. It’s a universal
# approach that balances the load regardless of the number of cores. This way, the computer responds to the user’s
# actions quickly, and the number of processor cores does not matter.
