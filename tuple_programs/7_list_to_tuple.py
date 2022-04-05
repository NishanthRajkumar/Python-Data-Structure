'''
    @Author: Nishanth
    @Date: 05-04-2022 12:26:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 12:26:00
    @Title: Convert list to tuple
'''
import sys
import logging

def list_to_tuple(list_data: list):
    """
        Description:
            Converts given list to tuple
        
        Parameter:
            list_data: a list
        
        Return:
            None
    """
    logging.info(f"List: {list_data}")
    new_tuple = tuple(list_data)
    logging.info(f"Tuple from list: {new_tuple}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    list_to_tuple(['rgb', 70, 30, 49, 'rgb', 30, 30, 70])