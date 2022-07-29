# Graph Database
# In this lesson, we will learn about the graph database and when to choose it for our projects.

# What is a graph database?
# Graph databases are a part of the NoSQL family. They store data in nodes/vertices and edges in the form of relationships. Each node in a graph database represents an entity, it can be a person, a place, a business, etc., and the edge represents the relationship between the entities.

# system_design_full_path/images/049.png

# But, why use a graph database to store relationships when we already have SQL-based relational databases available?

# Why use a graph database?
# There are instances when complex relationships stored in a relational database across tables become slow to query. Developers have to unwillingly use joins to fetch data and joins across multiple tables slow things down.

# With the graph data model, there is less fighting the database in production since data is accessed with low latency. And there is a reason for this.

# Graph data model fits best for modelling real-world use cases where entities have complex relationships.

# Real-world use cases of graph databases
# Modeling relationships between users in social networks
# Facebook built its graph search feature using the graph data structure and the associated algorithms. The core feature of social networks today is to map the relationships between their users. And these relationships are multi-dimensional
# besides just mapping friendships, these networks also map links between users and their favourite restaurants, cuisines, sports teams, etc.

# system_design_full_path/images/050.png

# Empowered by these relationships, these networks can recommend users where to: dine, travel, be friends with, and so on.

# A graph data structure has a set of vertices or nodes and the associated edges. Vertices/nodes are typically seen as users or entities in a network, and the edges are seen as relationships, as you see in the illustration.

# There are two primary ways of representing graphs: Adjacency List and the Adjacency Matrix
# which one to pick depends on the kind of operation to be performed on the graph.

# Adjacency Matrix ideally helps figure out queries like if a relationship between two nodes exists, in constant time O(1), though it is a bit space-intensive. If the nodes in a graph contain a lot of edges, we tend to represent it with the adjacency matrix. On the flip side, if the edges are sparse, we represent the graph using the adjacency list.

# In the case of a social network, where there are, say, 2 billion users/nodes, a user/node on average would have 500 friends/edges. The edges are pretty sparse in context to the number of nodes. We would pick an adjacency list to represent this kind of graph
# using an adjacency matrix would be a waste of memory. If the relationships/edges between the nodes were in billions, we could have then chosen the adjacency matrix to represent the graph. It all depends on the use case.

# Graphs are traversed using the search algorithms depth-first search and breadth-first search, which are implemented using stack and queue data structures, respectively. Depth-first search is primarily run to find paths and connectivity between the nodes, detect cycles in a graph, and more. Breadth-first search is used to find the shortest path between two nodes.

# Though this is not a tutorial on the graph data structure, I am delving into the details just for the sake of helping you understand how graph databases are built to model real-world data having relationships.

# In graph databases, the relationships are stored differently from how relational databases store relationships.

# Graph databases are faster because the relationships in them are not calculated at query time, as it happens with the help of joins in the relational databases. Rather, the relationships here are persisted in the datastore in the form of edges, and we just have to fetch them
# no need to run any sort of computation at the query time.

# Google maps is one big graph
# Besides mapping user relationships etc., in social networks, graphs also represent cities and networks. Google Maps and cab booking apps like Uber, Ola are perfect examples of this.

# In Google Maps, nodes represent cities, and the edges are the roads between these cities. The nodes could further represent places in a city, intersections, and even houses. The entire application is one big map that heavily uses graph theory to find the shortest distance between the two places.

# system_design_full_path/images/051.png

# The same goes for flight networks where each node represents an airport and the edges flights between them.

# In graph theory, based on the use case, different algorithms are used to calculate the shortest path between two nodes. A few of the popular ones are Dijkstra’s algorithm, Bellman-Ford algorithm, A * search algorithm, Floyd–Warshall algorithm, Johnson’s algorithm, and the Viterbi algorithm.

# Mobility service providers like Uber, Ola use different routing algorithms to find an efficient route between pickup and drop locations.

# Graphs in Google’s page rank algorithm
# Google’s page rank algorithm is built on graph theory. The web pages are considered as nodes, and the links between them, the edges. Further, the nodes have weights. Weights decide the authority of a page on the web. If a web page contains detailed information on a particular topic and links to credible sources, it is given a higher weight, and the pages higher in weight are ranked first.

# These are a few examples of popular real-world products and features modeled on graphs and the associated algorithms that have genuinely changed our lives.

# When do I pick a graph database?
# Ideal use cases of graph databases are building social, knowledge, and network graphs, writing AI-based apps, recommendation engines, fraud analysis apps, storing genetic data, and so on.

# Anytime you need to store complex relationships, consider a graph database. Graph databases help us visualize our data with minimum latency. A popular graph database used in the industry is Neo4J.

# Real-life Implementations
# Here are some of the real-life implementations of the tech:

# Walmart shows product recommendations to its customers in real-time using the Neo4J graph database.
# NASA uses Neo4J to store “lessons learned” data from their previous missions to educate the scientists and engineers.
