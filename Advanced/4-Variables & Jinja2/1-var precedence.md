
##  Ansible Variable Precedence  ##     [] {} =


Docs for Variable Precedence:

    https://docs.ansible.com/ansible/2.5/user_guide/playbooks_variables.html


# Main Variable Precedence in Ansible

1. Command Line variables   ( --extra-vars )
2. Playbook variables
3. Host variables           ( Inventory )
4. Group Variables          ( Inventory )


# Variable Precedence in Inventory File

/etc/ansible/hosts
------------------
web1 ansible_host=172.20.1.100
web2 ansible_host=172.20.1.101 dns_server=10.5.5.4

[web_servers]
web1
web2

[web_servers:vars]
dns_server=10.5.5.3
------------------

    Inventory Precedence ( Highest to Lowest ):

        1. host variable  ( dns_server=10.5.5.4 )
        2. group variable ( dns_server=10.5.5.3 )


# Variable Precedence in Playbook

playbook.yml
------------
- name: Configure DNS Server
  hosts: all
  vars:
    dns_server: 10.5.5.5
  tasks:
    - nsupdate:
        server: "{{ dns_server }}"
------------

>> ansible-playbook -i inventory playbook.yml \
    --extra-vars "dns_server=10.5.5.6"

    Playbook Precedence ( Highest to Lowest ):

        1. Command Line variable
        2. Playbook Variable
