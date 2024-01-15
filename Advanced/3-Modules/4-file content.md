
##  Ansible Module: File Content  ##     [] {} =



1. Create a blank file '/opt/data/perm.txt' with 0640 permissions on web1

    # perm.txt
    ---
    - hosts: web1
      tasks:
        - name: Create a file
          file:
            path: /opt/data/perm.txt
            state: touch
            mode: 0640



2. Add 'This line was added using Ansible lineinfile module!' 
   to /var/www/html/index.html file on web1 

    # index1.yml
    ---
    - hosts: web1
      tasks:
        - name: Add line to /var/www/html/index.html
          lineinfile:
            path: /var/www/html/index.html
            line: 'This line was addded using Ansible lineinfile module!'
            create: true        * ( create file if it doesn't exist )



3. Create a Playbook that finds file in 'opt/data' that are:
   - older than 2 minutes && >= 1MB. 
   It should then copy those files to the '/opt' directory.

    # find.yml
    ---
    - hosts: web1
      tasks:
        - name: Find files
          find:
            paths: /opt/data
            recurse: true
            age: 2m
            size: 1m
          register: file 

        - name: Copy files
          command: "cp {{ item.path }} /opt"
          with_items: "{{ file.files }}"



4. Add additional content to the beginning of '/var/www/html/index.html':
   - "Welcome to KodeKloud!\n This is Ansible Lab."
   - owner & group: apache 

    # index2.html
    ---
    - hosts: web1
      tasks:
        - name: Add content block
          blockinfile:
            path: /var/www/html/index.html
            insertbefore: 'BOF'
            block: |
              Welcome to KodeKloud!
              This is Ansible Lab.
            owner: apache
            group: apache



5. Create a Playbook to change Port 80 to 8080 in:
   - '/etc/httpd/conf/httpd.conf'
   - Restart httpd service after making the change

    # httpd.yml
    ---
    - hosts: web1
      tasks:
        - name: Update httpd to port 8080
          replace:
            path: /etc/httpd/conf/httpd.conf
            regexp: "Listen 80"
            replace: "Listen 8080"

        - name: Restart httpd service
          service:
            name: httpd
            state: restarted
