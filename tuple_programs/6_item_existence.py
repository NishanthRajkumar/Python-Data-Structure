'''
    @Author: Nishanth
    @Date: 05-04-2022 11:43:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 11:43:00
    @Title: Check if item exists in tuple
'''
import sys
import logging

def chk_item_exist(tuple_data: tuple, item = None):
    """
        Description:
            Checks if item exists in tuple
        
        Parameter:
            tuple_data: A tuple
            item: item to search for in tuple
        
        Return:
            None
    """
    logging.info(f"Original tuple: {tuple_data}")
    if item == None:
        item = input("Enter item to search: ")
    if item in tuple_data:
        logging.info(f"{item} is present in tuple")
    else:
        logging.info(f"{item} is not present in tuple")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    chk_item_exist(('rgb', 70, 30, 49, 'rgb', 30, 30, 70), 49)