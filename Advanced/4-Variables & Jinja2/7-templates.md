
##  Ansible Using Templates to Create Customized Config Files  ##  [] {} =



You can use variables in Playbooks that change values based on their Hosts.


To do this, you must do 2 things:

    - specify the file as a Jinja2 template ( filename.txt.j2 )
    - use the 'template' paramater instead of 'copy'


# Playbook to print Host name on each server

inventory
---------
[web_servers]
web1 ansible_host=172.20.1.100
web2 ansible_host=172.20.1.101
web3 ansible_host=172.20.1.102

index.html.j2
-------------
<!DOCTYPE html>
<html>
<body>
This is {{ inventory_hostname }} server
</body>
</html>

playbook
--------
- hosts: web_servers
  tasks:
    - name: Copy index.html to remote servers
      template:
        src: templates/index.html.j2
        dest: /var/www/html/index.html


# Template Examples

name_servers:
  - 10.1.1.2
  - 10.1.1.3
  - 8.8.8.8

/etc/resolv.conf.j2
-------------------
{% for name in name_servers -%}
nameserver {{ name }}
{% endfor %}

/etc/resolv.conf
----------------
nameserver 10.1.1.2
nameserver 10.1.1.3
nameserver 8.8.8.8