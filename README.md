# Linux System Dashboard 🚀

## Dashboard Preview

![Dashboard Screenshot](images/dashboard.png)

## About the Project

This is my first cloud deployment project.

I built this Linux System Dashboard using Flask and Python to display some basic system information such as hostname, current user, CPU usage, RAM usage, and disk usage.

Initially, the project was running only on my local machine, but later I deployed it on AWS EC2 and configured it with Gunicorn, Nginx, a custom DuckDNS domain, and HTTPS using Let's Encrypt SSL certificates.

Working on this project helped me understand how a web application is actually deployed and made accessible over the internet.

---

## Features

* Displays hostname of the Linux machine
* Shows currently logged-in user
* Displays CPU usage
* Displays RAM usage
* Displays disk usage
* Responsive dashboard interface
* Hosted on AWS EC2
* Accessible through a custom domain
* Secured with HTTPS

---

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS

### System Monitoring

* psutil

### Deployment

* AWS EC2
* Gunicorn
* Nginx
* Systemd

### Networking & Security

* DuckDNS
* Let's Encrypt SSL
* HTTPS

### Version Control

* Git
* GitHub

---

## How the Dashboard Works

The application collects system information from the Linux server and displays it on a web page.

### Hostname

The hostname identifies the machine on which the application is running.

### User

The dashboard displays the currently logged-in Linux user.

### CPU Usage

CPU utilization is collected using the psutil library.

### RAM Usage

The dashboard calculates the percentage of memory currently being used.

### Disk Usage

The dashboard displays the percentage of storage currently occupied on the server.

---

## Deployment Process

I followed the following steps to deploy this project:

1. Built the Flask application locally.
2. Uploaded the source code to GitHub.
3. Created an Ubuntu EC2 instance on AWS.
4. Connected to the server using SSH.
5. Installed Python and project dependencies.
6. Created a virtual environment.
7. Ran the application using Gunicorn.
8. Configured Nginx as a reverse proxy.
9. Created a systemd service so the application starts automatically.
10. Connected a DuckDNS domain to the EC2 instance.
11. Generated SSL certificates using Let's Encrypt.
12. Enabled HTTPS for secure access.

---

## Challenges I Faced

While deploying the project, I ran into several issues and learned a lot by fixing them.

Some of the problems included:

* SSH authentication errors
* Missing Python packages
* Gunicorn service conflicts
* Nginx configuration issues
* SSL certificate installation errors
* HTTPS port configuration in AWS Security Groups

Troubleshooting these issues helped me understand how cloud deployment works in a real environment.

---

## Live Demo

https://linux-system-dashboard.duckdns.org

---

## Future Improvements

Some features I would like to add in the future:

* Auto-refreshing metrics
* CPU and RAM usage graphs
* Historical monitoring data
* Docker-based deployment
* AWS CloudWatch integration
* User authentication

---

## What I Learned

This project helped me understand:

* Flask application deployment
* AWS EC2 basics
* Linux server management
* SSH connectivity
* Nginx reverse proxy configuration
* Gunicorn application server
* Domain and DNS configuration
* HTTPS and SSL certificates
* Git and GitHub workflow

This project was a great learning experience and gave me practical exposure to cloud deployment and web application hosting.
