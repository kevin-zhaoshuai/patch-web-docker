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

2016.03.06
Begin port it to fleet and CoreOS

TODO: 
Using Kubernetes to deploy
Add loading balance
