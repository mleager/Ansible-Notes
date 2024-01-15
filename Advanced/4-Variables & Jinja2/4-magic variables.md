
##  Ansible Magic Variables  ##     [] {} =


Docs:

    https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html


# Magic Variables - Hosts

You can get access to variables and/or facts defined on other Hosts using:

    - hostvars


* Syntax: 

    hostvars[ <hostname> ]


Ex:

---
- name: Print DNS Server
  hosts: all
  tasks:
    - debug:
        msg: "{{ hostvars['web2'].dns_server }}"


* Get Host names

    msg: "{{ hostvars['web2'].ansible_host }}"


* Get Host's architecture

    msg: "{{ hostvars['web2'].ansible_facts.architecture }}"


* Get Host's device ino

    msg: "{{ hostvars['web2'].ansible_facts.device }}"


# Magic Variables - Groups & Group_Names

* Groups:
    
    Return all Hosts under a given group 

        msg: "{{ groups.web_servers }}"


* Group_Names:

    Return all Groups a Host is part of

        msg: "{{ group_names.web1 }}"


# Magic Variable - Inventory_Hostname

Returns the name configured for the Host in the inventory file 

    msg: "{{ inventory_host }}"
