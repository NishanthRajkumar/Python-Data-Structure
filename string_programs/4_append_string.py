'''
    @Author: Nishanth
    @Date: 05-04-2022 13:27:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 13:27:00
    @Title: Add 'ing' at the end of a given string (length should be at least 3). 
            If the given string already ends with 'ing' then add 'ly' instead
'''
import sys
import logging

def add_ing_ly(text: str):
    """
        Description:
            Adds 'ing' to text, if length > 3. if text ends with 'ing' then adds 'ly'
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    logging.info(f"Original text: {text}")
    if len(text) > 2:
        if text[-3:] == 'ing':
            text = text + 'ly'
        else:
            text = text + 'ing'
    logging.info(f"Updated text: {text}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    add_ing_ly("stay")
    add_ing_ly("calming")