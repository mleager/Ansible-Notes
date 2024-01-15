
##  Ansible Vault  ##     [] {} =


Docs:

    https://docs.ansible.com/ansible/latest/vault_guide/index.html


Ansible Vault allows you to store encrypted variables 
rather than writing them in plain text.

    - such as 'ansible_host' & 'ansible_password'


##  Encrypt the existing inventory file  ##

inventory
---------
web1 ansible_host=172.20.1.100 ansible_ssh_pass=Passw0rd
web2 ansible_host=172.20.1.101 ansible_ssh_pass=Passw0rd

>> ansible-vault encrypt inventory 

* You will be required to enter a Vault Password

    - you will not be able to view the contents of the encrypted
      file without the Vault password


##  View the Encrypted inventory file  ##

>> ansible-vault view inventory 


##  Create a new Encrypted file  ##

>> ansible-vault create inventory 


##  Run a Playbook Using the Encrypted inventory  ##

The Play will not run if the inventory or any other file is encrypted.

# Option 1:
    
    Use the CLI variable to enter the Vault password for decryption:

    --ask-vault-pass


>> ansible-playbook -i inventory playbook.yml --ask-vault-pass


# Option 2:

    Store the Vault password in a file, specify it in the CLI:

    --vault-password-file = < /path/to/password >


>> ansible-playbook -i inventory playbook.yml \
   --vault-password-file ./vault_pass.txt


# Option 3:

    Use a Python script to retrieve the Vault password 
    ( Ex: storing password in S3 and retrieving via API call )

    -vault-password-file = </path/to/python/script.py >


>> ansible-playbook -i inventory playbook.yml \
   --vault-password-file ./vault_pass.py
