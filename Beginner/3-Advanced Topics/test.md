
##  Ansible Final Lab  ##     [] {} =


1. Install Ansible on the student-node

    >> sudo yum install ansible -y


2. Create an Ansible config file under /home/bob/playbooks
   and disable the SSH Host Key Checking for Ansible

    >> vi ansible.cfg

    [defaults]
    host_key_checking = False


3. Create an Ansible inventory file for Host "node01"

    >> vi inventory

    node01 ansible_host=node01 ansible_ssh_pass=caleston123


4. Add an alias for "node02" to the inventory file

    >> vi inventory

    node01 ansible_host=node01 ansible_ssh_pass=caleston123
    node02 ansible_host=node02 ansible_ssh_pass=caleston123


5. Test the connection for both "node01" and "node02" 

    >> ansible -i inventory node01 -m ping
    >> ansible -i inventory node02 -m ping


6. Create a group called "web_nodes" with both "node01" & "node02"

    >> vi inventory 

    ...
    [web_nodes]
    node01
    node02


7. Create a new inventory file at "inventory_table" with the provided data

    >> vi inventory_table

    # Web Nodes
    web_node1 ansible_host=web01.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
    web_node2 ansible_host=web02.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
    web_node3 ansible_host=web03.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass

    # DB Nodes
    sql_db1 ansible_host=sql01.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass
    sql_db2 ansible_host=sql02.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass

    # Groups
    [web_nodes]
    web_node1
    web_node2
    web_node3

    [db_nodes]
    sql_db1
    sql_db2

    [boston_nodes]
    sql_db1
    web_node1

    [dallas_nodes]
    sql_db2
    web_node2
    web_node3

    [us_nodes:children]
    boston_nodes
    dallas_nodes


8. Create a Playbook "command.yml" to execute the command to display
   the contents of file "/etc/resolv.conf" on loclahost

    >> vi command.yml

    ---
    - hosts: localhost
      connection: local
      tasks:
        - name: Display resolv.conf file
          command: 'cat /etc/resolv.conf'

    >> ansible-playbook -i localhost command.yml -vv


9. Create a Playbook "perm.yml" to:
    - create "blog.txt" under /opt/news on "node01" - group owner: sam
    - create "story.txt" under /opt/news on "node02" - user owner: sam

    >> vi perm.yml

    ---
    - hosts: node01
      become: true
      tasks:
        - name: Create /opt/news/blog.txt
          file:
            path: /opt/news/blog.txt
            state: touch
            group: sam

    - hosts: node02
      become: true
      tasks:
        - name: Create /opt/news/story.txt
          file:
            path: /opt/news/story.txt
            state: touch
            owner: sam

    >> ansible-playbook -i inventory perm.yml -vv


10. Create a Playbook "file.yml" to create a a file at "/opt/file.txt"
    on "node01". The file contents: "This file is created by Ansible"

    >> vi file.yaml

    Option 1
    ---
    - hosts: node01
      become: true
      tasks:
        - name: Create /opt/file.txt
          shell: 'echo "This file is created by Ansible!" >> /opt/file.txt'

    Option 2
    ---
    - hosts: node01
      become: true
      tasks:
        - name: create a file
          copy:
            dest: /opt/file.txt
            content: "This file is created by Ansible!"

    >> ansible-playbook -i inventory file.yml -vv
    >> ssh node01
    >> cat /opt/file.txt


11. Create a Playbook "copy.yml" to copy "/usr/src/blog.index.html"
    to both Nodes at "/opt/blog"

    >> vi copy.yml

    ---
    - hosts: web_nodes
      tasks:
        - name: Copy /usr/src/blog/index.html 
          copy:
            src: /usr/src/blog.index.html
            dest: /opt/blog
            remote_src: true

    >> ansible-playbook -i inventory copy.yml -vv
    >> ssh node01  ( and node02 )
    >> cat /opt/blog/index.html 


12. Create a Playbook "replace.yml" to:
    - node01: replace string 'Kodekloud' to 'Ansible' at /opt/music/blog
    - node02: replace string 'Ansible' to 'Kodekloud' at /opt/music/story

    >> vi replace.yml

    ---
    - hosts: node01
      become: true
      tasks:
        - replace:
            path: /opt/music/blog.txt
            regexp: 'Kodekloud'
            replace: 'Ansible'

    - hosts: node02
      become: true
      tasks:
        - replace:
            path: /opt/music/story.txt
            regexp: 'Ansible'
            replace: 'Kodekloud'

    >> ansible-playbook -i inventory replace.yml -vv


13. Modify the Playbook "banana.yml" to use a conditional to print
    "I am a Banana" if fruit == 'banana'

    >> vi banana.yml

    ---
    - name: 'Am I a Banana or not?'
      hosts: localhost
      connection: local
      vars:
        fruit: banana
      tasks:
        - command: 'echo "I am a Banana"'
          when: fruit == 'banana'
        - command: 'echo "I am not a Banana"'
          when: fruit != 'banana'

    >> ansible-playbook -i localhost banana.yml -vv


