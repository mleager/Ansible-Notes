
##  Ansible Conditionals  ##     [] {} =


You can use conditionals to determine which Tasks are run
based on if the resulting condition is True.



# Example Playbook with Conditionals

---
- name:
  hosts: all
  tasks:
    - name: Install NGINX on Debian
      apt:
        name: nginx
        state: present
      when: ansible_os_family == "Debain" and
            ansible_ditribution_version == "16.02"

    - name: Install NGINX on Redhat
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "Redhat" or
            ansible_os_family == "SUSE"


# Example Playbook with Conditionals in Loops

---
- name: Install Softwares
  hosts: all
  vars:
    packages:
      - name: nginx
        required: True
      - name: mysql
        required: True
      - name: apache
        required: False
  tasks:
    - name: Install "{{ item.name }}" on Debian
      apt:
        name: "{{ item.name }}"
        state: present
      when: item.required == True
      loop: "{{ packages }}"


# Example Playbook with Conditionals & Register

---
- name: 
  hosts: localhost
  tasks:
    - command: service httpd status
      register: result

    - mail:
        to: admin@company.com
        subject: Service Alert
        body: Httpd Service is down
        when: result.stdout.find('down') != -1


# Another Example

---
- name: Display whether use is a Child or an Adult
  hosts: localhost
  var:
    age: 25
  tasks:
    - command: 'echo "User is a Child"'
      when: age < 18
    - command: 'echo "User is an Adult"'
      when: age >= 18