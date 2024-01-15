
##  Ansible Module: Firewalld ##     [] {} =



1. Install 'firewalld' on the Node 'web1'. Start and enable the service.

  # firewall.yml
  ---
  - hosts: web1
    gather_facts: false
    tasks:
      - name: Install Firewalld
        yum:
          name: firewalld
          state: present
      
      - name: Start & Enable Firewalld Service
        service:
          name: firewalld
          state: started
          enabled: true

  ---
  - hosts: web1
    tasks:
      - yum: name=firewalld state=present
      - service: name=firewalld state=started enabled=true



2. Create a Firewall Rule to whitelist ( allow ) web2's IP ( 172.20.1.101 )

  # whitelist.yml
  ---
  - hosts: web1
    gather_facts: false
    tasks:
      - name: Block web2's IP Address
        firewalld:
          source: 172.20.1.101
          state: enabled
          zone: internal
          permanent: true
          immediate: true

  # Check if 161 is blocked on web1

  >> ssh root@web1
  >> firewall-cmd --list-ports --zone=block



3. Block port 161/udp on web1 permanently

  # block.yml
  ---
  - hosts: web1
    tasks:
      - name: Block Port 161/udp
        firewalld:
          port: 161/udp
          zone: block
          state: enabled
          permanent: true
          immediate: true

  * NOTE: I thought it would be 'state: disabled' but
          using the 'block' zone rejects incoming connections



4. Add Firewall rule to enabled https from Controller machine (172.20.1.2).
   Rule should persist after reboot

  # https.yml
  ---
  - hosts: web1
    tasks:
      - name: Allow HTTPS traffic
        firewalld:
          source: 172.20.1.2
          service: https
          state: enabled
          zone: internal
          permanent: true
          immediate: true
      
      - name: Restart Firewalld service
        service:
          name: firewalld
          state: reloaded

  # Check if HTTPS from controller in enabled on web1

  >> ssh root@web1
  >> firewall-cmd --list-all --zone=internal



5. Install HTTPD, start and enabled the service. 
   Install Firewalld, start and enabled the service.
   Change HTTPD's port from 80 to 8082.
   Allow incoming traffic on port 8082 

  # web2-config.yml
  ---
  - hosts: web2
    tasks:
      - name: Install HTTPD & Firewalld
        yum:
          name: httpd, firewalld
          state: present
      
      - name: Start & Enable HTTPD & FirewallD
        service:
          name: "{{ item }}"
          state: started
          enabled: true
        with_items:
          - httpd
          - firewalld

      - name: Change HTTPD Port
        replace:
          path: /etc/httpd/conf/httpd.conf
          regexp: "Listen 80"
          replace: "Listen 8082"

      - name: Restart HTTPD 
        service:
          name: httpd
          state: restarted

      - name: Add Firewall Rule to Allow Traffic on HTTPD's Port 8082
        firewalld:
          port: 8082/tcp
          state: enabled
          permanent: true
          immediate: true 

  # Check if Firewall Rule Active
  >> ssh root@web2
  >> firewall-cmd --list-all --zone=public