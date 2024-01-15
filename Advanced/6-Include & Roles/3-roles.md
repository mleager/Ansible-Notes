
##  Ansible Roles  ##     [] {} =


Roles allow you to package a Play or Playbook to be re-used later

    - organize code and to share with others


Anisble Galaxy is a website to find thousands of Roles available.


Best Practices for Roles is to organize your code seperately.
Each piece is grouped together:

    - Tasks
    - Variables
    - Defaults
    - Handlers
    - Templates ( Playbooks )


##  Create Your Own Role using Ansible Galaxy  ##


Ansible Galaxy has a tool that can create a skeleton directory:

    >> ansible-galaxy init mysql

        - mysql
          -> README.md
          -> templates
          -> tasks
          -> handlers
          -> vars
          -> defaults
          -> meta


There are 2 common places to store this set of Directories:

    1. In your local Playbook directory

        - my-playbook
          -> playbook.yml
          -> roles
            --> templataes
            --> tasks
            --> ...

    2. In a common directory used for storing Roles

        - /etc/ansible/roles

        * This is configurable and can be changed to any path/dir

            - /etc/ansible/ansible.cfg
                roles_path = /etc/ansible/roles

        ** default search location if Ansible can't find 
           the Role in the current directory


You can share your Role by uploading to GitHub to a specifc Repo


##  Using a Role from Ansible Playbook  ##


- CLI -

To search for a Role using:

    >> ansible-galaxy search mysql


To Install a Role in '/etc/ansible/roles':

    >> ansible-galaxy install geerlingguy.mysql


To Install a Role in your Local Playbook Directory:

    >> ansible-galaxy install geerlingguy.mysql -p ./roles


View a List of Currently Installed Roles:

    >> ansible-galaxy list


To View Where Roles Will be Installed:

    >> ansible-config dump | grep ROLE