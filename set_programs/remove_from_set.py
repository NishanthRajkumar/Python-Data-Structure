'''
    @Author: Nishanth
    @Date: 03-04-2022 22:06:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 22:06:00
    @Title: Remove an item from a set
'''
import sys
import logging

def remove(set_data: set, *items) -> set:
    """
        Description:
            Removes the given item(s) from the set
        
        Parameter:
            set_data: The set to remove the item from
            items: the item(s) to be removed
        
        Return:
            returns a set
    """
    set_of_items = set(items)
    return set_data.difference(set_of_items)

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    original_set = set(['asd', 'qwe', 123, 'rty'])
    logging.info(f"Original set: {original_set}")
    updated_set = remove(original_set, 123, 'asd')
    logging.info(f"Updated set: {updated_set}")