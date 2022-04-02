'''
    @Author: Nishanth
    @Date: 02-04-2022 11:16:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 11:16:00
    @Title: Count of occurence of distinct letters in string
'''
import logging
import sys

def unique_values(string_to_evaluate: str):
    """
        Description:
            Counts the occurence of distinct letters in string
        
        Parameter:
            accepts the string to count the letters
        
        Return:
            None
    """
    if type(string_to_evaluate) is not str:
        logging.error("The input parameter must be string")
        return None
    letter_count = {}
    for character in string_to_evaluate:
        if character in letter_count.keys():
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    logging.info(f"Letter count for '{string_to_evaluate}': {letter_count}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    unique_values('w3resource')