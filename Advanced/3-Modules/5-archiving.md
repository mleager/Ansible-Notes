
##  Ansible Module: Archiving  ##     [] {} =



1. Create an inventory file ( web1 | 172.20.1.100 | root | Passw0rd )

    # inventory
    web1 ansible_host=172.20.1.100 \
    ansible_user=root \
    ansible_password=Passw0rd



2. Create a Playbook to make a zip archive 'opt.zip' of the '/opt'
   directory on web1 - save at '/root'

    # zip.yml
    ---
    - name: Zip /opt directory to /root
      hosts: web1
      tasks:
        - archive:
            path: /opt
            dest: /root/opt.zip
            format: zip



3. Extracts the contents of the local 'local.zip' to web1's /tmp directory

    # local.yml
    ---
    - name: Extract file to web1
      hosts: web1
      tasks:
        - unarchive:
            src: local.zip
            dest: /tmp



4. Extract the file '/root/data.tar.gz' from web1 to '/srv' then remove
   the 'data.tar.gz' from web1 upon completion

    # data.yml
    ---
    - name: Transfer Archived file from web1 to controller
      hosts: web1
      tasks:
        - unarchive:
            src: /root/data/tar.gz
            dest: /srv
            creates: true
            remote_src: true

        - file:
            path: /root/data.tar.gz
            state: absent



5. Create a Playbook to download and extract a zip archive under '/root':
   - web1: https://github.com/kodekloudhub/Hello-World/archive/master.zip

    # download.yml
    ---
    - name: Download & Install archive on web1
      hosts: web1
      tasks:
        - unarchive:
            src: |
              https://github.com/kodekloudhub/Hello-World/archive/master.zip
            dest: /root/
            remote_src: true

    * NOTE: use 'remote_src' to download to target node 



6. Create a bz2 archive of the following files on web1:
   - /root/file1.txt
   - /usr/local/share/file2.txt
   - /var/log/lastlog
   * Save archive at '/root/files.tar.bz2'

    # files.yml
    ---
    - name: Archive multiple files to /root/files.tar.bz2
      hosts: web1
      tasks:
        - archive:
            path:
              - /root/file1.txt
              - /usr/local/share/file2.txt
              - /var/log/lastlog
            dest: /root/files.tar.bz2
            format: bz2



7. Create a Playbook to do the following tasks:
   - install, start, enable nginx
   - extract '/root/nginx.zip' under '/usr/share/nginx/html'
   - in '/usr/share/nginx/html/index.html' replace the line:
     * "This is a sample html code"  -->  "This is KodeKloud Ansible lab"

    # nginx.yml
    ---
    - name: Install and Configure Nginx
      hosts: web1
      tasks:
        - name: Install nginx
          yum:
            name: nginx
            state: present

        - name: Start & Enable nginx
          service:
            name: nginx
            state: started
            enabled: true

        - name: Extract /root/nginx.zip 
          unarchive:
            src: /root/nginx.zip
            dest: /usr/share/nginx/html
            remote_src: true

        - name: Replace lines inside nginx index.html
          replace:
            path: /usr/share/nginx/html/index.html
            regexp: "This is sample html code"
            replace: "This is KodeKloud Ansible lab"
