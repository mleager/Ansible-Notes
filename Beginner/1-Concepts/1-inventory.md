
#  Ansible Inventory [] {} =


Ansible stores information about its target systems in the file "inventory.txt"

If you don't create a new inventory file, it uses the default inventory at: /etc/ansible/hosts 


Sample inventory file: <br>
---------------------- <br>
server1.company.com    <br>
server2.company.com    <br>

[group2] <br>
server3.company.com    <br>
server4.company.com    <br>

[web] <br>
server5.company.com    <br>
server6.company.com    <br>



Assigning an alias to servers:
-------------------------------------
**web**  ansible_host=server1.company.com    <br>
**db**   ansible_host=server2.company.com    <br>
**web2** ansible_host=server3.company.com    <br>



Other inventory parameters:

    - ansible_connection  -->  ssh/winrm/localhost
    - ansible_port        -->  22/5986
    - ansible_user        -->  root/administrator
    - ansible_ssh_pass    -->  Password


Example inventory file with parameters:
---------------------------------------
web ansible_host=server1.company.com ansible_connection=ssh ansible_user=root



##  Sample Inventory Files
<br>
----------  Basic  ----------  

### Web Servers
**web1** ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123! <br>
**web2** ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123! <br>
**web3** ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123! <br>

### Database Servers
**db1** ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!

**[web_servers]**  <br>
web1           <br>
web2           <br>
web3           <br>

**[db_servers]**  <br>
db1           <br>

**[all_servers:children]** <br>
web_servers            <br>
db_servers             <br>


----------  More Advanced  ----------

### Web Servers
**web_node1** ansible_host=web01.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass    <br>
**web_node2** ansible_host=web02.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass    <br>
**web_node3** ansible_host=web03.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass    <br>

### DB Servers
**sql_db1** ansible_host=sql01.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass    <br>
**sql_db2** ansible_host=sql02.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass    <br>

**[db_nodes]** <br>
sql_db1    <br>
sql_db2    <br>

**[web_nodes]** <br>
web_node1    <br>
web_node2    <br>
web_node3    <br>

**[boston_nodes]** <br>
sql_db1        <br>
web_node1      <br>

**[dallas_nodes]** <br>
sql_db2        <br>
web_node2      <br>
web_node3      <br>

**[us_nodes:children]** <br>
boston_nodes        <br>
dallas_nodes        <br>
