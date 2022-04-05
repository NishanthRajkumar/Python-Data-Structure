'''
    @Author: Nishanth
    @Date: 05-04-2022 10:35:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 10:35:00
    @Title: Split a list based on first character of word
'''
import sys
import logging

def split_words_in_list(list_data: list):
    """
        Description:
            Splits a list based on first character of word
        
        Parameter:
            list_data: list of data
        
        Return:
            None
    """
    logging.info(f"Original list: {list_data}")
    for i in range(len(list_data)):
        if type(list_data[i]) is str and len(list_data[i]) > 1:
            list_data[i] = [list_data[i][0], list_data[i][1:]]
    logging.info(f"Updated list: {list_data}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = ['Red', 'Green', 'White', 234, 3+8j, 'Black', 'Pink', 'Yellow']
    split_words_in_list(sample_list)