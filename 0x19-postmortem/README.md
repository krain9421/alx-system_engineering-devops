**Issue Summary**
From 09:00 to 09:30 GMT, connection requests to our Apache server returned an error message. This particular Apache server hosts one of our legacy applications. Throughout the duration of this issue, all users of this service were affected. The root cause of this issue was a configuration script which caused the Apache server to stop running.

**Timeline (GMT)**
•	09:00: Configuration script run on server
•	09:00: Server outage start time
•	09:05: Multiple user complaints received by mail
•	09:10: Complaints escalated to Network Operations Center
•	09:15: Preliminary checks run on server
•	09:20: Apache service restarted
•	09:25: Apache server back online
•	09:30: Network Engineers report issue as resolved

**Root Cause**
At 08:55 GMT, a configuration script was run on an Apache server that hosts one of our legacy applications. The script, being that it was run during working hours and outside maintenance windows, was meant to make a textual change to the index page on the server without stopping the apache2 service. However, this particular script contained the following line at the end, ‘service apache2 stop’. That command caused the apache2 service to stop running and subsequently the server to go offline at 09:00 GMT.

**Resolution**
After receiving an escalation query at 09:10 GMT, the network operating division, in charge of monitoring the server of the legacy application, swiftly responded to resolve the issue. 
At 09:15 GMT, the engineers ran the necessary preliminary checks to determine the health of the server. Then they ran ‘curl’ commands on ports 80 of the server and received the error message: ‘(7) Failed to connect to 0 port 80: Connection refused’. 
Thus, they were able to deduce that the apache2 service on the server wasn’t running and at 09:20, they executed the command to restart the apache2 service and get the server back online.

**Corrective and Preventive Measures**
I would suggest that configuration scripts should be thoroughly read through and run in test environments before being run in production environments. There should also be service listeners installed on the servers that will alert the network team if any crucial service becomes inactive. Listed below are some tasks that address the issue.
•	Run all future scripts in test environments before production.
•	Ensure that all results in test environments meet all requirements before pushing scripts to production environment.
•	Develop and deploy monitoring systems on all servers to detect inactive services.
•	Ensure that the network team is quickly alerted if an inactive service is unable to be restarted automatically.
