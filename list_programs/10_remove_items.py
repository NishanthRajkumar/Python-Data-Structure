'''
    @Author: Nishanth
    @Date: 05-04-2022 10:35:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 10:35:00
    @Title: Remove 0th, 4th and 5th elements from list
'''
import sys
import logging

def remove_items(list_data: list):
    """
        Description:
            Remove 0th, 4th and 5th elements from list
        
        Parameter:
            list_data: list of data
        
        Return:
            None
    """
    logging.info(f"List: {list_data}")
    if type(list_data) is not list and len(list_data) < 5:
        logging.error("Must be of type list with min of 5 items in list")
        return None
    list_data.pop(0)
    list_data.pop(3)
    list_data.pop(3)
    logging.info(f"Updated list: {list_data}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    remove_items(sample_list)