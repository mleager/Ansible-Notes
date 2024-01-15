
##  Ansible Use Vaiables to Retrieve Command Results  ##     [] {} =



You can store the ouput of one task as the input of another.

    - "register" parameter


# Capture the output of 1st command and pass it to the 2nd command

playbook.yml
---
- name: Check /etc/hosts file
  hosts: all
  tasks:
    - shell: cat /etc/hosts
      register: result

    - debug:
        var: result.stdout_lines


    The 'registered' value set to the Host scope

        - they can be used on consecutive Plays in the same Playbook