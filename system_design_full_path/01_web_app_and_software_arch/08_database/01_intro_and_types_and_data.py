# Introduction and Types of Data
# In this lesson, we get an introduction to databases and different types of data.

# What is a database?
# A database is a component in application architecture required to persist data. Data can be of many forms: structured, unstructured, semi-structured, and user state data.

# system_design_full_path/images/043.png

# Let’s have a quick insight into the classification of data before delving into the databases in detail.

# Structured data
# Structured data is the type of data that conforms to a certain structure, typically stored in a database in a normalized fashion.

# Structured data is the most easy to work with since it does not need any sort of data preparation before we can interact with it.

# An example of this type of data is the details of a customer stored in a database row. The customer Id would be of integer type, the name would be of string type with a certain character limit, age would be of integer type and so on.

# Every column of the database row has some pre-defined rules for the data that is meant to be persisted in it. With structured data, we know what we are dealing with. Since the customer name is strictly of string type, we can run string operations on it without worrying about errors or exceptions.

# Structured data is typically managed by a query language such as SQL(Structured query language).

# Unstructured data
# Unstructured data has no definite structure. It is the heterogeneous type of data consisting of text, image files, videos, multimedia files, pdfs, blob objects, word documents, machine-generated data, etc.

# We generally have to deal with this kind of data when running data analytics. In a data analytics architecture, the data streams in from multiple sources such as IoT devices, social networks, web portals, industry sensors, etc., into the analytics system.

# We cannot directly interact with unstructured data. The initial data collected is pretty raw. We have to make it flow through a data preparation stage that segregates it based on business logic and then analytics algorithms are run to extract meaningful information.

# system_design_full_path/images/044.png

# Semi-structured data
# Semi-structured data is a mix of structured and unstructured data. This data is often stored in data transport formats such as XML, JSON and handled as per the business requirements.

# User state
# User state data is the data containing the information of activity the user performs on the website.

# For instance, when browsing through an e-commerce website: the user typically browses through several product categories, sorts the products based on different parameters, clicks on recommended products, adds a few of them to the wishlist and the availability notification list, and so on.

# All this activity is the user state. Storing user state helps businesses improve the user browsing experience and the conversion rate on their website. Also, persisting the state enables the users to continue from where they left off when they log in next. It does not feel like they are starting fresh on a website.

# So, now that we are clear on the different types of data, let’s look into different kinds of databases. There are different kinds of databases fitting different use cases. We will understand them in the lessons lined up next.
