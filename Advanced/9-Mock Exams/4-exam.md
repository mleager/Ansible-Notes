
##  Ansible Mock Exam: 4  ##     [] {} =



1. Perform the following tasks:
    - install ansible using the package manager ( if not installed )
    - generate your SSH key to path '~/.ssh/id_rsa
    - push the Public Key to the remote servers
    - use an adhoc command to test that the remotes are connnected


a. Check if Ansible is installed 

>> ansible-inventory -i inventory --list -y


b. Generate SSH Keys

>> ssh-keygen -t rsa 


c. Copy to node00

>> ssh-copy-id root@node00


d. Copy to node01

>> ssh-copy-id root@node01


e. Test connection

>> ansible all -m ping -i inventory


f. Update inventory

node00 ansible_host=172.20.1.100 ansible_user=root ansible_ssh_password_file=/home/thor/.ssh/id_rsa.pub

node01 ansible_host=172.20.1.101 ansible_user=root ansible_ssh_password_file=/home/thor/.ssh/id_rsa.pub


## --------------------------------------------------------------- ##


2. Create the Playbook 'add_user_with_ssh.yml' on all hosts to:
    - create the user 'deploy'
    - copy the Public Key from 'playbooks/devops.pub' to the
      'deploy' user's 'authorized_keys' file


---
- hosts: all
  tasks:
    - name: Create User
      user:
        name: deploy
        state: present

    - name: Copy SSH Key
      authorized_key:
        user: deploy
        state: present
        key: "{{ lookup('file', 'devops.pub') }}"


## --------------------------------------------------------------- ##


3. Create the Playbook 'install_from_source.yml' on all hosts to:
    - install the tool 'mosh' from github
    - install all necessary dependencies
    - active tool


---
- hosts: all
  tasks:
    - name: Install dependencies
      package:
        name: "{{ item }}"
        state: present
      loop:
        - git
        - make
        - autoconf
        - automake
        - protobuf-devel
        - libutempter-devel
        - ncurses-devel
        - openssl-devel
        - gcc
        - gcc-c++

    - name: Download mosh from Git 
      git:
        repo: 'https://github.com/mobile-shell/mosh'
        dest: /tmp/mosh
        #force: true

    - name: Run commands to start mosh
      shell: ./autogen.sh && ./configure && make && make install 
      args:
        chdir: /tmp/mosh


## --------------------------------------------------------------- ##


4. Create the Playbook 'logrotate.yml' on all hosts to:
    - get the module from GitHub
    - use ansible-galaxy to install module in '/playbooks/roles'
    - configure log rotation rules as: 
        - daily | rotate 3 | compress


a. Install logrotate module from GitHub URL

>> ansible-galaxy install git+https://github.com/arillso/ansible.logrotate --roles-path ~/playbooks/roles


b. Configre ansible.logrotate 

>> vi roles/ansible.logrotate/defaults/main.yml
      
* Bottom of file - add:

logrotate_applications:
  - name: myapp
    definitions:
      - logs:
          - /var/log/myapp.log
        options:
          - daily
          - rotate 3
          - compress


c. Create Playbook

---
- hosts: all
  gather_facts: true
  roles:
    - ansible.logrotate
