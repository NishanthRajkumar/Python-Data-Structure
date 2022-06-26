'''
    @Author: Nishanth
    @Date: 01-04-2022 20:05:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 20:05:00
    @Title: Create an array of 5 integers and display the array items
'''
import array as arr
import logging
import sys

def display_int_array(list_of_integers: list):
    """
        Description:
            create an array of 5 integers and display the array items
        
        Parameter:
            List of integer values
        
        Return:
            None
    """
    if len(list_of_integers) != 5:
        logging.warning("No of integers must be 5")
        return None
    try:
        int_array = arr.array('i', list_of_integers)
        for i in range(5):
            logging.info(f"int Array[{i}]: {int_array[i]}")
    except TypeError:
        logging.exception("The list had non integer type elements")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"array_programs\array.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    display_int_array([23, 4, 5, 7, 120])