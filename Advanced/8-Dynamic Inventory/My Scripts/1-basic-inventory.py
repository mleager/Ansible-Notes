#!/usr/bin/env python3

# Basic Inventory using Python ( Not Dynamic ) [] {} =

import json

inventory = {
    '_meta': {
        'hostvars': {
            # Host Variables
            'web': {
                'ansible_host': '172.20.1.100',
                'ansible_user': 'john',
                'ansible_password': 'Passw0rd'
            },
            'db': {
                'ansible_host': '172.20.1.101',
                'ansible_user': 'maria',
                'ansible_password': 'Passw0rd'
            }
        }
    },
    'all': {
        'children': [
            'web_server',
            'db_server'
        ]
    },
    'web_server': {
        'hosts': ['web'],
        # Group Varaibles
        'vars': {
            'http_port': 80,
            'max_connections': 100
        }
    },
    'dbserver': {
        'hosts': ['db'],
        # Group Variables
        'vars': {
            'db_port': 3306,
            'db_name': 'ecomdb'
        }
    }
}

inventory_json = json.dumps(inventory, indent=4)

with open('Advanced/8-Dynamic Inventory/My Scripts/2-basic-inventory.json', 'w') as file:
    file.write(inventory_json)
