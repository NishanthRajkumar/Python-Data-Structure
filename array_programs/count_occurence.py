'''
    @Author: Nishanth
    @Date: 01-04-2022 21:22:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 21:22:00
    @Title: Count the occurence of specififed item in array
'''
from array import array
import logging
import sys

def count_occurence(homogenous_list: list, list_type: str, array_element):
    """
        Description:
            Counts the occurence of the element in array
        
        Parameter:
            homogenous_list: A list of items that are of same type
            list_type: type of element in list. accepted values: 'int', 'unicode', 'float'
            array_element: element in array, to check count of occurence
        
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
        count = array_from_list.count(array_element)
        logging.info(f"Count of {array_element} in {array_from_list}: {count}")
    except TypeError:
        logging.exception(f"1 or more items in the list did not match the list type: {list_type}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"array_programs\array.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    count_occurence([23, 4, 5, 7, 120, 4, 78, 4], 'int', 4)