'''
    @Author: Nishanth
    @Date: 04-04-2022 18:13:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 18:13:00
    @Title: Count no of item in list that are string type and length >= 2
'''
import sys
import logging

def count_string(list_of_items: list):
    """
        Description:
            Counts no of item in list that are string type and length >= 2
        
        Parameter:
            list_of_items: a list
        
        Return:
            None
    """
    string_count = 0
    logging.info(f"The list: {list_of_items}")
    for item in list_of_items:
        if (type(item) is str) and (len(item) > 1) and (item[0] == item[-1]):
            string_count += 1
    logging.info(f"String count(len > 2 & starts and ends with same character): {string_count}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    count_string(['abc', 'xyz', 'aba', '1221'])
    count_string(['abcda', 'a', 'xyz', 'd', 45, 'aba', '1221'])