
##  Ansible Use Conditionals to Control Play Execution  ##     [] {} =



You can use conditionals to control which Plays are run
depending on the scenario.


# Playbook that install nginx depending on the OS

---
- name: Install Nginx
  hosts: all
  tasks:
    - name: Install Nginx on Debian
      apt:
        name: nginx
        state: present
      when: ansible_os_family == "Debain" and
            ansible_distribution_version == "16.04"

    - name: Install Nginx on Redhat
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "Redhat" or
            ansible_os_family == "SUSE"

* NOTE: 'ansible_os_family' is a builtin varaible


# Conditionals in Loops

---
- name: Install softwares
  hosts: all
  vars:
    packages:
      - name: nginx
        required: true
      - name: mysql
        required: true
      - name: apache
        required: false
  tasks:
    - name: Install "{{ item.name }}" on Debian
      apt:
        name: "{{ item.name }}"
        state: present
      when: item.required == True
      loop: "{{ packages }}"

# Breakdown

    - name: Install "{{ item.name }}" on Debian
      vars:
        item:
          name: nginx
          required: true
      vars:
        item:
          name: mysql
          required: true
      vars:
        item:
          name: apache
          required: false


# Conditionals & Register

---
- name: Check status of a service and email if it's down
  hosts: localhost
  tasks:
    - command: service httpd status
      register: result

    - mail:
        to: admin@company.com
        subject: Service Alert
        body: Httpd Service is down
        when: result.stdout.find('down') != -1