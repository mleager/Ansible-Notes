
##  Ansible Project - Variables: 2  ##        [] {} =


* Continues from "10-Project/1-Playbook"


1. Update the Playbook to perform the following tasks:
    * 'Create Application DB User' task
    - update lampweb's IP address to use a variable,
      rather than hard-coding the value


    # deploy-lamp-stack.yml
    ---
    - hosts: all
      become: true
      tasks:
        - ...
        ...
    
    - hosts: lamp-db
      become: true
      tasks:
        - name: ...
          ...

        - name: Create Application DB User
          mysql_user: name={{ dbuser }} password={{ dbpassword }} priv=*.*:ALL host={{ hostvars['lampweb'].ansible_host }} state=present

    * Before: host=172.20.1.100
    * After:  host={{ hostvars['lampweb'].ansible_host }}


## --------------------------------------------------------------- ##


2. Convert 'db-load-script.sql' into a Jinja2 template to replace
   the hard-coded DB Name with the variable 'dbname':

   >> mkdir templates
   >> cp files/db-load-script.sql templates/db-load-script.sql.j2
   >> vi templates/db-load-script.sql.j2 
        CREATE {{ dbname }};
        ...


## --------------------------------------------------------------- ##


3. Convert 'my.cnf' into a Jinja2 template to replace the hard-coded
   port with the variable 'mysql_port':

   >> cp files/my.cnf templates/my.cnf.j2
   >> vi templates/my.cnf.j2
        ...
        port={{ mysql_port }}
        

## --------------------------------------------------------------- ##


4. Convert 'index.php' into a Jinja2 template to replace the following
   hard-coded variables:
    - 172.20.1.101 -->  lamp-db's IP address
    - ecomuser     -->  dbuser
    - ecompassword -->  dbpassword
    - ecomdb       -->  dbname

   >> cp files/index.php templates/index.php.j2
   >> vi templates/index.php.j2
        
    * Before:
        ...
        ...
        $link = mysqli_connect('172.20.1.101', 'ecomuser', 'ecompassword', 'ecomdb');

    * After:
        ...
        ...
        $link = mysqli_connect(
            "{{ hostvars['lamp-db']['ansible_facts']['eth0']['ipv4']['address'] }}", 
            "{{ hostvars['lamp-db']['dbuser'] }}", 
            "{{ hostvars['lamp-db']['dbpassword'] }}", 
            "{{ hostvars['lamp-db']['dbname'] }}"
        );


## --------------------------------------------------------------- ##


5. Update the Playbook to use all of the templates:
    - templates/db-load-script.sql.j2
    - templates/my.cnf.j2
    - templates/index.php.j2

    # deploy-lamp-stack.yml
    ---
    - hosts: all
      become: true
      tasks:
        - ...
        ...
    
    - hosts: lamp-db
      become: true
      tasks:
        - name: ...
          ...

        - name: Create Mysql configuration file
          template:
            src: templates/my.cnf.j2
            dest: /etc/my.cnf

        - name: ...
          ...
        
        - name: Move db-load-script to db host
          template:
            src: templates/db-load-script.sql.j2
            dest: /tmp/db-load-script.sql

    - hosts: lampweb
      become: true
      tasks:
        - name: ...
          ...

        - name: Creates the index.php file
          template: 
            src: templates/index.php.j2 
            dest: /var/www/html/index.php


## --------------------------------------------------------------- ##


6. Click the 'Web App' link to ensure the web & db server are working:

    - SUCCESS



# Lamp-db variables when Play run from Lampweb

{{ hostvars['lamp-db']['ansible_facts']['eth0']['ipv4']['address'] }}, 
{{ hostvars['lamp-db']['dbuser'] }}, 
{{ hostvars['lamp-db']['dbpassword'] }}, 
{{ hostvars['lamp-db']['dbname'] }}



# Print lampweb IP address from lamp-db playbook
---
- hosts: lamp-db
  gather_facts: no

  tasks:
    - name: Print lampweb IP address
      debug:
        var: hostvars['lampweb'].ansible_host


    * NOTE: Use 'ansible_host' variable that's defined in the inventory


# ---- Same Thing? ---- #
{{ hostvars['lampweb']['ansible_facts']['eth0']['ipv4']['address'] }}
{{ hostvars['lampweb'].ansible_host }}