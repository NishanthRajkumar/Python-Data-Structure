'''
    @Author: Nishanth
    @Date: 05-04-2022 08:52:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 08:52:00
    @Title: Check if 2 lists are circularly identical
'''
import sys
import logging

def chk_circular(list1: list, list2: list):
    """
        Description:
            Checks if 2 lists are circularly identical
        
        Parameter:
            list1, list2: The 2 lists to check if circularly identical
        
        Return:
            True if circularly identical, else False
    """
    if len(list1) != len(list2):
        return False
    double_list = list1 + list1
    for i in range(len(list1)):
        if list2 == double_list[i: i + len(list2)]:
            return True
    return False

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list1 = ['powershell', 'gitbash', 'terminal']
    sample_list2 = ['gitbash', 'terminal', 'powershell']
    logging.info(f"\nList 1: {sample_list1}\nList 2: {sample_list2}")
    logging.info(f"Circular Identical? {chk_circular(sample_list1, sample_list2)}")