# Mobile Backend as a Service
# In this lesson, we will learn about mobile backend as a service and when to use it.

# What is mobile backend as a service?
# Mobile Backend as a Service or MBaaS is a cloud-based service model that takes care of the backend infrastructure of our mobile app, enabling us to focus on the business logic and the user interface.

# So, what are the things an MBaaS takes care of? What features does it bring along?

# Besides the business logic and the user interface, an online service contains several other key features that collectively make the service functional and worthy of getting the user’s attention. These features are user authentication, integration with social networks, push-notifications, real-time database, caching, data storage, messaging, chat integration, integration of third-party tools, analytics, crash reporting etc., etc.

# system_design_full_path/images/083.png

# An MBaaS takes care of all these features making a developer’s life a lot easier during the bootstrapping phase. Imagine writing and maintaining all these features yourself from the bare bones. I mean, it’s not even possible unless you have a team.

# With these freemium cloud-based services, you don’t have to worry much about the app hosting costs during the initial days because these services offer a generous free tier. So, if you are a solo developer bootstrapping with minimal resources, with these services, you can always bring your app idea to reality and show it to the world.

# Deploy your app to the cloud, show it to the community, have some initial customers, get feedback, and pitch it to the potential investors without paying a dime for hosting and infrastructure. Well, what more can I say?

# This is the whole reason the cloud service model blew up, specifically the PaaS Platform as a Service. It provided a way for solo, indie developers to bootstrap their business and get a foothold in the market by focusing on the idea implementation part and letting the cloud service take care of the rest.

# An MBaaS typically offers an API for every feature. There will be an API for user authentication, an API for real-time databases, an API for messaging and so on. Our code can directly interact with the respective API and perform read writes.

# Also, since we do not have to manage the infrastructure, a mobile backend as a service cuts down the time it takes to develop an app by notches. A few popular examples of MBaaS are Google Firebase, AWS Amplify, and Parse.

# Parse was the early leader in this space but was bought and shut down by Facebook.

# When should you use a mobile backend as a service?
# MBaaS is great for mobile-only services and use cases where you do not need or don’t already have a custom backend up and running for your service.

# In the case of MBaaS, all the business logic resides on the client, which is the mobile app. So, the app is a Fat/thick client.

# MBaaS is best for apps like mobile games, messaging apps, and to-do list kinds of apps. When using MBaaS, there are a few things that you should keep in mind. Since we don’t have much control over the backend, we always have to keep the business logic on the client. This is one and another is . If we ever need to add a new feature that would require the business logic to be on the server, we will have to design a custom backend from the bare bones.

# On the flip side, we can start with a custom backend and then write a mobile client, which is the conventional way. With a custom backend, we can always customize the design of our service, introduce new clients, and so on by introducing dedicated APIs for respective clients.

# system_design_full_path/images/084.png

# We can also use MBaaS and a custom backend setup in the same app in scenarios where we are required to integrate a legacy enterprise system with our mobile app or if we need to leverage some additional features that the custom backend server hosts.

# Think of a banking app built using an MBaaS that needs to interact with the legacy enterprise backend to cross verify the data entered by the user every time.

# system_design_full_path/images/085.png

# There is one more thing, not having much control over the backend makes this a vendor lock-in situation. Just like parse.com, what if the service provider decides to close their shop? Or, they stop upgrading their service, resulting in severe security flaws? Or they stop adding new features to their service, or you in the future disapprove of their updated billing rules? What are you going to do next? Think about it.
