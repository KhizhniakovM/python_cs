# GUI: An Overview
# Let's discuss the history of GUI, why it was needed, and how it was made available.

# * MARK: - Main types of computers
# Modern OSs are able to solve a wide range of tasks. These tasks depend on the type of computer where we
# run the OS. Below are the main types of computers:

# - Personal computers (PC) and notebooks
# - Smartphones and tablets
# - Servers
# - Embedded systems

# * MARK: - User interface
# We will consider OSs for PCs and notebooks only. Apart from multitasking, they provide a graphic user
# interface (GUI). This interface is the way to interact with the system: we launch applications, configure
# computer devices and OS components, all via the user interface. Let’s take a look at its history and how
# it reached its current state.

# * MARK: - History of UI
# Nobody worked with commercial computers interactively before 1960. Digital Equipment Corporation
# implemented the interactive mode for their minicomputer PDP-1 in 1959. It was a fundamentally new
# approach. Before that, IBM computers dominated the market in the 1950s. They worked in batch processing
# mode only. This mode automated program loading and provided high performance for tasks involving calculation.

# * MARK: - The SAGE project
# The idea of interactive work with computers appeared first in the SAGE (Semi-automatic Ground Environment)
# military project by the US Air Force. The goal of the project was to develop an automated air defense
# system to detect Soviet bombers.

# When working on the SAGE project, engineers faced an interesting problem. The user of the system needed to
# analyze data from radars in real-time and react as quickly as possible. However, existing methods of
# interaction with computers didn’t fit this task. They did not let the computer show information to the user
# in real-time and receive the user’s input at any moment.

# Engineers then came to the idea of interactive mode. They implemented it in the first interactive computer
# AN/FSQ-7 in 1955. The figure below shows this computer.

# The computer used a monitor with a cathode-ray tube to display information from radar. The light pen allowed
# the user to command the system.

# ? Drawbacks of batch processing
# The new way of interaction with computers became known in scientific circles and quickly gained popularity.
# The existing batch processing mode coped with program execution well. However, this mode was inconvenient for
# developing and debugging applications. Let’s suppose that we write a program for the computer with batch
# processing. We should prepare our code and write it to the storage device. When the device is ready, we put
# it in a queue. The computer’s operator takes devices from the queue and loads them to the computer one by one.
# Therefore, our task can wait in the queue for several hours. Now, assume that an error occurred in our program.
# In this case, we’d need to fix it, prepare the new version of the program, and write it to the device. We
# put the revised program in the queue again and then must wait for some time. Because of this workflow, we
# need several days to get even a small program working.

# ? Benefits of interactive mode
# The software development workflow differs when we use an interactive mode. We prepare our program and load
# it to the computer. Then, it launches the program and shows us results. Immediately, we can analyze a
# possible error, fix it, and relaunch the program. This workflow significantly accelerates the processes of
# software development and debugging tasks. Now, we spend a few hours on a task that would require days with
# batch processing.

# ? Challenges of the interactive mode
# Interactive mode brought new challenges for computer engineers. This mode required a system that reacted
# to user actions immediately. Also, providing a short reaction time required a new load-balancing mechanism.
# The concept of multitasking became a solution to this problem.

# ? Alternatives to the interactive mode
# There are alternatives to multitasking that still provide an interactive mode. For example, there are
# interactive single-tasking OSs like MS-DOS. MS-DOS was the system for cheap PCs of the 1980s.

# However, it was inadvisable to apply single-tasking in the 1960s when computers were too expensive.
# These computers executed many programs in parallel in a concept called time-sharing. It allowed several
# users to share expensive hardware resources. The single-tasking approach does not fit such a use case
# because it is not compatible with time-sharing.

# ? Single-tasking OSs
# When the first relatively cheap personal computers appeared in the 1980s, they used single-tasking OSs.
# Such systems required fewer hardware resources than their analogs with multitasking. Despite their simplicity,
# single-tasking OSs supported interactive mode for the currently running program. This mode became especially
# attractive for PC users.

