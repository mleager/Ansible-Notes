
##  Ansible Variables  ##     [] {} =



Variables can be defined and used in the:

    - inventory
    - Playbook
    - in its own seperate "variables" file


Variables are written as Key: Value pairs 
    
    - use Jinja2 Templating to insert Variable values


##  Example Playbook with Variables
- 
  name: Add DNS server to resolv.conf
  hosts: localhost
  vars:
    dns_server: 10.1.250.10
  tasks:
    - lineinfile:
        path: '/etc/resolv.conf'
        line: 'nameserver  {{ dns_server }}'


##  Example Variable File & Playbook  ##

# Sample Variable File - web.yaml

---------------------------
http_port: 8081
snmp_port: 161-162
inter_ip_range: 192.0.2.0
---------------------------

# Sample Playbook

-----------------------------------
-
  name: Set Firewall Configurations
  hosts: web
  tasks:
    - firewalld:
        service: https
        permanent: true
        state: enabled
    
    - firewalld:
        port: '{{ http_port }}'/tcp
        permanent: true
        state: disabled

    - firewalld:
        port: '{{ snmp_port }}'/udp
        permanent: true
        state: disabled

    - firewalld:
        source: '{{ inter_ip_range }}'/24
        Zone: internal
        state: enabled
-----------------------------------