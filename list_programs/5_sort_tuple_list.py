'''
    @Author: Nishanth
    @Date: 04-04-2022 19:21:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 19:21:00
    @Title: Sort the list of tuples in increasing order
'''
import sys
import logging

def sort_tuple_list(list_of_tuples: list[tuple]):
    """
        Description:
            Sorts the list of tuples in increasing order
        
        Parameter:
            list_of_tuples: a list of tuples
        
        Return:
            None
    """
    for item in list_of_tuples:
        if type(item) is not tuple:
            logging.error("Items in list must be tuple")
    sorted_list = [tuple_item for tuple_item in sorted(list_of_tuples, key= lambda item: item[-1])]
    logging.info(f"Original List: {list_of_tuples}")
    logging.info(f"Sorted List: {sorted_list}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sort_tuple_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    sort_tuple_list([(2, 5, 1), (1, 2, 7), (4, 9, 4), (2, 3), (2, 1)])