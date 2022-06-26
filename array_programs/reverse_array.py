'''
    @Author: Nishanth
    @Date: 01-04-2022 20:37:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 20:37:00
    @Title: Reverse the array items
'''
from array import array
import logging
import sys

def reverse_array(homogenous_list: list, list_type: str):
    """
        Description:
            Reverses the order of the items in the array
        
        Parameter:
            homogenous_list: A list of items that are of same type
            list_type: type of element in list. accepted values: 'int', 'unicode', 'float'
        
        Return:
            None
    """
    list_type = list_type.casefold()
    array_types = {'int': 'i', 'unicode': 'u', 'float': 'd'}
    if list_type not in array_types.keys():
        logging.error("Invalid list type!")
        return None
    try:
        array_from_list = array(array_types[list_type], homogenous_list)
        array_from_list.reverse()
        logging.info("Reversed Array:")
        for i in range(len(array_from_list)):
            logging.info(f"Array[{i}]: {array_from_list[i]}")
    except TypeError:
        logging.exception(f"1 or more items in the list did not match the list type: {list_type}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"array_programs\array.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    reverse_array([23, 4, 5, 7, 120], 'int')