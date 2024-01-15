
##  Ansible Manage Parallelism  ##     [] {} =



Strategies are defined at the Play-Level.

By default, 5 Hosts are run at a time.

This is defined by the variable 'forks' in '/etc/ansible/ansible.cfg'


# Linear Strategy

    The default strategy Ansible uses to execute a Playbook.

    When a Playbook is run with multiple Hosts, 
    each Task is run on all Hosts at the same time.

    Once the Task is completed on each Host, it moves to the next Task.

    If one Host is slow, it slows down the entire Playbook execution.


# Free Strategy

    Each Host runs all of its Tasks independently of eachother.

    It does not wait for Tasks to finish on other Hosts.

    ---
    - name: Deploy Web App
      hosts: all
      strategy: free
      tasks:
        - ...
            ...


# Batch Strategy

    Uses the same strategy as Linear, 
    except you specify how many Hosts to run together.

    Ex: 
    
        You have 10 Hosts, and specify a Play to run 3 at a time.

        When the 3 Hosts successfully complete the Play,
        3 more Hosts are run - and so on until all Hosts have completed.

    ---
    - name: Deploy Web App
      hosts: all
      serial: 3
      tasks:
        - ...
            ...