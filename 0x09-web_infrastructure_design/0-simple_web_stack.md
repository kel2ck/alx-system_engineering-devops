## SIMPLE WEB STACK

### EXPLANATION:

**Server:**  Machine without mouse, keyboard, screen that provides services to clients. Only network can be access.
**Web Server (Nginx):** delivers webpage content to browser.
**App Server:** process/compile dynamic code to HTML
**Database(mysql)** = master = read/write
		   Slave = read.

**What is a server?**

In computing, a server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called “clients”. This architecture is called the Client-server model.

**What is the role of the domain name?**

Domain names serve to identity internet resources such as computers, networks and services with a text-based label that is easier to memorize than the numerical addresses used in the internet protocols. A domain name may represent entire collections of such resources or individual instances.
What type of DNS record www is in www.foobar.com: CNAME

**What is the role of the web server?**

The primary role of a web server is to store, process, and deliver requested information or webpages to end users. It users physical storage. All website data is stored on a physical web server to ensure its safety.

**What is the role of the application server?**

The function of the application server is to act as host (or container) for the User’s business logic while facilitating access to and performance of the business application.

**What is the role of the database?**

The use of a computer database is typically involved in efficient data management. A shared, integrated computer structure. A database stores the following: End-user data that is raw data relevant to the end user. Metadata – the data about data, though which end-user data is integrated and managed.

**What is the server using to communicate with the computer of the user requesting the website?**

Web servers and HTTP (a primer) web browsers communication with web servers using the Hypertext Transfer Protocol (HTTP) when you click link on web page, submit a form, or run a search, the browser sends an HTTP Request to the server

**SPOF:**

A single point of failure (SPOF) is a potential risk posed by a flaw in the design, implementation or configuration of a circuit or system. 
SPOF refers to one fault or malfunction that can cause an entire system to stop operating.

Downtime when maintenance needed (like deploying new code web server needs to be restarted): During maintenance or update the server needs to be restarted, causing downtime and disrupting access to the website.

Cannot scale if too much incoming traffic: if the website receives too much traffic, the infrastructure will not be able to handle it, leading to crashes or a slow loading time. since this infrastructure only has a single server the scaling options are limited.
