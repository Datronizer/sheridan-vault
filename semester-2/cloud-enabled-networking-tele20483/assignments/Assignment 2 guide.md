Create 1 VM
- Empty container. Literally nothing
Create 2 Webservers (these will probably have the same public IP).
- These will have their own databases
- They will use TCP port 27017, 8081, 8082
- They will use NGINX
- They will have a docker container and a mongodb

The security groups we need to create are already provided and specified in a very detailed table in the Assignment 2 docx 

VM to VM communication should be done using private IP
PC to VM communication (of course) should be done using public IP

You will need: 
- Wireshark (fuck i uninstalled it)

Letting **all** IPv4 pass will be: `0.0.0.0/0`
Letting **all** IPv6 pass will be: `::/0`

Database should NEVER be allowed access to the internet. You should link the DB to an instance that can access the internet instead. That's more secure.