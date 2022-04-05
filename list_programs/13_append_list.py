'''
    @Author: Nishanth
    @Date: 05-04-2022 07:46:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 07:46:00
    @Title: Append 1 list to another list
'''
import sys
import logging

def list_append(list1: list, list2: list):
    """
        Description:
            Appends 1 list to another list
        
        Parameter:
            list1, list2: The 2 lists to find append
        
        Return:
            None
    """
    new_list = list1 + list2
    logging.info(f"\nList 1: {list1}\nList 2: {list2}\nNew List: {new_list}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list1 = ['powershell', 'gitbash', 'terminal']
    sample_list2 = ['git', 'gitbash', 'github']
    list_append(sample_list1, sample_list2)