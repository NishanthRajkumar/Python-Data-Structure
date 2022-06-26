'''
    @Author: Nishanth
    @Date: 05-04-2022 13:08:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 13:08:00
    @Title: Replace occurrences of a string's first char to '$'
'''
import sys
import logging

def replace_1stchar(text: str):
    """
        Description:
            Replaces occurrences of a string's first char to '$'
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    if len(text) < 2:
        logging.error("Length of text must > 1")
        return None
    updated_text = text[0] + text[1:].replace(text[0], '$')
    logging.info(f"Original text: {text}")
    logging.info(f"Updated text: {updated_text}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    replace_1stchar("summer solstice")