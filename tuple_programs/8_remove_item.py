'''
    @Author: Nishanth
    @Date: 05-04-2022 12:26:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 12:26:00
    @Title: Remove item from tuple
'''
import sys
import logging

def remove_item(tuple_data: tuple, item = None):
    """
        Description:
            Removes item from tuple
        
        Parameter:
            tuple_data: a tuple
            item: item to remove
        
        Return:
            None
    """
    logging.info(f"Original Tuple: {tuple_data}")
    if item == None:
        item = input("Enter item to remove: ")
    try:
        remove_index = tuple_data.index(item)
        tuple_data = tuple_data[:remove_index] + tuple_data[remove_index+1:]
        logging.info(f"Updated tuple: {tuple_data}")
    except ValueError:
        logging.error("Item does not exist in tuple")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    remove_item(['rgb', 70, 30, 49, 'rgb', 30, 30, 70], 49)