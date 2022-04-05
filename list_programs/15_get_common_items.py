'''
    @Author: Nishanth
    @Date: 05-04-2022 09:06:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 09:06:00
    @Title: Get common items among 2 lists
'''
import sys
import logging

def list_common_items(list1: list, list2: list):
    """
        Description:
            Gets common items among 2 lists
        
        Parameter:
            list1, list2: The 2 lists to find common items
        
        Return:
            None
    """
    list_common = list(set(list1).intersection(set(list2)))
    logging.info(f"\nList 1: {list1}\nList 2: {list2}")
    logging.info(f"List of common items: {list_common}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list1 = ['powershell', 'gitbash', 'terminal']
    sample_list2 = ['git', 'gitbash', 'github', 'terminal']
    list_common_items(sample_list1, sample_list2)