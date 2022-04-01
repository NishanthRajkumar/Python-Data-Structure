'''
    @Author: Nishanth
    @Date: 01-04-2022 22:13:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 22:13:00
    @Title: Sort a Dictionary by value
'''
import logging
import sys

def sort_by_value(dictionary_to_sort: dict, descending: bool = False):
    """
        Description:
            Sort the given dictionary by value
        
        Parameter:
            Accepts a dictionary as parameter
        
        Return:
            None
    """
    sorted_dictionary = {key: val for key, val in sorted(dictionary_to_sort.items(), key= lambda item: item[1], reverse=descending)}
    logging.info(f"Orginal Dictionary: {dictionary_to_sort}")
    logging.info(f"Sorted by Value(Descending={descending}): {sorted_dictionary}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dictionary = {1: 230, 2: 350, 3: 130}
    sort_by_value(sample_dictionary)
    sort_by_value(sample_dictionary, True)