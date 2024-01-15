
##  Ansible: Playbook Run Options  ##     [] {} =


# Check Mode ( Dry Run ):

    Outputs the results of running a Playbook without 
    actually executing it or making changes 

    >> ansible-playbook playbook.yml --check


# Start-At-Task:

    Specify the Task that the Playbook should start at,
    and skip any Tasks above the specified Task

    * runs all Tasks at and after the specified Task

    ---
    - name: Install httpd
      hosts: all
      tasks:
        - name: Install httpd
          yum:
            name: httpd
            state: installed
        - name: Start httpd service
          service:
            name: httpd
            state: started

    >> ansible-playbook playbook.yml --start-at-task "Start httpd service"


# Tags:

    Add Tags to Plays or Tasks and specify to run or skip it

    * Runs or skips only the tag specified

    ---
    - name: Install httpd
      tags: install and start
      hosts: all
      tasks:
        - yum:
            name: httpd
            state: installed
          tags: install
        - service:
            name: httpd
            state: started
          tags: start httpd service

    >> ansible-playbook playbook.yml --tags "install"
    >> ansible-playbook playbook.yml --skip-tags "start httpd service"