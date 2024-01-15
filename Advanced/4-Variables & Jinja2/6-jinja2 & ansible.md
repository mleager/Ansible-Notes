
##  Ansible & Jinja2  ##     [] {} =



# File Related Jinja2 Filters

    To get the filename from a full path:

        {{ "/etc/hosts" | basename }}

            * returns hosts from the '/etc/hosts' file

        {{ "c:\windows\hosts" | win_basename }}
    
        {{ "c:\windows\hosts" | win_splitdrive }} -> ["c:", "\windows\host"]

        {{ "c:\windows\hosts" | win_splitdrive | first }} -> "c:"

