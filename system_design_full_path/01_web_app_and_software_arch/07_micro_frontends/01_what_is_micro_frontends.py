# Introduction to Micro Frontends
# In this lesson, we will understand micro frontends.

# What are micro frontends?
# Micro frontends are distinct loosely coupled components of an application’s user interface developed applying the concept of microservices to the frontend.

# Writing micro frontends is more of an architectural design decision and a development approach as opposed to it being a technology.

# What does applying the concept of microservices to the front end mean?

# Microservices provide complete autonomy to the teams developing them. They are loosely coupled, provide fault isolation, and offer the freedom to pick the desired technology stack to the dedicated teams, to develop a certain service. Micro frontends offer the same upsides to frontend development.

# Typically, in application architecture, despite having microservices on the backend, our frontend is a monolith that is developed by a dedicated frontend development team.

# system_design_full_path/images/037.png

# With the micro frontends approach, we split our application into vertical slices, where a single slice goes end to end right from the user interface to the database. And every slice is owned by a dedicated team.

# Besides having the backend devs, the micro frontend team of a particular vertical slice also includes the frontend developers who develop the user interface component only for that specific service.

# Every team builds their user interface component choosing their desired technology, and later all these components are integrated, forming the complete user interface of the application. This micro frontend approach averts the need for a dedicated centralized user interface team. Every micro frontend team becomes more of a full-stack team.

# system_design_full_path/images/038.png

# Let’s break this down further with the help of an example.

# Micro frontends e-commerce application example
# I’ve picked the example of an e-commerce application because the micro frontends approach is pretty popular with e-commerce websites.

# Imagine an online game store that delivers video games for desktops and consoles such as Xbox, Nintendo Switch, PlayStation, and the related hardware.

# Our online gaming store will have several different UI components. A few of the key components would be:

# The search component – This is a search bar at the top center of the website that enables the users to search games based on the keywords they enter.

# Once the user runs a search, the component enables the user to filter their search results based on several options, including the price range, type of console, game genre, and so on.

# The game category component – This component displays the popular and widely searched games for different categories on the website’s homepage.

# Add to cart and checkout component – This user interface component enables users to add games of their liking to their cart and proceed to the checkout filling in their address and other required information to make the final payment.

# During the checkout, the website may also recommend related games to the user as upsells. The user can also feed in coupons and gift cards if they have any.

# The payment component – The payment UI component offers different payment options to the user and facilitates the order payment once the user enters their card details on the page.

# Every UI component has a dedicated microservice running on the backend powering that particular user interface component. All these different components are developed and managed by dedicated full-stack(micro frontend) teams.

# The application’s complete user interface is rendered combining all these different UI components, also called micro frontends.

# Let’s continue this discussion in the next lesson.
