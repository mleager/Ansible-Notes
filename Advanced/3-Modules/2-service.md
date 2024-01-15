
##  Ansible Module: Service  ##     [] {} =



1. Create Playbook to make sure HTTPD service is started on web1

    # httpd.yml
    ---
    - hosts: web1
      tasks:
        - name: Start HTTPD Service
          service:
            name: httpd
            state: started



2. Modify the the Playbook so that the HTTPD server reloads after copying

    # file.yml
    ---
    - hosts: all
      gather_facts: false
      tasks:
        - name: Copy Apache welcome file
          copy:
            src: index.html
            dest: /var/www/html/index.html
        
        - name: Reload HTTPD
          service:
            name: httpd
            state: reloaded



3. Update the HTTPD Playbook to always start automatically after a reboot

    # httpd.yml
    ---
    - hosts: web1
      tasks: 
        - name: Start HTTPD Service
          service:
            name: httpd
            state: started
            enabled: true



4. Modify the Playbook to enabled Port 443 for HTTPD. Restart after

    # config.yml
    ---
    - hosts: web1
      tasks:
        - name: Enable HTTPD on Port 443
          replace:
            path: /etc/httpd/conf/httpd.conf
            regexp: "^Listen 80"
            replace: "Listen 443"

        - name: Restart HTTPD
          service:
            name: httpd
            state: restarted



5. Create a Playbook to install Nginx and Start & Enable the service

    # nginx.yml
    ---
    - hosts: web1
      tasks:
        - name: install nginx
          yum:
            name: nginx
            state: present

        - name: restart & enable nginx
          service:
            name: nginx
            state: started
            enabled: true
