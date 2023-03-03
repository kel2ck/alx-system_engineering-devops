##SCALE:

**Server:** Machine without mouse, keyboard, screen that provides service to clients. Only network can access.

•	Active-Active: All servers running
•	Active-passive: Some servers active while the passive servers are back up if failure.

**Web Server (Nginx or Apache):**  Delivers webpage contents to browser

**App server:** Process/compile dynamic code to HTML
**Database (MYSQL):**  

Master = read/write which is the primary
		           Slave = read which is replica.
Load balancer: HAproxy algorithm to balance 

**Secure Socket Layer (SSL):**

•	Public/private key match
•	Create SSL certificate that ensures connection is safe (HTTPS)
•	Without SSL, private data is sent unencrypted. 

**Firewall:** Block unauthorized access to/from network

**Monitoring Tool:**(Sumologic Datadog)
•	Monitors health of hardware and software.
•	Query per second gives information
