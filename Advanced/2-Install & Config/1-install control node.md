
##  Ansible Installing Controller Node  ##     [] {} =


# Ansible Installation Docs:

    https://docs.ansible.com/ansible/latest/installation_guide/


The Controller Node is where all the core Ansible software 
is installed and configured:

    - Config file
    - Inventory
    - Playbooks
    - Modules


    * Ansible can only be installed on Linux, 
      but the Target/Managed Nodes can be Windows.


# Ways to Install Ansible using CLI:

    - via the website
    - Redhat: >> sudo yum install ansible
    - Ubuntu: >> sudo apt install ansible
    - Fedora: >> sudo dnf install ansible
    - Python: >> sudo pip install ansible
    - GIT: install from source


# Installing using PIP on Linux:

    If PIP not installed:

        >> sudo yum install epel-release
        >> sudo yum install python-pip

    Install Ansible:

        >> sudo pip install ansible

    Upgrade Ansible Version:

        >> sudo pip install --upgrade ansible

    Install a Specific Version of Ansible:

        >> sudo pip install ansible==2.4

    ** NOTE:

        When installing with PIP, the default Config and Inventory
        will not be created automatically, and must be done manually


# After Installation:


    Inventory is created in the default location:

        >> /etc/ansible/hosts 

    
    Config File is created in the default location:

        >> /etc/ansible/ansible.cfg 

    
    * both can be modified or created in a local directory 


