# hw4_dillon_rollins CDT Echo 2025

My tool is a simple c2 system directed towards windows systems that contains 2 files:

1. A server python file that can be run on either windows or linux - I ran the server on ubuntu
2. A .ps1 script that connects to the server and creates a client ID, once its run on the target windows machine it can be run in the background and attemtps to mimic a legit web service.

The client .ps1 script needs to be configured before its dropped on the target to the server's IP and given a client ID before executing, before execution you have to set execution policy to be bypassed in powershell before it can successfuly be ran.
