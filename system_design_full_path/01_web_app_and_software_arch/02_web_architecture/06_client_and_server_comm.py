# Communication Between the Client and the Server
# In this lesson, we will discuss how communication between the client and the server occurs.

# Request-response model
# The client and the server have a request-response model. The client sends the request and the server responds with the data.

# If there is no request, there is no response.

# HTTP protocol
# The entire communication happens over the HTTP protocol. It is the protocol for data exchange over the World Wide Web. HTTP protocol is a request-response protocol that defines how information is transmitted across the web.

# It’s a stateless protocol, and every process over HTTP is executed independently and has no knowledge of previous processes.

# If you want to read more about the protocol, this Mozilla article is a good resource on it.

# Moving on.

# REST API and API Endpoints
# Speaking from the context of modern n-tier web applications, every client has to hit a REST endpoint to fetch the data from the backend.

# Note: If you aren’t aware of the REST API and the API Endpoints, we will discuss it in the next lesson in detail. I’ve brought up the terms in this lesson just to give you a heads up on how modern distributed web applications communicate.

# The backend application code has a REST-API implemented. This acts as an interface to the outside world requests. Every request, be it from the client written by the business or the third-party developers, those who consume our API data have to hit the REST endpoints to fetch the data.

# ../../images/011.png

# Real world example of using a REST API
# Let’s say we want to write an application to keep track of the birthdays of all our Facebook friends. The app would then send us a reminder a couple of days before the birthday of a certain friend.

# To implement this, the first step would be to get the data of the birthdays of all our Facebook friends. We would write a client to hit the Facebook Social Graph API, which is a REST-API, to get the data and then run our business logic on the data.

# Implementing a REST-based API has several upsides. Let’s delve into it in detail in the next lesson to have a deeper understanding.
