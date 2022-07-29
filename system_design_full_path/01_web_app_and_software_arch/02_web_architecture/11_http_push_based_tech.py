# HTTP Push-Based Technologies
# In this lesson, I will discuss HTTP PUSH-based technologies.

# Web Sockets
# A Web Socket connection is preferred when we need a persistent bi-directional low latency data flow from the client to the server and back.

# Typical use-cases of web sockets are messaging, chat applications, real-time social streams, browser-based massive multiplayer games, etc. These are apps with quite a significant number of read writes compared to a regular web app.

# With web sockets, we can keep the client-server connection open as long as we want.

# Have bi-directional data? Go ahead with web sockets. One more thing, web sockets don’t work over HTTP. The mechanism runs over TCP. Also, the server and the client should both support web sockets. Else it won’t work.

# The WebSocket API and Introducing WebSockets – Bringing Sockets to the Web are good resources for further reading on web sockets.

# AJAX – Long polling
# Long polling lies somewhere between AJAX and Web Sockets. In this technique, instead of immediately returning the empty response, the server holds the response until it finds an update to be sent to the client.

# The connection in long polling stays open a bit longer compared to polling. The server doesn’t return an empty response. If the connection breaks, the client has to re-establish the connection to the server.

# The upside of using this technique is that there are fewer requests sent from the client to the server than the regular polling mechanism. This cuts down a lot of network bandwidth consumption.

# Long polling can be used in simple asynchronous data fetch use cases when you do not want to poll the server every now and then.

# HTML5 Event-Source API and Server-Sent Events
# The Server-Sent Events(SSE) implementation takes a different approach. Instead of the client polling for data, the server automatically pushes the data to the client whenever the updates are available. The incoming messages from the server are treated as events.

# Via this approach, the servers can initiate data transmission towards the client once the client has established the connection with an initial request.

# This helps eliminate a considerable number of blank request-response cycles cutting down the bandwidth consumption by notches.

# To implement the server-sent events, the backend language should support the technology. On the UI, HTML5 Event-Source API is used to receive the incoming data from the backend.

# An important thing to note here is that once the client establishes a connection with the server, the data flow is in one direction only, from the server to the client.

# SSE is ideal for scenarios like a real-time Twitter feed, displaying stock quotes on the UI, real-time notifications, etc.

# This is a good resource for further reading on SSE.

# Streaming over HTTP
# Streaming over HTTP is ideal for cases where we need to stream extensive data over HTTP by breaking it into smaller chunks. This is made possible with HTML5 and a JavaScript Stream API.

# ../../images/016.png

# Both the client and the server must agree to conform to the streaming settings to stream data. This helps them determine when the stream begins and ends over an HTTP request-response model.

# The technique is primarily used for streaming multimedia content, like large images, videos, etc., over HTTP. Empowered by this technique, we can watch a partially downloaded video as it downloads by playing the downloaded chunks on the client.

# For further reading on Stream API, this is a good resource.

# Summary
# So, now we understand what HTTP Pull and Push are. We went through different technologies that help us establish a persistent connection between the client and the server.

# Every tech has a specific use case, and AJAX is used to dynamically update the web page by polling the server at regular intervals.

# Long polling has a connection open time slightly longer than the polling mechanism.

# Web Sockets have bi-directional data flow, whereas server-sent events facilitate data flow from the server to the client.

# Streaming over HTTP facilitates the streaming of large objects like multimedia files.

# What tech would fit best for our use case depends on the application we intend to build.

# In the next lesson, let’s gain an insight into the pros and cons of the client and the server-side rendering.
