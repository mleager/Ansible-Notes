
##  Ansible Inventory  ##     [] {} =



Ansible stores information about its target systems 
in the file "inventory.txt"

    - if you don't create a new inventory file, it uses
      the default inventory at: /etc/ansible/hosts 



Sample inventory file:
----------------------
server1.company.com
server2.company.com

[group2]
server3.company.com
server4.company.com

[web]
server5.company.com
server6.company.com
----------------------


Assigning an alias to servers:
-------------------------------------
web  ansible_host=server1.company.com
db   ansible_host=server2.company.com
web2 ansible_host=server3.company.com
-------------------------------------


Other inventory parameters:

    - ansible_connection  -->  ssh/winrm/localhost
    - ansible_port        -->  22/5986
    - ansible_user        -->  root/administrator
    - ansible_ssh_pass    -->  Password


Example inventory file with parameters:
---------------------------------------
web ansible_host=server1.company.com ansible_connection=ssh ansible_user=root



##  Sample Inventory Files  ##

----------  Basic  ----------  

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

# Database Servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!

[web_servers]
web1
web2
web3

[db_servers]
db1

[all_servers:children]
web_servers
db_servers


----------  More Advanced  ----------

# Web Servers
web_node1 ansible_host=web01.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
web_node2 ansible_host=web02.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
web_node3 ansible_host=web03.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass

# DB Servers
sql_db1 ansible_host=sql01.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass
sql_db2 ansible_host=sql02.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass

[db_nodes]
sql_db1
sql_db2

[web_nodes]
web_node1
web_node2
web_node3

[boston_nodes]
sql_db1
web_node1

[dallas_nodes]
sql_db2
web_node2
web_node3

[us_nodes:children]
boston_nodes
dallas_nodes