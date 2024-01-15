
##  Ansible Facts  ##     [] {} =


Ansible gathers Facts from the Target machine when you run a Playbook

    - Facts are a collection of info from the Hosts in a Play


Facts from an Ansible Target include:

    - basic system info      ( OS, version, processor/memory details, etc. )
    - network connectivity info     ( interfaces, IP addresses, FQDN, etc. )
    - device info                           ( disks, volumes, mounts, etc. )


Ansible gathers these Facts using the 'setup module'

    - runs automatically when you apply a Playbook


All Facts gathered from Ansible are stored in a variable:

    - ansible_facts 


# Playbook to print the Ansible Facts:

---
- name: Print Facts
  hosts: all
  tasks:
    - debug:
        var: ansible_facts 


# Playbook to disbale Facts:

---
- name: Disable Facts for this Play
  hosts: all
  gathers_facts: no
  tasks:
    - debug: 
        msg: Hello from Ansible!


Facts are also defined in '/etc/ansible/ansible.cfg' and can be disabled:

    /etc/ansible/ansible.cfg
    ------------------------
    # plays gather facts by default, which contain information about ...
    # smart - gather by default, but don't regather if already gathered
    # implicit - gather by default, turn off with 'gather_facts: False'
    # explicit - do not gather by default, to gather 'gather_facts: True'
    gathering = implicit
