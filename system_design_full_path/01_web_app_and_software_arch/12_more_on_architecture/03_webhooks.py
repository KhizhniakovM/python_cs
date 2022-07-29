# Webhooks
# In this lesson, we’ll learn about the need for webhooks and how they work.

# What are Webhooks?
# Imagine we’ve written an API that provides information on the latest, most exclusive Baseball events. Now our API is consumed by a lot of third-party services that fetch the information from the API, add their own flavor to it, and present it to their users.

# However, so many API requests every now and then, just to check if a particular event has occurred, is crushing our server. The server can hardly keep up with the requests. There is no way for consumers to know that the new information isn’t available on the server yet or that an event hasn’t occurred yet. They just keep polling the API.

# This will pile up the unwanted load on the server and can eventually bring it down.

# What do we do? Is there a way we can cut down the load on our servers?

# Yes!! Webhooks.

# Webhooks are more like call-backs. It’s like, “I will call you when new information is available. You carry on with your work.”

# Webhooks enable communication between two services without the middleware. They have an event-based mechanism.

# Okay! So, how do they work?

# How do webhooks work?
# To use the Webhooks, consumers register an HTTP endpoint with the service with a unique API Key. It’s like a phone number. Call me on this number when an event occurs. I won’t be calling you anymore.

# Whenever new information is available on the backend, the server fires an HTTP event to all the registered endpoints of the consumers, notifying them of the latest update.

# system_design_full_path/images/068.png

# Browser notifications are one example of Webhooks. Instead of visiting the websites every now and then for new info, they notify us when they publish new content.
