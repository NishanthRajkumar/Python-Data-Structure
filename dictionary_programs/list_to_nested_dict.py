'''
    @Author: Nishanth
    @Date: 03-04-2022 11:30:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 11:30:00
    @Title: Convert list to nested dictionary
'''
import logging
import sys

def list_to_nested_dict(list_data: list) -> dict:
    """
        Description:
            Convert list to nested dictionary
        
        Parameter:
            list_data: the list to be converted to nested dictionary
        
        Return:
            dictionary
    """
    if len(list_data) < 2:
        logging.error("List must contain 2 or more items")
        return None
    if len(list_data) == 2:
        return {list_data[0]: list_data[1]}
    return {list_data[0]: list_to_nested_dict(list_data[1:])}

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = ['abc', 'xyz', 'aba', '1221']
    nested_dict = list_to_nested_dict(sample_list)
    logging.info(f"Nested dict: {nested_dict}")