# 2b2t-Q-Position-Server (Windows Only)
See your 2b2t Queue Position from an Apache web server

## Installation
Step 1: Download Apache Lounge and install it following this link https://www.znetlive.com/blog/how-to-install-apache-php-and-mysql-on-windows-10-machine/
*Note: Only install Apache, don't install PHP and MYSQL

Step 2: Download q.py from repository

Step 3: Open q.py in a text editor and replace !here! with the path to your .minecraft folder

## Running
To start: Run q.py in the cmd prompt using python
*Note: A new window should also appear for the Apache Server

To stop: Ctrl^C out of both programs

## Ways to connnect/brodcast the server
LAN only: This program will always brodcast the server to the LAN, access the server by typing your computer's ip address into your browser

Port Forwarding: You can optionally use port forwarding to brodcast your server onto the web, read more at https://www.howtogeek.com/66214/how-to-forward-ports-on-your-router/
*Note: Apache runs on port 80 by default
