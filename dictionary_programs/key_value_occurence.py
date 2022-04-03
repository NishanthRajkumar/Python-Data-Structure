'''
    @Author: Nishanth
    @Date: 03-04-2022 11:14:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 11:14:00
    @Title: Count occurence of key, value pair in list of dictionaries
'''
import logging
import sys

def table_format(list_of_dicts: list[dict], key, value):
    """
        Description:
            Count occurence of key, value pair in list of dictionaries
        
        Parameter:
            list_of_dicts: List of dictionaries to analyse and search
            key: key to match
            value: value to match
        
        Return:
            None
    """
    key_value_count = 0
    for dictionary_data in list_of_dicts:
        if dictionary_data.get(key) == value:
            key_value_count += 1
    logging.info(f"({key}: {value}) occurs {key_value_count} times in {list_of_dicts}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dict_list = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    table_format(sample_dict_list, 'success', True)