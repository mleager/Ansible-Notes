
##  Ansible Create Shell Script That Runs Ahdoc Commands  ##   [] {} =


You can create a Shell Script to use multiple Adhoc Commands in order

    - you can also set ENV Variables before running the commands


shell-script.sh
---------------

export ANSIBLE_GATHERING=explicit
ansible -m ping all
ansible -a 'cat /etc/hosts' all
ansible-playbook playbook.yml 


>> sh shell-script.sh

    * or set permissions and run 

    >> chmod 755 shell-script.sh 
    >> ./shell-script.sh 



## Examples ##


# Ex 1: 

Create a script called 'host_details.sh' that:
    a. prints all hostnames
    b. copies /etc/resolv.conf to /tmp/resolf.conf on node00


host_details.sh
---------------
ansible -a "hostname" -i inventory all
ansible -m copy -a "src=/etc/resolf.conf dest=/tmp/resolv.conf" -i inventory node00

>> chmod 755 host_details.sh
>> ./host_details.sh


# Ex 2: 

Create a script called "host_data.sh" that:
    a. sets 'gathering' to False
    b. print the 'uptime' of all managed nodes in the inventory
    c. create and run a playbook 'playbook.yml' to cat '/etc/redhat-release'
       on all managed nodes in the inventory file in verbose mode


host_data.sh
------------
export ANSIBLE_GATHERING=explicit
ansible -m shell -a 'uptime' -i inventory all
ansible-playbook -i inventory playbook.yml -vv

playbook.yml
------------
- hosts: all
  tasks:
    - shell: cat /etc/redhat-release

>> chmod 755 host_data.sh
>> ./host_data.sh