14. Add a loop directive to the Playbook "fruits.yml" to print
    all fruits defined under the 'fruits' variable

    >> vi fruits.yml

    ---
    - name: 'Print fruits'
      hosts: localhost
      connection: local
      vars:
        fruits:
          - Apple
          - Banana
          - Grapes
          - Orange
      tasks:
        - command: 'echo "{{ item }}"'
          with_items: '{{ fruits }}'

    >> ansible-playbook -i localhost fruits.yml -vv


15. Create the Playbook "package.yml" to install "vim-enhanced" locally

    >> vi package.yml

    ---
    - name: 'Install "vim" package'
      hosts: localhost
      become: true
      connection: local
      tasks:
        - yum:
            name: vim-enhanced
            state: present

    >> ansible-playbook -i localhost package.yml -vv


16. Modify the Playbook "copy_file.yml" from 'student-node' to:
    - node01: copy '/usr/src/condition/blog.txt' to '/opt/condition'
        user & group: bob  |  permissions: 0640
    - node02: copy '/usr/src/condition/story.txt' to '/opt/condition'
        user & group: sam  |  permissions: 0400

    >> vi copy_file.yml

    Option 1
    ---
    - hosts: node01
      become: true
      tasks:
        - name: Copy /usr/src/condition/blog.txt 
          copy:
            src: /usr/src/condition/blog.txt
            dest: /opt/condition/blog.txt
            owner: bob
            group: bob
            mode: "0640"

    - hosts: node02
      become: true
      tasks:
        - name: Copy /usr/src/condition/story.txt
          copy:
            src: /usr/src/condition/story.txt
            dest: /opt/condition/story.txt
            owner: sam
            group: sam
            mode: "0400"

    Option 2
    ---
    - hosts: all
      become: true
      tasks:
        - name: Copy file with owner and permissions on node01
          copy:
            src: /usr/src/condition/blog.txt
            dest: /opt/condition/blog.txt
            owner: bob
            group: bob
            mode: "0640"
          when: inventory_hostname == "node01"

        - name: Copy file with owner and permissions on node02
          copy:
            src: /usr/src/condition/story.txt
            dest: /opt/condition/story.txt
            owner: sam
            group: sam
            mode: "0400"
          when: inventory_hostname == "node02"

    >> ansible-playbook -i inventory copy_file.yml -vv


17. Create a Playbook "lineinfile.yml" to:
    - node01: add "Welcome to KodeKloud Labs!" to the top of
        /var/www/html/index.html without deleting existing content

    >> vi lineinfile.yml

    ---
    - hosts: node01
      become: true
      tasks:
        - lineinfile:
            path: /var/www/html/index.html
            line: 'Welcome to KodeKloud Labs!'
            state: present
            insertbefore: 'BOF'
            
    >> ansible-playbook -i inventory lineinfile.yml -vv
    >> ssh node01
    >> cat /var/www/html/index.html


18. Create a Playbook "service.yml" on both nodes to:
    - install 'vsftpd'
    - start the 'vsftpd' service

    >> vi service.yml

    ---
    - hosts: all
      become: true
      tasks:
        - name: 'Install "vsftpd" on node01 and node02'
          yum:
            name: vsftpd
            state: present

        - name: 'Start "vsftpd" on node01 and node02'
          service:
            name: vsftpf
            state: started  
          
    >> ansible-playbook -i inventory service.yml -vv
    >> ssh node01  ( and node02 )
    >> systemctl status vsftpd


19. Create a Playbook "archive.yml" on both nodes to:
    - create an archive of '/usr/src/ecommerce'
    - archive name must be 'demo.tar.gz'
    - save it to '/opt./ecommerce' on both nodes

    >> vi archive.yml

    ---
    - hosts: all
      become: true
      tasks:
        - name: 'Archive /usr/src/ecommerce'
          archive:
            path: /usr/src/ecommerce/
            dest: /opt/ecommerce/demo.tar.gz
            
    >> ansible-playbook -i inventory archive.yml -vv
    >> ssh node01
    >> ls /opt/ecommerce


20. Using Ansible Galaxy, install the Role 'geerlingguy.nodejs'
    under the '/home/bob/playbooks/roles' directory

    * galaxy.ansible.com  -->  search "node.js" / find the link

    >> ansible-galaxy install geerlingguy.nodejs -p /$PWD/roles

    >> ls roles


21. Create an Ansible Role "package" under /playbooks/roles on student-node.
    - It should install 'nginx' and start the service
    - node01: Create a Playbook "role.yml" to use the 'package' Role

    >> cd roles
    >> ansible-galaxy init package
    >> ls package
    >> vi package/tasks/main..yml

    ---
    - name: Install Nginx
      ansible.builtin.package:
        name: nginx
        state: latest

    - name: Start Nginx service
      ansible.builtin.service:
        name: nginx
        state: started

    >> cd ..
    >> vi /playbooks/roles.yml

    ---
    - hosts: node01
      become: true
      roles:
         - roles/package

    >> ansible-playbook -i inventory role.yml
    >> ssh node01
    >> systemctl status nginx