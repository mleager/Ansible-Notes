
##  Ansible Loops  ##     [] {} =


You can use Loops in a Task to iterate over a list, etc.

Using Loops:

    - loop:
    - with_*    ( view Docs for list of available "with" directives )

Note:

    When working with a List, use "{{ item }}"


# Playbook with a Loop & List
---
- name: Create Users
  hosts: localhost
  tasks:
    - user:
        name: "{{ item }}"
        state: present
      loop:
        - joe
        - george
        - ravi
        - mani
        - mike
        - ranni


# Playbook with a List of decalred "vars"
---
-  name: 'Print list of fruits'
   hosts: localhost
   vars:
     fruits:
       - Apple
       - Banana
       - Grapes
       - Orange
   tasks:
     - command: 'echo "{{ item }}"'
       with_items:
         - "{{ fruits }}"
         
---
- name: 'Install required packages'
  hosts: localhost
  become: yes
  vars:
    packages:
      - httpd
      - make
      - vim
  tasks:
    - yum:
        name: '{{ item }}'
        state: present
      with_items: '{{ packages }}'


# Example Playbook with a Loop & List of Dicts
---
- name: Create Users
  hosts: localhost
  tasks:
    - user: 
        name "{{ item.name }}"
        state: present
        uid: "{{ item.uid }}"
      loop:
        - name: joe
          uid: 1010
        - name: george
          uid: 1011
        - name: ravi
          uid: 1012
        - name: mani
          uid: 1013
        - name: mike
          uid: 1014
        - name: ranni
          uid: 1015


# Same Playbook in JSON format
---
- name: Create Users
  hosts: localhost
  tasks:
    - user: name="{{ item.name }}" state=present uid="{{ item.uid }}"
      loop:
        - { name: joe, uid: 1010 }
        - { name: george, uid: 1011 }
        - { name: ravi, uid: 1012 }
        - { name: mani, uid: 1013 }
        - { name: mike, uid: 1014 }
        - { name: ranni, uid: 1015 }        


# Playbook with Loops using "with_*"
---
- name: Create Users
  hosts: localhost
  tasks:
    - user: name="{{ item }}" state=present
      with_items:
        - joe
        - george
        - ravi
        - mani
        - mike
        - ranni

    
# Another Exmaple of "with_*" Directives
---
- name: View Config Files
  hosts: localhost
  tasks:
    - debug: var=item
      with_file:
        - "/etc/hosts"
        - "/etc/resolv.conf"
        - "/etc/ntp.conf"
---
- name: Get from multiple URLs
  hosts: localhost
  tasks:
    - debug: var=item
      with_url:
        - "https://site1.com/get-servers"
        - "https://site2.com/get-servers"
        - "https://site3.com/get-servers"
---
- name: Check multiple MongoDBs
  hosts: localhost
  tasks:
    - debug: msg="DB={{ item.database }} PID="{{ item.pid }}"
      with_mongodb:
        - database: dev
          connection_string: "mongodb://dev.mongo/"
        - database: prod
          connection_string: "mongodb://prod.mango/"