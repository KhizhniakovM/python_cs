# Client-Side vs. Server-Side Rendering
# In this lesson, you will learn about the client-side and the server-side rendering and the use cases for both approaches.

# Client-side rendering - How does a browser render a web page?
# When a browser receives a web page from the server in response, it has to render the response on the window in the form of an HTML page.

# To pull this off, the browser has several components, such as:

# The browser engine
# Rendering engine
# JavaScript interpreter
# Networking and the UI backend
# Data storage etc.
# I won’t go into much detail
# the gist is the browser has to do a lot of work to convert the response from the server into an HTML page. The rendering engine constructs the DOM tree and renders and paints the construction and so on.

# Naturally, all this activity takes some time before the user can interact with the page.

# Server-side rendering
# To cut down all this rendering time on the client, developers often render the UI on the server, generate HTML there and directly send the HTML page to the UI.

# This technique is known as server-side rendering. It ensures faster rendering of the UI, averting the UI loading time in the browser window because the page is already created and the browser doesn’t have to do much assembling and rendering work.

# Here are some use cases for both approaches of rendering the UI—on the client and the server.

# Use cases for server-side & client-side rendering
# The server-side rendering approach is perfect for delivering static content, such as WordPress blogs. It’s also good for SEO because the crawlers can easily read the generated content.

# However, modern websites are highly dependent on AJAX. On such websites, content for a particular module or a page section has to be fetched and rendered on the fly. In this use case, the server-side rendering doesn’t help much.

# If we render the UI on the server for AJAX-based websites, for every AJAX request, the approach will generate the entire page on the server as opposed to just sending the updated content to the client in response.

# This process will prove to be resource-intensive and would consume unnecessary bandwidth, failing to provide a smooth user experience.

# Also, once the number of concurrent users on the website goes up, server-side rendering will exert an unnecessary load on the server.

# So, for modern dynamic AJAX-based websites, the client-side rendering works best.

# Moreover, we can leverage a hybrid approach to get the best of both worlds. We can use server-side rendering for the static content of our website and client-side rendering for dynamic content.

# Okay, before we move on to the database, message queue and caching components, it’s essential for us to understand concepts such as:

# - Scalability
# - High availability
# - Load balancing
# - Monolith and microservices

# Understanding these concepts will help us understand the rest of the web components better.

# Let’s have a look at them one by one.
