# check current inventory and return current after updating given two inventories

def update_inventory(new_inv, curr_inv):
    updated_inventory={}
    for item in new_inv:
        for other_item in curr_inv:
            if item["name"]==other_item["name"]:
                updated_inventory[item['name']] = other_item['quantity']+item['quantity']
            else:
                updated_inventory.update(item)
        
    return updated_inventory

new_inventory = [
    {"name":"Grain of Rice", "quantity": 9000},
    {"name":"Peanut Butter", "quantity": 50},
    {"name":"Royal Jelly", "quantity":20}
]

current_inventory = [
    {"name":"Peanut Butter", "quantity":20},
    {"name":"Grain of Rice", "quantity":1}

]

print(update_inventory(new_inventory, current_inventory))