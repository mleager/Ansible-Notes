
##  Ansible Config Files  ##     [] {} =


You can copy the default Ansible Config file into your Playbook's directory
in order to set your own defaults and values

    - default Ansible Config stored at: /etc/ansible/ansible.cfg


Where to store Ansible Config file:

    - /etc/ansible/ansible.cfg
    - create/modify ansible.cfg in the directory where your Playbook is
    - set path using an ENV Variable


You can create a Config file as use it for mutliple Playbooks
in other directories by: 

    1. using an ENV Variable before running the Playbook:

        >> ANSIBLE_CONFIG=/opt/ansible-web.cfg ansible-playbook playbook.yml

    2. setting the ENV Variable in the shell to be constantly active

        >> export ANSIBLE_CONFIG=/opt/ansible-web.cfg
        >> ansible-playbook playbook.yml 

    * ANSIBLE_CONFIG=</path/to/config>


Order Ansible uses for choosing which Config file to use:

    1. ENV Variable
    2. ansible.cfg in the current directoy
    3. .ansible.cfg in user's home directory
    4. /etc/ansible/ansible.cfg


You can override a single Config parameter using an ENV Variable.

    - The name of the ENV is the name of the parameter in all caps, 
      prefixed with 'ANSIBLE_'        ( check the Docs if needed )


Ex: Override the "gathering" parameter so that it's off 

    /etc/ansible/ansible.cfg 
    ------------------------
    gathering      = implicit

    >> export ANSIBLE_GATHERING=explicit

    * This ENV Variable now takes precedence over all other Config files,
      so all Playbooks run will now have 'gathering' off



# Viewing Configurations:


    List all different configurations:
    
        >> ansible-config list


    Show the current active Config file:

        >> ansibel-config view 


    Show the current Config settings:

        >> ansible-config dump

    
    Ex:

        >> export ANSIBLE_GATHERING=explicit

        >> ansible-config dump | grep GATHERING
            
            * 'DEFAULT_GATHERING(env:ANSIBLE_GATHERING)=explicit'