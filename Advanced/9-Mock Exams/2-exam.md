
##  Ansible Mock Exam: 2  ##     [] {} =



1. Create the Playbook 'update_version.yml' on all hosts to:
    - install the latest version of 'awscli' using pip


---
- hosts: all
  tasks:
    - name: Update awscli 
      pip:
        name: awscli
        state: latest
        executable: pip3


## --------------------------------------------------------------- ##


2. Create the Playbook 'give_ssh_access.yml' on all hosts to:
    - give dev 'John Doe' ssh access as root user to all remote servers


---
- hosts: all
  tasks:
    - name: Give Root SSH Access
      authorized_key:
        user: root
        state: present
        key: "{{ lookup('file', 'john_doe.pub') }}"


## --------------------------------------------------------------- ##


3. Create the Playbook 'configure_webserver.yml' on all hosts to:
    - install nginx
    - copy local index.html to '/usr/share/nginx/html/' on remotes


---
- hosts: all
  tasks:
    - name: Install Nginx
      yum:
        name: nginx
        state: present

    - name: Copy index.html to remote servers
      copy:
        src: index.html
        dest: /usr/share/nginx/html/

    - name: Start Nginx Service
      service:
        name: nginx
        state: started


## --------------------------------------------------------------- ##


4. Create the Playbook 'copy_secrets.yml' on all hosts to:
    - copy the encrypted file 'secret_file.txt' to '/root/.secret_file.txt'
    - use the vault password from the script 'get_vault_pass.py'


---
- hosts: all
  tasks:
    - name: Copy file
      copy:
        src: secret_file.txt
        dest: /root/.secret_file.txt

>> ansible-playbook -i inventory copy_secrets.yml \
    --vault-password-file get_vault_pass.py -v


## --------------------------------------------------------------- ##


5. Create the Playbook 'patch_system.yml' on all hosts to:
    - install and configure 'yum-cron' package
    - edit the config file '/etc/yum/yum-cron.conf' 
        * ( update_cmd = security )


---
- hosts: all
  tasks:
    - name: Install Package
      yum:
        name: yum-cron
        state: present

    - name: Edit Config
      lineinfile:
        path: /etc/yum/yum-cron.conf
        regexp: "^update_cmd*"
        line: "update_cmd = security"

    - name: Restart Service
      service:
        name: yum-cron
        state: restarted
