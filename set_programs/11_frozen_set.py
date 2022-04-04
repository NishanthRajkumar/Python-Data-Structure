'''
    @Author: Nishanth
    @Date: 04-04-2022 15:16:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 15:16:00
    @Title: Explore use of frozenset
'''
import sys
import logging

def frozenset_uses(items_for_frozenset: list|dict):
    """
        Description:
            shows use of frozenset
        
        Parameter:
            items_for_frozenset: A list of items to convert to frozen set
        
        Return:
            None
    """
    if type(items_for_frozenset) is list:
        logging.info(f"The list of items: {items_for_frozenset}")
        frozen_set = frozenset(items_for_frozenset)
        logging.info(f"The frozen set from list: {frozen_set}")
    elif type(items_for_frozenset) is dict:
        logging.info(f"The dictionary of items: {items_for_frozenset}")
        frozen_set = frozenset(items_for_frozenset)
        logging.info(f"The frozen set from dict: {frozen_set}")
    else:
        logging.error("The iterable for frozen set must be list or dict")
        return None
    logging.info("Attempting to modify frozen set")
    try:
        logging.info("Attempting to change first value to 11 in frozen set")
        frozen_set[0] = 11
    except TypeError:
        logging.exception("Failed to modify frozen set")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = [1, 2, 5, 78, 23, 3, 450, 48, 97, 98]
    sample_dict = {'1st': 1234, '2nd': 'qwer', 3: 5+7j}
    frozenset_uses(sample_list)
    frozenset_uses(sample_dict)