'''
    @Author: Nishanth
    @Date: 05-04-2022 13:08:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 13:08:00
    @Title: Count of occurence of distinct letters in string
'''
import sys
import logging

def char_count(text: str):
    """
        Description:
            Counts the occurence of distinct letters in string
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    if type(text) is not str:
        logging.error("The input parameter must be string")
        return None
    letter_count = {}
    for character in text:
        if character in letter_count.keys():
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    logging.info(f"Letter count for '{text}':\n{letter_count}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    char_count("Visual Studio Code")