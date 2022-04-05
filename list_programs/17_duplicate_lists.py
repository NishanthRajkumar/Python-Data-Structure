'''
    @Author: Nishanth
    @Date: 05-04-2022 08:52:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 08:52:00
    @Title: Remove duplicate lists
'''
import sys
import logging

def remove_duplicate_lists(list_of_lists: list[list]):
    """
        Description:
            Remove duplicate lists
        
        Parameter:
            list_of_lists: A list of list type items
        
        Return:
            None
    """
    logging.info(f"Original list: {list_of_lists}")
    distinct_list_of_lists = []
    for item in list_of_lists:
        if type(item) is not list:
            logging.error("The list must be a list of lists")
            return None
        if item not in distinct_list_of_lists:
            distinct_list_of_lists.append(item)
    logging.info(f"Distinct list: {distinct_list_of_lists}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    remove_duplicate_lists(sample_list)