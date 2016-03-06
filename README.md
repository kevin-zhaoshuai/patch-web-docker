Patch Statistic Website

Three container : MySQL ,Django and Git code.

Statistic projected:
Kernel 
libvirt 
openstack/nova

Use docker-compose to integrate the container,the port of the 
whole project is 8099, the mysql port is 3306
**: Git code container need to connect the mysql db container
using --link when "docker run" or modify the docker-compose ymal

TODO: 
add apache2 to Django container
add get docker ip address scripter for git_work.py
Using fleet to orchestrate the container
Add loading balance
