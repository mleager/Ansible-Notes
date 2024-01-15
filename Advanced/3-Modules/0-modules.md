
##  Ansible Modules  ##     [] {} =



This chapter includes a mix of 'Builtin' and 'Community.General' Modules

    * view Docs for all available parameters and options



# Package Manager:

    - yum
    - apt 
    - package (detects host's OS and applies correct manager )
                * (can have issues if using different versions 
                    on different hosts )


---
- name: Install web on CentOS
  hosts: all
  tasks:
    - yum:                  ( or apt or package )
        name: httpd
        state: installed    ( or present )



# Service:

    Used to start, stop, restart, and enable a service


---
- name: Start and enable httpd service
  hosts: all
  tasks:
    - service:
        name: httpd
        state: present
        enabled: true



# Firewalld (Firewall Rules):

    Configure firewall rules:

        - allow/block traffic
        - ports
        - protocols
        - specific servers / IP addresses 


---
- name: Add Firewalld rule
  hosts: all
  tasks:
    - firewalld:
        port: 8080/tcp
        service: http
        source: 192.0.0.0/24
        zone: public
        state: enabled
        permanent: true     ( persist rule across reboots )
        immediate: true     ( apply rule immediately )

    * NOTE: when specifying 'permanent' must define 'immediate'
            if you want the rule to apply immediately



# LVG & LVol ( Storage )

    Create and configure LVM volume groups ( Logical Volume Manager )


---
- hosts: all
  tasks:
    - name: Create LVM Volume Group
      lvg:
        vg: vg1
        pvs: /dev/sdb1,/dev/sdb2
    
    - name: Create LVM Volume
      lvol:
        vg: vg1
        lv: lvol1
        size: 2g



# Filesystem & Mount

    Create Filesystems on hosts/devices

    Mount the configured Filesystem 


---
- hosts: all
  tasks:
    - name: Create Filesystem
      filesystem:
        fstype: ext4
        dev: /dev/vg1/lvol1
        opts: -cc

    - name: Mount Filesystem
      mount:
        fstype: ext4
        src: /dev/vg1/lvol1
        path: /opt/app
        state: mounted



# File 

    Create files, directories, or links


---
- hosts: all
  tasks:
    - name: Create Directory
      file:
        path: /opt/app/web
        state: directory

    - name: Create File
      file:
        path: /opt/app/web/index.html
        state: touch
        owner: app-owner 
        group: app-owner
        mode: 0644



# Archive & Unarchive

    Compress files or directoires


---
- hosts: all
  tasks:
    - name: Compress a folder
      archive:
        path: /opt/app/web
        dest: /tmp/web.gz
        format: gz      ( zip, tar, bz2, xz )

    - name: Uncompress a folder
      unarchive:
        src: /tmp/web.gz
        dest: /opt/app/web
        remote_src: true    ( if the archived folder is on the Target )



# Cron

    Configure CronJobs or schedule tasks


---
- hosts: all
  tasks:
    - name: Create a scheduled task
      cron:
        name: Run daily heath report 
        job: sh /opt/scripts/health.sh
        month: *
        day: *
        hour: 8
        minute: 10 



# Users & Groups

    User: manage users on managed nodes
    Groups: manage groups on managed nodes


---
- hosts: all
  tasks:
    - name: Create the group developers
      group:
        name: developers
    
    - name: Create the user maria
      user:
        name: maria
        uid: 1001
        group: developers
        shell: /bin/bash



# Authorized Keys

    Configure managed nodes with the Public Key of User Accounts


---
- hosts: 
  tasks:
    - name: Configure SSH Keys
      authorized_keys:
        user: maria
        state: present
        key: |
          ssh-rsa ASHH*&yahsd87hawdqweas...maria@97asdh7