
##  Ansible Project - Roles: 3  ##        [] {} =


* Continues from "10-Project/2-Variables"


Directory Structure:

    inventory
    tasks
      --> common.yml
      --> db.yml
      --> web.yml
    templates
      --> sb-load-script.sql.j2
      --> index.php.j2
      --> my.cnf.j2
    host_vars
      --> lamp-db.yml
      --> lampweb.yml
    group_vars
      --> db_servers.yml
      --> web_servers.yml


1. Create 3 Roles named 'common', 'httpd-php', & 'mysql':

    >> ansible-galaxy init roles/common
    >> ansible-galaxy init roles/httpd-php
    >> ansible-galaxy init roles/mysql


## --------------------------------------------------------------- ##


2. Moves Tasks from the 'tasks' directory to the proper Roles directory:

    >> cp tasks/common.yml roles/common/tasks/main.yml
    >> cp tasks/db.yml roles/mysql/tasks/main.yml
    >> cp tasks/web.yml roles/httpd-php/tasks/main.yml


## --------------------------------------------------------------- ##


3. Update the main Playbook to use the created Roles:

    # deploy-lamp-stack.yml
    ---
    - name: Deploy lamp stack application
    hosts: all
    become: yes
    roles:
        - common

        # Install and Configure Database
    - name: Deploy lamp stack application
    hosts: lamp-db
    become: yes
    roles:
        - mysql

    - name: Deploy lamp stack application
    hosts: lampweb
    become: yes
    roles:
        - httpd-php


## --------------------------------------------------------------- ##


4. Run the Playbook

    >> ansible-playbook -i inventory deploy-lamp-stack.yml -v


## --------------------------------------------------------------- ##


5. Click 'Web App' link to ensure web & db server are working:

    - SUCCESS