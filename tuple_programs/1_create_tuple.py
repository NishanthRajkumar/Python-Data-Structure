'''
    @Author: Nishanth
    @Date: 05-04-2022 11:43:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 11:43:00
    @Title: Create a tuple
'''
import sys
import logging

def create_tuple(*data):
    """
        Description:
            Creates a tuple
        
        Parameter:
            *data: variable no of data to put in one tuple
        
        Return:
            None
    """
    new_tuple = (data)
    logging.info(f"Type: {type(new_tuple)}; Tuple created: {new_tuple}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    create_tuple('Red', 'Green', 'White', 234, 3+8j, 'Black', 'Pink', 'Yellow')