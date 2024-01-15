
##  Ansible Privilege Escalation  ##     [] {} =


# Users

    Best Practice is to have segregated users, 
    each with their own levels of permissions

        - root
        - admin
        - dev
        
    
    Software should also have a user account and permissions:

        - nginx
        - mysql
        - ansible 


# Users Workflow

    1. Admin logs into the machine using credentials ( passwords or ssh )

        >> ssh -i id_rsa admin@server1

    
    2. Install the required packages/software/applications onto the server 

        - you need certain privileges to do this 

        >> sudo yum install nginx 


    3. Admin configures the installed applications

        - create and/or switch to a user for each app and configure it 

        >> su nginx
            * configure ...

        >> su mysql 
            * configure ...


# Privilege Escalation Methods

    - sudo
    - pfexec
    - doas
    - ksu
    - runas 



##       ---- Examples ----        ## 


# 1. Running a Playbook with a User that doesn't have proper permissions

    inventory 
    ---------
    lamp-dev1 ansible_host=172.20.1.100 ansible_user=admin

    playbook
    --------
    - name: Install Nginx
      hosts: all
      tasks:
        - yum:
            name: nginx
            state: latest 

    * PERMISSION DENIED 


# 2. Allow Privilege Escalation to run the same Playbook

    playbook
    --------
    - name: Install Nginx
      become: true   <------- **
      hosts: all
      tasks:
        - yum:
            name: nginx
            state: latest

    * PERMISSION GRANTED 
        ( installed using "admin" user but with root privileges )



# 3. Run the same Playbook as another User 

    playbook
    --------
    - name: Install Nginx
      become: true         <------- **
      become_user: nginx   <------- **
      hosts: all
      tasks:
        - yum:
            name: nginx
            state: latest 

    * PERMISSION GRANTED 
        ( nginx user is configured to have required permissions )



#       ---- Privilege Order of Presedence ----         #

    You can set 'become' and other options like 'become_user' 
    in the following order of lowest to highest:

        - ansible.cfg
        - inventory
        - playbook
        - command line arguemnts


    
# Set Privilege Escalation in Config File

ansible.cfg
-----------
become          = True
become_method   = doas
become_user     = nginx


# Allow Privilege Escalation and Become another User in an Inventory File

inventory
---------
lamp1-dev ansible_host=172.20.1.100 \
    ansible_user=admin \
    ansible_become=true \
    ansible_become_user=nginx

    * NOTE: requires 'ansible_' prefix


# Privilege Escalation in a Playbook

playbook.yml
------------
- hosts: all
  become: true
  become_user: nginx
  ...


# As Command Line Arguemnts

>> ansible-playbook -i inventory playbook.yml \
    --become \
    --become-method=doas \
    --become-user=nginx \
    --ask-become-pass