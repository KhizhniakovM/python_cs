# Reducing the Application Deployment Costs via Caching
# In this lesson, we will discuss a real-world example of how effective caching can help us reduce the deployment cost of our application.

# Real-world use cases
# Stock market-based multiplayer game
# In this lesson, I will share an insight from a stock market-based multiplayer game that I developed and deployed on the cloud.

# The game had stocks of numerous companies listed on the stock market and the algorithm would trigger the stocks’ price movement based on certain parameters every second, if not before.

# Initially, I persisted the updated stock price in the database as soon as the prices changed to create a stock price movement timeline at the end of the day. However, the number of database writes for the stocks price movement for the whole day was very high, having the potential to create a crater in my pocket.

# Eventually, I decided not to persist the updated price every second in the database and rather use a cache(Memcache) to persist the updated stock prices. I then scheduled a batch operation that would run throughout the day every few hours to update the database with the stock prices.

# In the cloud, writing to Memcache was cheaper than writing to the database by quite an extent. The cache served all the stock price read-write requests, and the database got the updated values when the batch operation ran.

# This tweak may not be ideal for a real-life Fintech app. However, it helped me save a truckload of money and allowed me to run the game for a more extended period of time.

# So, this is one instance where you can leverage the caching mechanism to cut down costs. There are use cases where you might not want to persist every little information in the database and instead use the cache to store that not-so-mission-critical information.

# Polyhaven - a 3D asset library
# This is a very rudimentary example of how an application with static data can leverage caching to significantly cut down its deployment costs.

# I recommend reading this blog article that I wrote on how Polyhaven, a 3D asset library, managed 5 million page views and 80TB traffic a month for less than 400 USD by leveraging caching. If it weren’t for it, the storage cost for all that data on a cloud object-based storage would cost them approx. 4K USD a month.

# system_design_full_path/images/054.png

# In the next lesson, let’s look into some of the caching strategies we can leverage to enhance the app’s performance further.
