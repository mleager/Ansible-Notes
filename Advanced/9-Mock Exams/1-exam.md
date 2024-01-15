
##  Ansible Mock Exam: 1  ##     [] {} =



1. Create the Playbook 'add_users.yml' on node00 to do the following:
    - add all users in data/users.yml
    - make home dir for users in developers group to '/var/www/'
    - encrypt and use for Developer user's password: 'd3v3l0p3r'
    - encrypt and use for Admin user's password: 'adm$n$'
    - add admin users must be sudoers ( add to group 'wheel' )


    a. encrypt admin password
        >> ansible-vault encrypt_string 'adm$n$'
        * copy output 

    b. encrypt developer password
        >> ansible-vault encrypt_string 'd3v3l0p3r'
        * copy output

    c. create Playbook


---
- hosts: node00
  vars:
    admin_pass: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          33653035616639393861666332343133626531616333366430376239663966383531623033346132
          3930643336336132646562333531633265393133383832370a366466616533663763336266333833
          31316435303365613333373239646361376533663431363331613238313363353638316539633161
          3137666434323463610a353331346330396331353334333563663030306364316239323635303962
          3832

    dev_pass: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66303438313763616166373535316338616437336266396265623862323437333731373533366638
          3562363235626162303733306239313933383965633363330a626433663466663836653263636437
          34666137393437353463636137613232303265336262393534313638383833346461653339663036
          3635393865616361620a663936313664616238393232313065303639643338646333623963353535
          3137

  tasks:
    - include_vars: data/users.yml

    - name: Add Admin Users
      user:
        name: "{{ item }}"
        password: "{{ admin_pass | string | password_hash('sha512') }}"
        groups: wheel
      loop: "{{ admins | list }}"

    - name: Create Developer Users
      user:
        name: "{{ item }}"
        password: "{{ dev_pass | string | password_hash('sha512') }}"
        home: /var/www
      loop: "{{ developers | list }}"


## --------------------------------------------------------------- ##


2. Create the Playbook 'apache.yml' on node01 to do the following:
    - Install 'http' & 'php' packages
    - Change Apache DocuemntRoot to '/var/www/html/myroot'
    - Copy template 'phpinfo.php.j2' ( owner & group: apache )
    - Start & enable 'httpd'
    - Add Firewall rule for http port 80 to enable access


---
- hosts: node01
  tasks:
    - name: Install Packages
      yum:
        name:
          - httpd
          - php
        state: present


    - name: Create new DocumentRoot for Apache
      file:
        path: /var/www/html/myroot
        state: directory
        owner: apache
        group: apache

    - name: Change DocumentRoot for Apache Config file
      replace:
        path: /etc/httpd/conf/httpd.conf
        regexp: 'DocumentRoot "/var/www/html"'
        replace: 'DocumentRoot "/var/www/html/myroot"'

    - name: Copy Template
      template:
        src: templates/phpinfo.php.j2
        dest: /var/www/html/myroot/phpinfo.php
        owner: apache
        group: apache

    - name: Start & Enable HTTPD service
      service:
        name: httpd
        enabled: true
        state: started

    - name: Add Firewall Rule for HTTPD Port 80
      firewalld:
        port: 80/tcp
        zone: public
        state: enabled
        permanent: true


## --------------------------------------------------------------- ##


3. Create the Playbook 'database.yml' on node02 to do the following:
    - Start 'nginx' & 'mariadb' services
    - Delete all foldes under '/usr/share/nginx/html'
    - Download zip archive and extract to '/usr/share/nginx/html'
    - Configure DB ( use either replace or lineinfile )
    - Restart nginx


---
- hosts: node02
  tasks:
    - name: Start Nginx & MariaDB
      service:
        name: "{{ item }}"
        state: started
      loop:
        - nginx
        - mariadb

    - name: Delete folders under '/usr/share/nginx/html'
      file:
        path: /usr/share/nginx/html/*
        state: absent

    - name: Download and copy zip archive
      unarchive:
        src: https://github.com/indercodes/ansible-1100-mock-nginx/raw/master/index.php.zip
        dest: /usr/share/nginx/html
        remote_src: true

# Loop over a Dict to Replace Key with Value
    - name: Configure DB 
      replace:
        path: /usr/share/nginx/html/index.php
        regexp: "{{ item.key }}"
        replace: "{{ item.value }}"
      loop: "{{ db_data | dict2items }}"
      vars:
        db_data:
          '\$database.*': '$database = "mydb";'
          '\$username.*': '$username = "myuser";'
          '\$password.*': '$password = "mypassword";'

    - name: Restart Nginx service
      service:
        name: nginx
        state: restarted


## --------------------------------------------------------------- ##


4. Create a Playbook 'facts.yml' on node02 to do the following:
    - Use blockinfile to to create a file at '/root/facts.txt'
    - Info for Block to contain:
        This is Ansible managed node <hostname-of-node>
        IP address of host is <ip-address-of-host>
        Its OS family is <is-family>
    - Copy the completed file to '/usr/share/nginx/html/index.html'


---
- hosts: node02
  gather_facts: true
  tasks:
    - name: Create Block facts.txt
      blockinfile:
        path: /root/facts.txt
        create: true
        block: |
          This is Ansible managed node {{ ansible_nodename }}
          IP address of host is {{ ansible_default_ipv4.address }}
          Its OS family is {{ ansible_os_family }}
    
    - name: Copy facts.txt
      copy:
        src: /root/facts.txt
        dest: /usr/share/nginx/html/index.html
        remote_src: true
