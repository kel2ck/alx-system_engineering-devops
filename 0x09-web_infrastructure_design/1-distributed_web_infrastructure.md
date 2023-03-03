## DISTRIBUTED WEB INFRASTRUCTURE

**What distribution algorithm your load balancer is configured with and how it works?**

 A load balancer distributes incoming traffic to multiple servers to ensure that no single server becomes overloaded. Load balancer are used to improve the performance, availability and scalability of the web infrastructure.

**Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both**

The load balancer is configured to enable an active-passive setup, in which only one server is active at any given time, while the other server is in standby mode. The active server handles all incoming requests, while the passive server is ready to take over whenever the active server fails.

**Difference between active-active and active-passive load balancer:**
In an active-active configuration, the load balancer spread out the workload’s traffic among multiple nodes whereas, in active-passive configuration, the server load balancer recognizes a failed node and redirects traffic to the next available node.
**How a database Primary-Replica(master-slave) cluster works:**

A master-slave database cluster is a setup in which one database node acts as the primary or master node, while one or more database nodes acts as replica or slave nodes. The master node is responsible for accepting read and write requests from the primary node and serve read-only requests from the application.

**The difference between the Primary node and the Replica node in regard to the application:**
Read-Write Access: The primary node handles both read and write requests from the application, I it accept write requests and update the database while replica nodes are typically only used for read-only requests. The replica nodes replicate the data from the primary node and can serve read requests, but they cannot accept write requests.

**Issues With This Infrastructure**

- There are multiple SPOF (Single Point Of Failure). For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

- Security issues. The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. 
  There is no way of blocking unauthorized IPs since there's no firewall installed on any server.

- No monitoring. We have no way of knowing the status of each server since they're not being monitored.
