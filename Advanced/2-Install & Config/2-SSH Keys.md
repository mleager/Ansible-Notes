
##  Ansible Create & Distribute SSH Keys to Target/Managed Nodes  ## [] {} =


# Using SSH Keys on Linux

    
    1. Generate an SSH Key:

        >> ssh-keygen -t rsa 
            ( id_rsa & id_rsa.pub )

        * To generate a specific named file for the Keys:

            >> ssh-keygen -t rsa -f ~/.ssh/ansible-keys
                ( ansible_keys & ansible_keys.pub )

    
    2. Copy the Public Key to the Remote system:

        a. enable password-based authentication on the Remote
        
        b. ssh into the Remote system using a password

        c. scp or copy to the Remote system

        d. disbale password-based authentication on the Remote
    
    
    3. Place the Public Key (id_rsa.pub) on the Remote system at: 
        
        - ~/.ssh/authorized_keys

    
    4. SSH into the Remote system using your Private Key:

        >> ssh -i id_rsa user1@server1



# Using SSH Keys with Ansible


    1. Create SSH Keys on the Control Node 


    2. Transfer Public Key to the Remote 

        >> ssh-copy-id -i /path/to/id_rsa user1@server1



# Config Inventory File to use SSH Keys


/etc/ansible/ansible.cfg
------------------------
web1 ansible_host=172.20.1.100 ansible_user=user1 ansible_ssh_private_key_file=/some-path/private-key 

web2 ansible_host=172.20.1.101 ansible_user=user1
ansible_ssh_private_key_file=/some-path/private-key


    NOTE:

        1. Ansible always assumes 'user' is root.

          If the SSH Key was generated with a specific user,
          that user needs to be specified in the Inventory to connect


        2. If the SSH Keys are in the default location ( user's home dir )
           then Ansible will automatically pibk it up

           If its in another location, it needs to be specified using:

            ' ansible_ssh_private_key_file= '