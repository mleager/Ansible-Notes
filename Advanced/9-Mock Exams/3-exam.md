
##  Ansible Mock Exam: 3  ##     [] {} =



1. Create the Playbook 'update_dns_server.yml' on all hosts to:
    - update the resolv.conf template to use the host's dns server
    - copy the template to /tmp/resolv.conf


templates/resolv.conf.j2
------------------------
nameserver  {{ dns_server }}
options ndots:0

---
- hosts: all
  tasks:
    - name: Copy template
      template:
        src: templates/resolv.conf.j2
        dest: /tmp/resolv.conf


## --------------------------------------------------------------- ##


2. Create the Playbook 'blocks.yml' on all hosts to:
    - use 'block' to group the tasks
    - install httpd
    - start the service


---
- hosts: all
  tasks:
    - name: Install HTTPD & Start Service
      block:
        - yum: 
            name: httpd
            state: present
        - service:
            name: httpd
            state: started
      

## --------------------------------------------------------------- ##


3. Create the Playbook 'firewall.yml' on node00 to:
    - install firewalld
    - whitelist node01's IP address on node00


---
- hosts: node00
  tasks:
    - name: Install Firewalld
      yum:
        name: firewalld
        state: present
    
    - name: Start Firewalld
      service:
        name: firewalld
        state: started

    - name: Whitelist node01's IP Address
      firewalld:
        source: 172.20.1.101
        zone: internal
        state: enabled
        premanent: true
        immediate: true
