'''
    @Author: Nishanth
    @Date: 05-04-2022 11:43:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 11:43:00
    @Title: Clone a tuple
'''
import sys
import logging
from copy import deepcopy

def clone_tuple(tuple_data: tuple):
    """
        Description:
            Clones a tuple
        
        Parameter:
            tuple_data: A tuple
        
        Return:
            None
    """
    tuple_clone = deepcopy(tuple_data)
    logging.info(f"Original tuple: {tuple_data}")
    logging.info(f"Cloned tuple: {tuple_clone}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    clone_tuple(('rgb', 70, 30, 49))