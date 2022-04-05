'''
    @Author: Nishanth
    @Date: 05-04-2022 07:46:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 07:46:00
    @Title: Check if 2 lists have common items
'''
import sys
import logging

def chk_common_item(list1: list, list2: list):
    """
        Description:
            Checks if 2 lists have common items
        
        Parameter:
            list1: first list
            list2: 2nd list
        
        Return:
            True if if common items present, else False
    """
    for item in list1:
        if item in list2:
            return True
    return False

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list1 = ['shell', 'powershell', 'gitbash', 'terminal', 'cmd']
    sample_list2 = ['powershell7', 'gitbash', 'terminal', 'cmd prompt']
    logging.info(f"List 1: {sample_list1}\nList 2: {sample_list2}")
    logging.info(f"Any common items? {chk_common_item(sample_list1, sample_list2)}")