
##  Ansible Adhoc Commands  ##     [] {} =


Adhoc Commands are one-liners that can be used to test your Playbooks.


# To use a specific Module, use the syntax:

    " -m <module-name> <host-name> "


Ex 1: "ping" a Target Node to make sure the Controller can connect

    * ansible -m ping <target host>

    >> ansible -m ping web1 


Ex 2: "ping" the localhost and save output to '/tmp/ansible_ping.txt'

    >> ansible -m ping localhost > /tmp/ansible_ping.txt



# To run a command instead of using a Module, use the syntax:

    " -a <command> <host-name> "


Ex 1: "cat" the /etc/hosts file of All Hosts:

    * ansible -a <command> <host-name>

    >> ansible -a 'cat /etc/hosts' all 


Ex 2: install nginx in All Hosts:

    >> ansible -a "yum install nginx -y" all


Ex 3: get ansible version and save output to '/tmp/ansible_version.txt'

    >> ansible --version > /tmp/ansible_version.txt