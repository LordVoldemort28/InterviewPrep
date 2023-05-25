(1) FEATURE EXPECTATIONS [5 min]
        (1) Use cases
        (2) Scenarios that will not be covered
        (3) Who will use
        (4) How many will use
        (5) Usage patterns
(2) ESTIMATIONS [5 min]
        (1) Throughput (QPS for read and write queries)
        (2) Latency expected from the system (for read and write queries)
        (3) Read/Write ratio
        (4) Traffic estimates
                - Write (QPS, Volume of data)
                - Read  (QPS, Volume of data)
        (5) Storage estimates
        (6) Memory estimates
                - If we are using a cache, what is the kind of data we want to store in cache
                - How much RAM and how many machines do we need for us to achieve this ?
                - Amount of data you want to store in disk/ssd
(3) DESIGN GOALS [5 min]
        (1) Latency and Throughput requirements
        (2) Consistency vs Availability  [Weak/strong/eventual => consistency | Failover/replication => availability]
(4) HIGH LEVEL DESIGN [5-10 min]
        (1) APIs for Read/Write scenarios for crucial components
        (2) Database schema
        (3) Basic algorithm
        (4) High level design for Read/Write scenario
(5) DEEP DIVE [15-20 min]
        (1) Scaling the algorithm
        (2) Scaling individual components: 
                -> Availability, Consistency and Scale story for each component
                -> Consistency and availability patterns
        (3) Think about the following components, how they would fit in and how it would help
                a) DNS
                b) CDN [Push vs Pull]
                c) Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
                d) Reverse Proxy
                e) Application layer scaling [Microservices, Service Discovery]
                f) DB [RDBMS, NoSQL]
                        > RDBMS 
                            >> Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning
                        > NoSQL
                            >> Key-Value, Wide-Column, Graph, Document
                                Fast-lookups:
                                -------------
                                    >>> RAM  [Bounded size] => Redis, Memcached
                                    >>> AP [Unbounded size] => Cassandra, RIAK, Voldemort
                                    >>> CP [Unbounded size] => HBase, MongoDB, Couchbase, DynamoDB
                g) Caches
                        > Client caching, CDN caching, Webserver caching, Database caching, Application caching, Cache @Query level, Cache @Object level
                        > Eviction policies:
                                >> Cache aside
                                >> Write through
                                >> Write behind
                                >> Refresh ahead
                h) Asynchronism
                        > Message queues
                        > Task queues
                        > Back pressure
                i) Communication
                        > TCP
                        > UDP
                        > REST
                        > RPC
(6) JUSTIFY [5 min]
	(1) Throughput of each layer
	(2) Latency caused between each layer
	(3) Overall latency justification


Approach
------------

Entity or Model in DB
APIs entry points
How services are interacting with each other and DB


Talk about every decisions you make

## Metrics
- See the interviewer as the customer, requirements might be intentionally vague
- Write assumption you are making
- Fell free to create a diagram if that helps you clarifying your thoughts.


### Fulfilling requirements
- Non functional requirements (amount of load, load distribution, security) ways of interacting with the system(user access, scheduled processes, synchronous/asynchronous communication) and data flow. 

- Explicitly mention all the assumptions that are being made.
- Spend majority of time on the critical requirements identified and on the core functionality 
- Justify the design choices that are made.
- Design the solution for scale, would more transaction seamlessly work.

### Designing for performance
-  What are the key business and technical metrics for the system? 
-  Potential Bottlenecks or pain points
-  What are failure points exists
-  What redundancy can we build in to reduce single points of failure
-  How does someone get logs and debug the system

MOST IMPORTANT TALK ABOUT TRADEOFF WITH DIFFERENT DESIGN
Scaling is critical component of software design at amazon
Fault tolerance translate to the Customer Obsession leadership principle

If the interviewer asks you to dive deep into something you are unfamilier with, tell them and suggest some other areas you are familier with and dive into that. 