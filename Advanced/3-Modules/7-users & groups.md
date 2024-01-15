
##  Ansible Module: Users & Groups  ##     [] {} =



1. Create a Playbook that creates:
   - user: 'admin'
   - group: 'admin'
   - uid: 2048

    # create_user.yml
    ---
    - name: Create Admin User
      hosts: all
      tasks:
        - group:
          name: admin
          state: present

        - user:
            name: admin
            group: admin
            uid: 2048



2. Create a Playbook to create a user account for Sabin Nepal
   - user name: neymarsabin
   - expiry data (in epoch): 1704067199

    # add_user.yml
    ---
    - name: Create User for Sabin Nepal
      hosts: all
      tasks:
        - user:
            name: neymarsabin
            expires: 1704067199



3. Remove the 'admin' user and group that was created in #1.

    # remove_user.yml
    ---
    - name: remove admin user
      hosts: all
      tasks:
        - user:
            name: admin
            state: absent 
        
        - group:
            name: admin
            state: absent