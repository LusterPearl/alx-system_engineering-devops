**Learning from the Journey: A Tale of Triumphs and Challenges**

In the fast-paced world of web development, every engineer encounters hurdles that test their skills and determination.
Join me on a journey through the highs and lows of my recent projects, where I faced server outages, configuration mishaps,
and even a few lessons in humility.

Duration: Various durations, ranging from a few hours to weeks.
Impact: Multiple services affected, including SSH access, SSL certificate setup, load balancer configuration, and MySQL database.
Root Causes: Lack of experience, configuration errors, forgetting crucial steps, and encountering unfamiliar technologies.

Let's delve into the heart of these challenges and uncover the insights gained along the way:

Timeline:
Detection: Issues were detected through manual observation and system alerts.
Actions Taken: Investigated affected systems, attempted direct fixes, and escalated unresolved issues to team members.
Misleading Paths: Initial assumptions and actions sometimes led to dead ends or incorrect solutions.
Escalation: Some incidents required escalation to more experienced team members.
Resolution: Issues were resolved through various means, including server rebuilds, configuration file corrections,
and assistance from team members.
Root Cause and Resolution:
Web Server Setup: Lack of understanding led to issues such as being locked out and misconfigurations.
Resolved by rebuilding servers and correcting configurations.
SSL Certificate: Inexperience and oversight led to the delay in obtaining the SSL certificate.
Resolved through continued learning and seeking assistance.
Load Balancer Configuration: Incorrect configuration due to duplicate server entries. Resolved by identifying and correcting the configuration error using sed.
MySQL Database: Corruption and errors due to inexperience. Resolved with the help of a team member's JSON dump.
Corrective and Preventative Measures:
Continued learning and practice in server setup and maintenance.
Improved documentation and checklist creation for server configurations.
Regular audits and reviews of configurations to prevent similar issue.
Improved Monitoring: Implement comprehensive monitoring solutions to detect and alert for issues such as server downtime,
high resource usage, and configuration errors. This includes monitoring of server memory, disk space, CPU usage, and network traffic.
Automated Configuration Management: Utilize configuration management tools (e.g., Ansible, Chef, Puppet)
to automate server configuration and ensure consistency across environments. This will help prevent configuration errors and streamline future deployments.
Regular Backup and Restore Testing: Establish and maintain a regular schedule for backing up critical data,
including databases and configuration files. Test the backup and restore processes periodically to ensure they are reliable and effective.
Documentation and Knowledge Sharing: Improve documentation for server setup, configuration, and troubleshooting procedures.
Encourage knowledge sharing within the team to improve overall expertise and reduce reliance on individual members.
Continuous Learning: Invest time in continuous learning and skill development,
particularly in areas where you have encountered challenges, such as MySQL database management and Nginx server configuration.
Implementing a Test Environment: Set up a dedicated test environment to replicate production issues and test
solutions before implementing them in the live environment. This can help prevent downtime and unexpected behavior in production.
Tasks to Address the Issues:
Add Monitoring for Server Memory: Implement monitoring for server memory usage to detect and prevent memory-related issues.
Resolve Port 80 Issue: Investigate and resolve the ongoing Nginx port 80 issue to ensure proper web server functionality.
