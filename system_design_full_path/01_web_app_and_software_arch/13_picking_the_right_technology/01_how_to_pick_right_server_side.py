# How to Pick the Right Server-Side Technology?
# In this lesson, we'll learn how to pick the right server-side technology for our projects.

# Before commencing the lesson, I would like to state that there is no rule of thumb that says that for a use case X, we should always pick a technology Y.

# Everything depends on our business requirements. Every use case has its unique needs. There is no perfect tech, no silver bullet. Everything has its pros and cons. You can be as creative as you want. No rule holds us back.

# With this being said, in the lesson, I have listed some of the general scenarios, or standard use cases, in the application development domain. And then, I’ve discussed what backend technology fits best with those use cases.

# Real-time data interaction
# Imagine building an app that needs to interact with the backend server in real-time to stream data to and fro. For instance, your app could be a messaging application, a real-time browser-based massively multiplayer game, a real-time collaborative text editor, or an audio-video streaming app like Spotify, Netflix, etc.

# To implement this, we need a persistent connection between the client and server. You also need non-blocking technology on the backend. We’ve already talked about both concepts in detail.

# Some of the popular technologies that enable us to write these apps are NodeJS, Python’s Tornado framework. If you are working in the Java ecosystem, you can look into Spring Reactor, Play, and Akka.

# Once you start researching these technologies and go through the architecture concepts given in the developer docs, you’ll gain further insights into how things work and what other tech and concepts you can leverage to implement your use case. One thing leads to the other.

# Uber used Node.js to write their core trip execution engine. The technology enabled them to manage a large number of concurrent connections without much fuss.

# Peer-to-peer web application
# If you intend to build a peer-to-peer web app, for instance, a P2P distributed search engine or a P2P Live TV radio service, something similar to LiveStation by Microsoft, look into JavaScript protocols like DAT and IPFS. Also, checkout FreedomJS, which is a framework for building P2P web apps that work in modern web browsers.

# CRUD-based regular application
# Regular CRUD-based apps include simple use cases such as a tax filing app, employee management, employee attendance systems, etc.

# Today, CRUD(Create Read Update Delete) is the most common form of web app businesses build. Be it an online booking portal, an app collecting user data, or a social site. Most of them have an MVC(Model View Controller) architecture on the backend.

# Some of the popular technologies that help us implement these use cases are Spring MVC, Python Django, Ruby on Rails, PHP Laravel, and ASP .NET MVC.

# Simple, small scale applications
# If you intend to write an app that doesn’t involve much complexity like a blog, a wordpress plugin, a simple online form, or simple apps that integrate with social media platforms running within the IFrame of the website, these include web browser-based strategy airline and football manager games. You can pick PHP.

# PHP is ideally used in these kinds of scenarios. We can also consider other web frameworks, like Spring boot and Ruby on Rails, that cut down the verbosity, configuration, and development time by notches and facilitate rapid development. However, PHP hosting will cost much less compared to hosting other technologies. It is ideal for very simple use cases.

# CPU and memory intensive applications
# Do you need to run CPU-intensive, memory-intensive, heavy computational tasks on the backend, such as Big Data processing, parallel processing, and running monitoring and analytics on quite a large amount of data?

# Performance is critical in systems running tasks that are CPU and memory-intensive. Handling massive amounts of data has its costs. A system with high latency and memory consumption can take a toll on the economy of a company.

# Also, regular web frameworks and scripting languages are not meant for number crunching.

# Tech commonly used in the industry to write performant, scalable, and distributed systems are:

# C++ has features that facilitate low-level memory manipulation. This provides more control over memory to the developers when writing distributed systems
# most of the cryptocurrencies are written using this language.

# Rust is a programming language similar to C++. It is built for high performance and safe concurrency. Lately, it’s been gaining quite some popularity amongst the developer circles.

# Java, Scala, and Erlang are also good picks. Most of the large-scale enterprise systems are written in Java. Elasticsearch is an open-source real-time search and analytics engine is written in Java.

# Erlang is a functional programming language with built-in support for concurrency, fault-tolerance, and distribution. It facilitates the development of massively scalable systems. This is a good read on Erlang.

# Go is a programming language by Google to write apps for multi-core machines handling a large amount of data.

# Julia is a dynamically programmed language built for high performance, running computations, and numerical analytics.

# Well, Folks, this is pretty much it. In the next lesson, we’ll talk about a few key things to bear in mind while researching on a fitting technology stack for our project.
