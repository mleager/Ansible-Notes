
##  Ansible Modules  ##     [] {} =



Modules are categorized into various groups based on their funcitonality.

Some Module Groups:

    - System
    - Commands
    - Files
    - Database
    - Cloud
    - Windows
    - etc.


For full list of Moudles & actions:

    * docs.ansible.com        


Basic System Module actions:

    - User              - Make
    - Group             - Mount
    - Hostname          - Ping
    - Iptables          - SystemD
    - LVG               - Service
    - Lvol


Basic Commands Module actions:

    - Command           - Script
    - Expect            - Shell
    - Raw


Basic Files Module actions:

    - Acl               - LineInFile
    - Archive           - Replace
    - Copy              - Stat
    - File              - Template
    - Find              - Unarchive


Basic Database Module actions:

    - Mongodb           - Postgresql
    - Mssql             - Proxysql
    - Mysql             - Vertica


Basic Cloud Module actions:

    - Amazon            - Linode
    - Azure             - OpenStack
    - CloudStack        - Rackspace
    - DigitalOcean      - Smartos
    - Docker            - VMware


Basic Window Module actions:

    - win_copy          - win_package
    - win_command       - win_path
    - win_domain        - win_ping
    - win_file          - win_shell
    - win_iis_website   - win_user


##  Module Examples  ##

# Command:

- 
  name: Play 1
  hosts: localhost
  tasks:
    - name: Execute the command 'date'
      command: date

    - name: Change to '/etc/ Dir & display 'resolv.conf' file
      command: cat resolv.conf chdir=/etc

    - name: Create the folder if the folder doesn't exist
      command: mkdir /folder creates=/folder


# Script:

-
  name: Play 2
  hosts: localhost
  tasks:
    - name: Run a script on a remote server
      script: /some/local/script.sh -arg1 -arg2


# Service:

-
  name: Play 3
  hosts: localhost
  tasks:
    - name: Start the database service
      service: 
        name: postgresql
        state: started

    - name: Start the httpd service
      service:
        name: httpd
        state: started

    - name: Start the nginx service
      service:
        name: nginx
        state: started


# Lineinfile:

- 
  name: Add DNS server to resolv.conf
  hosts: localhost
  tasks:
    - lineinfile: 
        path: /etc/resolv.conf
        line: 'nameserver  10.1.250.10'


# Using Multiple Modules:

- name: 'hosts'
  hosts: all
  become: yes
  tasks:
    - name: 'Execute a script'
      script: '/tmp/install_script.sh'

    - name: 'Start httpd service'
      service:
        name: 'httpd'
        state: 'started'

    - name: 'Create or update index.html file.'
      lineinfile:
        path: /var/www/html/index.html
        line: 'Welcome to ansible-beginning course'
        create: true

    - name: 'Create a new user'
      user:
        name: 'web_user'
        uid: 1040
        group: 'developers'