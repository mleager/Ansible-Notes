
##  Ansible Blocks  ##     [] {} =



Blocks allow you to logically group tasks together.

With 'block' you can use 2 additional parameters:

    - rescue
    - always 


# Use Blocks to organize the Tasks 
---
- hosts: server1
  tasks:
    - block:
      - name: Install MySQL
        yum:
          name: mysql-server
          state: present
      - name: Start MySQL service
        service:
          name: mysql-server
          state: started
      become_user: db-user
      when: ansible_facts.distribution == 'CentOS'
      
      # Only invoked if a task in the blcok fails
      rescue:
        - mail:
            to: admin@company.com
            subject: Installation Failure
            body: DB Install Failed at {{ ansible_failed_task.name }}
      
      # Invoked whether the task is successful or not
      always:
        - mail:
            to: admin@company.com
            subject: Installation Status
            body: DB Install Status - {{ ansible_failed_result }}

    - block:
        - name: Install Nginx
          yum:
            name: nginx
            state: present
        - name: Start Nginx service
          service: 
            name: nginx
            state: started
      become_user: web-user
      when: ansible_facts.distribution == 'CentOS'

    