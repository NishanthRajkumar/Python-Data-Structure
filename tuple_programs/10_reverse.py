'''
    @Author: Nishanth
    @Date: 05-04-2022 12:26:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 12:26:00
    @Title: Reverse a tuple
'''
import sys
import logging

def reverse(tuple_data: tuple):
    """
        Description:
            Reverses a tuple
        
        Parameter:
            tuple_data: a tuple
        
        Return:
            None
    """
    logging.info(f"Original Tuple: {tuple_data}")
    reversed_list = []
    for item in tuple_data:
        reversed_list.insert(0, item)
    reversed_tuple = tuple(reversed_list)
    logging.info(f"Reversed Tuple: {reversed_tuple}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    reverse(('rgb', 70, 30, 49, 'rgb', 30, 30, 70))