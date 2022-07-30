# Go for Microservices?
# In this lesson, we'll see how Go fits for usage in the implementation of Microservices according to the criteria specified in the Requirements lesson.
# Let's Begin!

# The criteria from the second lesson of this chapter for the implementation of microservices can serve as a basis to assess Go’s suitability as a microservices programming language.

# Communication
# Go supports REST in the standard libraries. Libraries are also available for messaging systems such as AMQP, for example https: // github.com/streadway/amqp.

# There is also a library for messaging with Redis.

# Due to the widespread use of Go, there is hardly any communication infrastructure that does not support Go.

# Operation
# Go also offers many options for operation.

# Deployment
# The deployment in a Docker container is very easy with Docker multi stage builds, as already illustrated.
# Configuration
# Libraries like Viper support the configuration of Go applications. This library supports formats such as YAML or JSON.
# Logs
# Go itself already offers support for logs. The Go microservices framework Go Kit contains additional features for logs in more complex scenarios.
# Metrics
# For metrics, Go Kit supports a plethora of tools such as Prometheus, but also Graphite or InfluxDB.
# New microservices
# For a new microservice, it is enough to create the Docker build and then write the source code.

# Resilience
# Go Kit contains an implementation of resilience patterns such as Circuit Breaker. In addition, there is a port of the Hystrix library for Go.

# Microservices have to communicate with other microservices. This requires a UI integration in the web UI or protocols such as REST or messaging.
