'''
    @Author: Nishanth
    @Date: 04-04-2022 18:13:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 18:13:00
    @Title: Get smallest item in list
'''
import sys
import logging

def min_of_list(list_of_items: list):
    """
        Description:
            Finds the smallest item in list
        
        Parameter:
            list_of_items: a list. The list items must be of numeric(int or float) type
        
        Return:
            None
    """
    try:
        smallest = min(list_of_items)
        logging.info(f"Smallest in {list_of_items} is {smallest}")
    except TypeError:
        logging.exception("Various types of items in list")
        logging.error("The list must be a homogenous numeric(int or float) list")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    min_of_list([23, 46, 35, 8, 25])
    min_of_list([23, 4.6, 3.5, 2.5])