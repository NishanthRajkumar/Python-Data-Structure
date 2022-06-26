'''
    @Author: Nishanth
    @Date: 04-04-2022 16:20:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 16:20:00
    @Title: Multiplication of items in list
'''
import sys
import logging

def mul_of_items(list_of_items: list):
    """
        Description:
            Computes the multiplication of items in the list
        
        Parameter:
            list_of_items: a list. The list items must be of numeric type
        
        Return:
            None
    """
    logging.info(f"The list is {list_of_items}")
    if type(list_of_items[0]) not in [int, float, complex]:
        logging.error("Not all list items are numeric")
        return None
    item_sum = list_of_items[0]
    for item in list_of_items[1:]:
            if type(item) not in [int, float, complex]:
                logging.error("Not all list items are numeric")
                return None
            item_sum *= item
    logging.info(f"The multiplication of list items: {item_sum}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    mul_of_items([23, 4.6, 3.5+8j, 25])
    mul_of_items(['qwe', 'rty', 'pass', 'word'])
    mul_of_items(['qwe', 'rty', 'pass', 3])