
##  Ansible Dynamic Inventory  ##     [] {} =


Docs:

https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html

Ansible Inventory Examples:

https://github.com/ansible/ansible/tree/stable-2.9/contrib

    * Note: use 'stable-2.9' version tree ( not availabel after that )


Dynamic Inventory files allow you to manage hundreds of servers
without hard-coding all the Host values.


Dynamic Inventory is inventory info that Ansible retreives 
programatically when the Playbook is run.


Dynamic Inventory uses:

    - scripts
    - API Calls


# Python Inventory Scripts

    The Python script needs to output the inventory file in 
    JSON format to be read.


# JSON Inventory Structure

{
    "_meta": {      <-----------------  # Host Variables
        "hostvars": {
            "web": {
                "ansible_host": "172.20.1.100",
                "ansible_user": "john",
                "ansible_password": "Passw0rd"
            },
            "db": {
                "ansible_host": "172.20.1.101",
                "ansible_user": "maria",
                "ansible_password": "Passw0rd"
            }
        }
    },              <-----------------  # Groups
    "all": {
        "children": [
            "web_servers",
            "db_servers"
        ]
    },
    "web_servers": {
        "hosts": ["web"],
        "vars": {   <-----------------  # Group Variables
            "httpd_port": 80,
            "max_connections": 100
        }
    },
    "db_servers": {
        "hosts": ["db"],
        "vars": {   <-----------------  # Group Variables
            "mysql_port": 3306,
            "db_name": "ecomdb"
        }
    }
}


# 