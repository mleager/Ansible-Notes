
##  Ansible Configure Error Handling  ##     [] {} =



# Task Failure

    When running a Playbook against multiple Hosts,
    a failed task on a Host will stop the chain for the Host.

    The other Hosts will continue until they succeed or fail.

        - each Host is independent 


# Any_Errors_Fatal: Stop the Playbook on all Hosts if a single Host fails

    - any_errors_fatal: true

    ---
    hosts: all
    any_errors_fatal: true
    tasks: 


# Max_Fail_Percentage: Fail entire Playbook if % of Hosts fail

    - max_fail_percentage: < num >

    ---
    hosts: all
    max_fail_percentage: 30
    tasks:


# Ignore_Errors: Ignore any errors in Playbook, Play, or Task

    - ignore_errors: true

    ---
    hosts: all
    ignore_errors: true
    tasks:
    
    ---
    hosts: all
    tasks:
        - name: Install DB
          ...
            ...
          ignore_errors: true 

    
# Failed_When: Implement a Health Check on a Task

    - failed_when: 

    ---
    hosts: all
    tasks:
      - name: If Error in log, fail the command
        command: cat /var/log/server.log
        register: command_output
        failed_when: 'ERROR' in command_output.stdout


# Error Handling in Blocks

    hosts: all
    tasks:
      - block:
          ...
            ...
        rescue:
          - command: echo This will run if any Task in the Block fails
    