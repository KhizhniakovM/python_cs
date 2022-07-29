# Hexagonal Architecture
# In this lesson, you will learn about hexagonal architecture.

# What is hexagonal architecture?
# The hexagonal architecture consists of three key components:

# Ports
# Adapters
# Domain
# The focus of this architecture is to make components of an application: independent, loosely coupled, and easy to test.

# The application should be designed in a way such that it can be tested by both humans and automated tests, with and without a UI, with mock databases and mock middleware, without making any changes or adjustments to the code.

# system_design_full_path/images/069.png

# The architectural pattern holds the domain at its core, which is business logic. On the outside, the outer layer has ports and adapters. Ports act like an API as an interface. All the input to the app goes through the interface.

# The external entities don’t have any direct interaction with the domain, the business logic. The adapter is the implementation of the interface. Adapters convert the data obtained from the ports to be processed by the business logic. The business logic lies isolated at the center, and all the IO input-output is at the edges of the structure.

# The hexagonal shape of the structure doesn’t have anything to do with the pattern. It’s just a visual representation of the architecture. Initially, the architecture was called the ports and the adapter pattern. Later, the name hexagonal stuck.

# The ports and the adapter analogy comes from computer ports as they act as the interface to the external devices for the input to the system. And the adapter converts the signals obtained from the ports to be processed by the chips inside.

# Real-world code implementation
# Zeroing in on the real-world code implementation, isn’t this what we already do with the layered architecture approach? We have different layers in our applications. We have the controller, then the service layer interface, the class implementations of the interface, the business logic that goes in the domain model, and a bit in the service, business, and repository classes.

# system_design_full_path/images/070.png

# Well, the hexagonal approach is an evolved layered architecture. There is not much difference. There is this one issue with the layered approach. Developers often end up creating too many layers besides the standard controller, service, data access, and business layers in large repos.

# This makes the business logic scatter across multiple layers making testing, refactoring, and plugging new entities difficult. Remember the stored procedures in the databases and the business logic coupled with the UI in Java Server Pages I discussed before?

# When working with JSPs and stored procedures, despite having a layered architecture, the business logic is spread across the application right from the UI to the database making the code tightly coupled.

# On the contrary, the hexagonal pattern makes its stance pretty clear: there is an inside component, which holds the business logic, then the outside layer, and the ports and the adapters, which involve the databases, message queues, APIs, and everything.
