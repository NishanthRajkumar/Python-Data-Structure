'''
    @Author: Nishanth
    @Date: 03-04-2022 13:05:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 13:05:00
    @Title: create a set
'''
import sys
import logging

def create_set(data = None) -> set:
    """
        Description:
            Creates a set from given data. if data is not given, then creates empty set
        
        Parameter:
            data: the data from which to create set from. Default: None
        
        Return:
            returns a set
    """
    return set(data)

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    created_set = create_set(['asd', 'qwe', 'fgh', 'rty'])
    logging.info(f"Created set: {created_set}")