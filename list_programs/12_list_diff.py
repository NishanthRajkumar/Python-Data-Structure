'''
    @Author: Nishanth
    @Date: 05-04-2022 07:46:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 07:46:00
    @Title: Get difference between 2 lists
'''
import sys
import logging

def list_difference(list1: list, list2: list):
    """
        Description:
            Gets difference between 2 lists
        
        Parameter:
            list1, list2: The 2 lists to find difference for
        
        Return:
            None
    """
    list_diff = list(set(list1).symmetric_difference(set(list2)))
    logging.info(f"\nList 1: {list1}\nList 2: {list2}")
    logging.info(f"List difference: {list_diff}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list1 = ['powershell', 'gitbash', 'terminal']
    sample_list2 = ['git', 'gitbash', 'github']
    list_difference(sample_list1, sample_list2)