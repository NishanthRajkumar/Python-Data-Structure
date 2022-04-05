'''
    @Author: Nishanth
    @Date: 04-04-2022 19:33:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 19:33:00
    @Title: Remove duplicates from list
'''
import sys
import logging

def remove_duplicates(list_of_items: list):
    """
        Description:
            Removes duplicates from list
        
        Parameter:
            list_of_items: a list of any type of items
        
        Return:
            None
    """
    updated_list = list(set(list_of_items))
    logging.info(f"Original List: {list_of_items}")
    logging.info(f"Updated List: {updated_list}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    remove_duplicates([1,5,8,3,5,2,1,8])