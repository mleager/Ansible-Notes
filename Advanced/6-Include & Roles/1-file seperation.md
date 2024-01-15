
##  Ansible File Seperation  ##     [] {} =



When multiple variables are defined in the inventory file,
it is better to organize the code using a specific folder architecture.


##  ----  Host_Vars Folder  ----  ##

    Put the Host variables in their own folder & files

1. Create the folder 'host_vars' 

2. create a .yml file for each Host in the inventory

3. the .yml file's need to be named exactly the same as the Host


old inventory
-------------
[web_servers]
web1 ansible_host=172.20.1.100 dns_server=10.1.1.5 size=big
web2 ansible_host=172.20.1.101 dns_server=10.1.1.5 size=small
web3 ansible_host=172.20.1.102 dns_server=10.1.1.5 size=small


- playbook.yml
- inventory
- host_vars
  --> web1.yml
  --> web2.yml
  --> web3.yml

host_vars/web1.yml
------------------
ansible_host: 172.20.1.100
dns_server: 10.1.1.5
size: big

host_vars/web2.yml
------------------
ansible_host: 172.20.1.101
dns_server: 10.1.1.5
size: small

host_vars/web3.yml
------------------
ansible_host: 172.20.1.103
dns_server: 10.1.1.5
size: small


new inventory
-------------
[web_servers]
web1
web2
web3


##  ----  Group_Vars Folder  ----  ##

    Put the Group variables in their own folder & files

1. Create the folder 'group_vars'

2. create a .yml file for each Group in the inventory

3. the .yml files need to be named exactly the same as the Group


    * Put the 'dns_server' variable into 'group_vars'
      because every Host uses the same one 


- playbook.yml
- inventory
- host_vars
  --> web1.yml
  --> web2.yml
  --> web3.yml
- group_vars
  --> web_servers.yml


group_vars/web_servers.yml
--------------------------
dns_server: 10.1.1.5


    * Now you can remove the 'dns_server' variable from the Hosts


host_vars/web1.yml
------------------
ansible_host: 172.20.1.100
size: big

host_vars/web2.yml
------------------
ansible_host: 172.20.1.101
size: small

host_vars/web3.yml
------------------
ansible_host: 172.20.1.103
size: small


##  ----  Final Folder Structure  ----  ##

    Create an 'inventory' folder that houses:

        - inventory file
        - host_vars folder
        - group_vars folder


- playbook.yml
- inventory/
  |--> inventory
  |--> host_vars
  |    |--> web1.yml
  |    |--> web2.yml
  |    |--> web3.yml
  |--> group_vars
       |--> web_servers.yml


Ex: Run the playbook.yml using this structure

    >> ansible-playbook -i inventory/inventory playbook.yml -v


# View the Inventory File to Ensure Variables are Working


    This helps you test your variables, 
    and view what values are assigned to them


# View Inventory Folder in YML format:

    >> ansible-inventory -i inventory/ -y


    * This shows the entire inventory folder and its 
      defined variables 

    
    * You can also specify a single inventory file,
      or view output in JSON ( don't use '-y' flag )