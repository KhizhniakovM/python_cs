# HTTP Pull - Polling With AJAX
# In this lesson, we will cover HTTP PULL, AJAX and how polling is done using AJAX.

# There are two ways of pulling/fetching data from the server.

# The first is sending an HTTP GET request to the server manually by triggering an event on the user interface by clicking a button or interacting with any other element on the web page.

# The other is pulling data dynamically at regular intervals using AJAX without any human intervention.

# AJAX – Asynchronous JavaScript and XML
# AJAX stands for Asynchronous JavaScript and XML. The name says it all. AJAX is used for adding asynchronous behavior to the web page.

# ../../images/014.png

# As you can see in the illustration above, instead of requesting the data manually every time with the click of a button, AJAX enables us to fetch the updated data from the server by automatically sending the requests over and over at stipulated intervals.

# Upon receiving the updates, a particular section of the web page is updated dynamically by the callback method. We see this behavior all the time on news and sports websites, where the updated event information is dynamically displayed on the page without needing to reload it.

# AJAX uses an XMLHttpRequest object to send the requests to the server. This object is built in the browser and uses JavaScript to update the HTML DOM(Document Object Model).

# AJAX is commonly used with the jQuery framework to implement the asynchronous behavior on the UI.

# This dynamic technique of requesting information from the server at regular intervals is known as polling.

# It is important to note here that AJAX polling and AJAX Long polling are different techniques. Do not confuse them as one.

# AJAX polling is the HTTP Pull mechanism and AJAX Long polling is a hybrid between the HTTP Push and the Pull, based on the BAYEUX protocol. I’ve discussed it in the HTTP Push-based technologies lesson.
