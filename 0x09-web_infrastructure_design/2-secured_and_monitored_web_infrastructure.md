##SECURED AND MONITORED WEB INFRASTRUCTURE

**The three firewalls** were installed to add layers of security and protect against all attack. This acts as a barrier between the internet and the web infrastructure which allows only authorized traffic to pass through.

**SSL(secure socket layer)** to ensure that the data transmitted between the website and its users is protected from  interception and tampering.

**Monitoring** to detect and alert on issues within the web infrastructure. The three monitoring clients collect data from different components of the web infrastructure such as the web server and MySQL database and send it to the monitoring service for analysis and alerting.

**What are firewalls for:** They acts as barriers between the internet and the web infrastructure. They help to block malicious traffic and prevent attacks.

**Why is the traffic served over HTTPS:**  to increase security of data transfer. 

**How the monitoring tool is collecting data:** This data can be collected by setting up monitoring for the web server, collecting metrics related to its performance, and analyzing those metrics to calculate the QPS.

**Issues With This Infrastructure**

•Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.
•Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.
•Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable.
