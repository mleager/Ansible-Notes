#!/usr/bin/env python3

# Basic Inventory using Python ( Using OOP ) [] {} =

import json


class DynamicInventory:
    def __init__(self) -> None:
        self.inventory = {
            'web': {
                'hosts': ['webserver1', 'webserver2'],
                'vars': {
                    'http_port': 80,
                    'max_connections': 100
                }
            },
            'db': {
                'hosts': ['dbserver1'],
                'vars': {
                    'db_port': 3306,
                    'db_name': 'mydb'
                }
            },
            '_meta': {
                'hostvars': {
                    'webserver1': {
                        'ansible_user': 'user1',
                        'ansible_ssh_pass': 'password1'
                    },
                    'webserver2': {
                        'ansible_user': 'user2',
                        'ansible_ssh_pass': 'password2'
                    },
                    'dbserver1': {
                        'ansible_user': 'user3',
                        'ansible_ssh_pass': 'password3'
                    }
                }
            }
        }

    def generate_inventory_file(self, file_path) -> __file__:
        inventory_json = json.dumps(self.inventory, indent=4)

        with open(file_path, 'w') as file:
            file.write(inventory_json)


dynamic_inventory = DynamicInventory()

dynamic_inventory.generate_inventory_file(
    'Advanced/8-Dynamic Inventory/My Scripts/3-oop-inventory.json')
