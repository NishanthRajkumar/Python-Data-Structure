'''
    @Author: Nishanth
    @Date: 03-04-2022 22:06:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 22:06:00
    @Title: add item to a set
'''
import sys
import logging

def add(set_data: set, item) -> set:
    """
        Description:
            adds given item to the given set
        
        Parameter:
            set_data: The set to add the item to
            item: the item to be added
        
        Return:
            returns a set
    """
    set_data.add(item)
    return set_data

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    updated_set = add(set(['asd', 'qwe']), 123)
    logging.info(f"Updated set: {updated_set}")