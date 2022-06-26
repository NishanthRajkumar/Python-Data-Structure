'''
    @Author: Nishanth
    @Date: 05-04-2022 14:15:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:15:00
    @Title: Sort comma separated words alphanumerically
'''
import sys
import logging

def sort_comma_sep_text(comma_sep_text: str):
    """
        Description:
            Sorts comma separated words alphanumerically
        
        Parameter:
            comma_sep_text: comma separated text
        
        Return:
            None
    """
    logging.info(f"Original text: {comma_sep_text}")
    list_of_words = comma_sep_text.split(',')
    logging.info(f"List of words: {list_of_words}")
    list_of_words.sort()
    logging.info(f"Sorted words: {list_of_words}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sort_comma_sep_text('red, white, black, red, green, black')