# When interactive mode became more and more popular, computer engineers faced a new challenge. The existing
# devices to interact with computers turned out to be inconvenient. Magnetic tapes and printers were widespread
# through the 1950s and early 1960s. They did not fit interactive mode absolutely.

# * MARK: - GUI: TTY and CLI
# Learn about teletype and command-line interface.

# * MARK: - Teletype
# The Teletype (TTY) became a prototype of a device for interactive work with a computer. The figure on
# the right shows the Model 33 Teletype, one of the most popular devices of the 1960s. It is an electromechanical
# typewriter. Once two teletypes are connected, operators can send text messages to each other. The sender types
# text on their device. The keystrokes are transmitted to the receiver’s device, which prints out each received
# letter on paper.

# Computer engineers connected the Teletype to computers. This solution allowed the user to send text commands
# to the machine and receive results. Such a workflow became known as a command-line interface (CLI).

# The Teletype used the printer as an output device. It worked very slowly and required around 10 seconds
# to print a single line. The next step to develop the user interface was to replace the printer with the monitor.

# This increased the data output speed by several times. The new device with a keyboard and monitor was
# called the terminal. It replaced Teletypes in the 1970s.

# * MARK: - The command-line interface
# The figure below shows a modern command-line interface. We can see the terminal emulator application there.
# This application emulates the terminal device for the sake of compatibility. It allows us to run programs
# that work with the real terminal only.

# The emulator application in the figure below is called the terminal. The Bash command-line interpreter is
# running in the terminal window. The window displays the results of the ping and ls programs.

# ? Pros of the CLI
# The command-line interface is still in demand today. It has several advantages over the graphical
# interface, such as the following:

# - The CLI does not require as many resources as the GUI.
# - The CLI runs reliably on low-performance embedded computers, as well as on powerful servers.
# - If we use the CLI to access the computer remotely, we can use a low-bandwidth communication channel.
#   The server will receive our commands in this case.

# ? Cons of the CLI
# The command-line interface has some disadvantages.

# - Learning to use the CLI effectively is difficult and time-consuming.
# - The CLI has very limited features to output data. It does not allow us to draw visually appealing graphs or tables.
# - The first disadvantage is that we need to remember a great number of commands. Moreover, each command
#   has several modes that change its behavior. Therefore, we must keep those in mind, too. It takes some time
#   to remember at least a minimum set of commands for daily work.

# The second disadvantage is a consequence of CLI limitations. It allows us to use only alphanumeric symbols
# and special characters for input and output data. It does not support any graphical objects.

# * MARK: - GUI: TUI and Xerox
# Learn about text-based user interfaces and Xerox.

# ? Text-based user interface
# We can choose to make the command-line interface more user-friendly, by giving a hint to the user about
# available commands. This is done in the text-based user interface (TUI).

# The TUI uses box-drawing characters along with alphanumeric symbols and special characters. The box-drawing
# characters display the graphic primitives—lines, rectangles, triangles, etc.—on the screen. Primitives guide
# the user through the available actions they can take with the application.

# The figure below shows a typical text-based user interface. There is an output of system resource usage
# by the htop program.

# The additional performance gain of computers allowed OS developers to replace box-drawing characters with
# real graphic elements. Examples of such elements include windows, icons, buttons, and so on. It was the moment
# when the full-fledged graphical interface was introduced. Modern OSs provide this kind of interface.

# The figure below demonstrates the Windows GUI. We can see the desktop. There are windows of three
# applications there. The applications are Explorer, Notepad, and Calculator. They work in parallel.

# ? The first GUI
# The first GUI appeared in the Xerox Alto minicomputer (see the figure on the right). It was developed in
# the Xerox PARC research center in 1973.

# However, the graphical interface did not spread widely until the 1980s. The reason is that a GUI requires
# a lot of memory and high computer performance. PCs with such features were too expensive for regular users
# at that time. Apple produced the first relatively cheap PC with a GUI in 1983, called Lisa.
