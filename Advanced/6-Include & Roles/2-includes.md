
##  Ansible Includes_*  ##     [] {} =



You can use Tasks and Variables that are stored at other
locations on the system in a Playbook.


# Include_Vars

    Import a Variable stored in a file outside the Playbook folder


/opt/apps/common-data/email/info.txt
------------------------------------
admin_email: admin@company.com


playbook.yml
---
- name: Send Email Alert
  hosts: web-db-server
  tasks:
    - include_vars:
        file: /opt/apps/common-data/email/info.yml
        name: email_data
    
    - mail:
        to: "{{ email_data.admin_email }}"
        subject: Service Alert
        body: Httpd service is down

    * Use <include_vars.name> . <variable in the file to use>
      to use the correct variable from the 'include_vars' file


# Include_Tasks

    Re-use a Task defined in another location 

        * allows you to re-use Tasks in different Playbooks


    You can break down Tasks into individual files, similar
    to using the 'host_vars' and 'group_vars' folder structure


1. Create a 'tasks' folder 

2. Give it identifiable names, but theres no naming requirement 


- playbook.yml
- inventory/
  |--> inventory
  |--> host_vars
       |--> web1.yml
       |--> web2.yml
       |--> web3.yml
  |--> group_vars
       |--> web_servers.yml
- tasks
  |--> db.yml
  |--> web.yml
  

tasks/db.yml
------------
- name: Install MySQL Packages
  ...
    ...

- name: Start MySQL Service
  ...
    ...

- name: Configure Database
  ...
    ...


tasks/web.yml
-------------
- name: Install Python Flask Dependencies
  ...
    ...

- name: Run Web-Server
  ...
    ...


playbook.yml
------------
- name: Deploy Web & DB Server
  hosts: web-db-server
  tasks:
    - name: Run DB Task
      include_tasks: tasks/db.yml
    
    - name: Run Web Task
      include_tasks: tasks/web.yml