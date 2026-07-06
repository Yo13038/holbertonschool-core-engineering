Introduction
Traditional HTTP communication follows a request–response model, where the client initiates every interaction and the server responds. This model is not suitable for applications that require continuous updates, such as chat systems, live dashboards, or collaborative tools.

WebSockets address this limitation by establishing a persistent connection. Once the connection is open, both the client and the server can send messages at any time without reopening the connection.

In this project, you will work with WebSockets, a communication protocol that enables real-time, bidirectional data exchange between a client and a server.

Context
You will progressively implement:

A WebSocket server
Clients that communicate with the server
Message exchange between multiple participants
Basic message routing and validation
Integration with a web-based client
Each step builds on previous behavior.

Learning Objectives
By the end of this project, you should be able to:

Implement a WebSocket server using asynchronous programming
Handle multiple concurrent client connections
Send and receive messages in real time
Implement different message exchange patterns
Enforce a defined message format when required
Resources
Intro Videos (must watch before starting):

Be a Better Dev - API REST (HTTP) vs. Websockets (7 mins)
FreeCodeCamp - A Beginner's Guide to WebSockets (30 mins)
Documentation:

websockets documentation
Python asyncio documentation
MDN WebSockets API
General Requirements
Environment used for correction:

Ubuntu 20.04
Python 3.x
You must use:

the websockets library
asynchronous programming (async / await)
Your implementation must:

behave exactly as specified
handle continuous communication correctly
support multiple concurrent connections when required
Unless explicitly stated, do not:

introduce additional frameworks
modify the communication protocol
add features beyond the requirements
Important Notes
Communication is persistent: connections remain open and must be handled accordingly
Multiple clients may interact at the same time
Message formats must be respected exactly when specified
Final Remarks
This project focuses on building a working real-time communication system.

Accuracy in behavior is essential. Small deviations from the expected behavior may result in failure during evaluation.