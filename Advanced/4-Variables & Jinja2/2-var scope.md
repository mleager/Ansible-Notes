
##  Ansible Variable Scope  ##     [] {} =



# Variable Scope Types

    1. Host
    2. Play
    3. Global 


# Host Variable Scope

/etc/ansible/hosts
------------------
web1 ansible_host=172.20.1.100
web2 ansible_host=172.20.1.101 dns_server=10.5.5.4
web3 ansible_host=172.20.1.102


    A Host variable is accessible for a Play that is run on that Host

        - host variable my be defined as host or group


# Play Variable Scope

---
- name: Play1
  hosts: web1
  vars:
    ntp_server: 10.1.1.1
  tasks:
    - debug:
        var: ntp_server

- name: Play2
  hosts: web1
  tasks:
    - debug:
        var: ntp_server 


    The var 'ntp_server' is only accessible in Play1

        - the scope does not apply to another Play


# Global Variable Scope

---
- name: Play1
  hosts: web1
  vars:
    ntp_server: 10.1.1.1
  tasks:
    - debug:
        var: ntp_server

- name: Play2
  hosts: web1
  tasks:
    - debug:
        var: ntp_server 

>> ansible-playbook -i inventory playbook.yml \
    --extra-vars "ntp_server=10.1.1.1"


    Command Line variables apply to the entire Playbook

        - both Play1 and Play2 will display ntp_server value