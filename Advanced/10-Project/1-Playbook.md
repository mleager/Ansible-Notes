
##  Ansible Project - Modules: 1  ##        [] {} =



# inventory
[db_servers]
lamp-db ansible_host=172.20.1.101 ansible_ssh_private_key_file=/home/thor/.ssh/maria ansible_user=maria mysqlservice=mysqld mysql_port=3306 dbname=ecomdb dbuser=ecomuser dbpassword=ecompassword

[web_servers]
lampweb ansible_host=172.20.1.100 ansible_ssh_private_key_file=/home/thor/.ssh/john ansible_user=john httpd_port=80 repository=https://github.com/kodekloudhub/learning-app-ecommerce.git


1. Create a Playbook on all Hosts to install to required packages

# deploy-lamp-stack.yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      package:
        name:
          - libselinux-python
          - libsemanage-python
          - firewalld
        state: present


## --------------------------------------------------------------- ##


2. Update the Playbook to perform the following tasks on 'lamp-db':
    - install mariadb
    - copy MySQL config file
    - start/enabled mariadb & firewalld
    - insert firewall rule for MySql port

# deploy-lamp-stack.yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      ...
    
- name: Install & Configure DB Server
  hosts: lamp-db
  become: true
  tasks:
    - name: Install MariaDB Packages
      yum:
        name:
          - mariadb-server
          - MySQL-python
        state: present
    
    - name: Copy MySQL Config File
      copy:
        src: files/my.cnf
        dest: /etc/my.cnf

    - name: Start & Enable MariaDB & Firewalld
      service:
        name: "{{ item }}"
        state: started
        enabled: true
      loop:
        - mariadb
        - firewalld

    - name: Insert Firewall Rule for MariaDB Port
      firewalld:
        port: "{{ mysql_port}}/tcp"
        zone: public
        state: enabled
        permanent: true
        immediate: true


## --------------------------------------------------------------- ##


3. Update the Playbook to add the following to the 'lamp-db' host:
    - create database
    - create database user
    - copy 'db-load-script.sql'
    - load db inventory from the script

# deploy-lamp-stack.yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      ...
    
- name: Install & Configure DB Server
  hosts: lamp-db
  become: true
  tasks:
    - name: Install MariaDB Packages
      ...
    ...

    - name: Create Database
      mysql_db:
        name: "{{ dbname }}"
        state: present

    - name: Create DB User
      mysql_user:
        name: "{{ dbuser }}"
        password: "{{ dbpassword }}"
        priv: "*.*:ALL"
        #host: "172.20.1.100"
        state: present

    - name: Copy DB Script
      copy:
        src: files/db-load-script.sql
        dest: /tmp/db-load-script.sql

    - name: Load DB Data from Script
      shell: mysql -f < /tmp/db-load-script.sql


## --------------------------------------------------------------- ##


4. Update the Playbook to perform the following tasks on 'lampweb':
    - install web server
    - install git
    - start & enable firewalld
    - insert firewall rule for httpd port
    - set 'index.php' as default for httpd
    - start & enable httpd

# deploy-lamp-stack.yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      ...
    
- name: Install & Configure DB Server
  hosts: lamp-db
  become: true
  tasks:
    - name: Install MariaDB Packages
      ...
    ...

- name: Install & Configure Web Server
  hosts: lampweb
  become: true
  tasks:
    - name: Install Packages
      package:
        name: "{{ item }}"
        state: present
      loop:
        - httpd
        - php
        - php-mysql
        - git

    - name: Start & Enable Firewalld
      service:
        name: firewalld
        state: started
        enabled: true

    - name: Insert Firewall Rule for HTTPD Port
      firewalld:
        port: "{{ httpd_port }}/tcp"
        zone: public
        state: enabled
        permanent: true
        immediate: true

    - name: Set index.php as Default
      replace:
        path: /etc/httpd/conf/httpd.conf
        regexp: "DirectoryIndex index.html"
        replace: "DirectoryIndex index.php"

    - name: Start & Enable HTTPD
      service:
        name: httpd
        state: started
        enabled: true

## --------------------------------------------------------------- ##


5. Update the Playbook to perform the following tasks for 'lampweb':
    - clone source code from git repo
    - copy custom index.php file

# deploy-lamp-stack.yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      ...
    
- name: Install & Configure DB Server
  hosts: lamp-db
  become: true
  tasks:
    - name: Install MariaDB Packages
      ...
    ...

- name: Install & Configure Web Server
  hosts: lampweb
  become: true
  tasks:
    - name: Install Packages
      ...
    ...

    - name: Get Source Code from Git Repo
      git:
        repo: "{{ repository }}"
        dest: /var/www/html/
        force: true

    - name: Copy Local index.php File
      copy:
        src: files/index.php
        dest: /var/www/html/index.php


## --------------------------------------------------------------- ##


6. Click 'Web App' Link to make sure webpage & DB are working

    - SUCCESS