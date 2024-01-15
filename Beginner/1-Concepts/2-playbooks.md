
##  Ansible Playbooks  ##     [] {} =



Playbooks define what actions to take.

    - written in YAML


Playbook:

    - single YAML file containing a set of Plays

        * a list of dictionaries


To Execute a Playbook:

    - ansible-playbook <playbook_file_name.yml>

    >> ansible-playbook playbook.yml
    >> ansible-playbook --help


Play:

    - defines a set of activities to be run 

        * a dictionary


Task:

    - single action to be performed ( run sequentially )

        * a list


Example Tasks:

    - execute a command
    - run a script
    - install a package
    - shutdown/restart


Modules:

    - the different actions run by Tasks

        * command, script, yum, service, etc


Module Info:

    - find available Modules using Ansible Docs
    - use the command "ansible-doc -l"


Hosts:

    - defined in the "inventory" file
    - Hosts must exist in the file to be used in a Playbook
    - you can also specify a Group



##  Example Playbook  ##

-
  name: Play 1
  hosts: localhost
  tasks:
    - name: Execute command 'date'          
      command: date                         ---> module

    - name: Execute script on server
      script: test_script.sh                ---> module

    - name: Install httpd service
      yum:                                  ---> module
        name: httpd
        state: present

    - name: Start web server
      service:                              ---> module
        name: httpd
        state: started
