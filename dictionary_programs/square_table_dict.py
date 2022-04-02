'''
    @Author: Nishanth
    @Date: 02-04-2022 10:53:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 10:53:00
    @Title: Generate square table dictionary for given n value
'''
import logging
import sys

def square_dict(nth_key_value: int):
    """
        Description:
            Generates square table dictionary for given n value
        
        Parameter:
            nth_key_value: generates square table upto this no
        
        Return:
            None
    """
    if type(nth_key_value) is not int:
        logging.error("The nth key value must be int")
        return None
    if nth_key_value < 1:
        logging.error("The nth key value must not be less than 1")
        return None
    square_table_dict = {}
    for i in range(1, nth_key_value+1):
        square_table_dict[i] = i*i
    logging.info(f"Square table dictionary(n={nth_key_value}): {square_table_dict}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    square_dict(1)