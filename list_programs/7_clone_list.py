'''
    @Author: Nishanth
    @Date: 04-04-2022 19:42:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 19:42:00
    @Title: Clone a list
'''
from copy import deepcopy
import sys
import logging

def clone_list(list_of_items: list):
    """
        Description:
            clones a list and prints it
        
        Parameter:
            list_of_items: a list of any type of items
        
        Return:
            None
    """
    cloned_list = deepcopy(list_of_items)
    logging.info(f"Original List: {list_of_items}")
    logging.info(f"Cloned List: {cloned_list}")
    item = input("Enter string to append to cloned list: ")
    cloned_list.append(item)
    logging.info(f"Original List: {list_of_items}")
    logging.info(f"Cloned List: {cloned_list}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    clone_list([1,5,8,3,5,2,1,8])