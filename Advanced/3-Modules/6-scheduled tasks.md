
##  Ansible Module: Scheduled Tasks  ##     [] {} =



1. Create a Playbook to add a cronjob 'Clear Lastlog' to empty 
   '/var/log/lastlog' everyday at 12am on node00

    # lastlog.yml
    ---
    - name: Run cronjob for lastlog
      hosts: node00
      tasks:
        - cron:
            name: "Clear Lastlog"
            hour: "0"
            minute: "0"
            job: "echo '' > /var/log/lastlog"



2. Create a Playbook to create the cronjob 'Free Memory Check' that
   executes the script at '/root/free.sh' on node00 every 2 hours

    # script_cron.yml
    ---
    - name: Execute Free Memory Script every 2 hours
      hosts: node00
      tasks:
        - cron:
            name: "Free Memory Check"
            hour: "*/2"
            minute: "0"
            job: "sh /root/free.sh"



3. Create a Playbook to remove the old cronjob 'Check Memory' on node00

    # remove_cron.yml
    ---
    - name: Remove cronjob 'Check Memory'
      hosts: node00
      tasks:
        - cron:
            name: "Check Memory"
            state: absent



4. Create a Playbook to execute the cronjob 'cleanup' that will remove
   all folders & files in node00's '/tmp' after a reboot

    # reboot.yml
    ---
    - name: Cleanup /tmp after reboot
      hosts: node00
      tasks:
        - cron:
            name: "cleanup"
            special_time: reboot
            job: "rm -rf /tmp/*"



5. Create the cronjob 'yum update' to do the following:
   - run 'yum update' every sunday at 8:05am
   - cron should be added for 'root' user
   - do not add to crontab, instead use '/etc/cron.d/ansible_yum

    # yum_update.yml
    ---
    - name: Run 'yum update' every sunday morning
      hosts: node00
      tasks:
        - cron:
            name: "yum update"
            weekday: "0"
            hour: "8"
            minute: "5"
            user: root
            job: "yum update -y"
            cron_file: ansible_yum
