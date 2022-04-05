'''
    @Author: Nishanth
    @Date: 05-04-2022 14:50:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:50:00
    @Title: Lowers n characters in a string
'''
import sys
import logging

def lower_n_char(text: str):
    """
        Description:
            Lowers n characters in a string
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    logging.info(f"Original text: {text}")
    try:
        no_of_char_to_lower = int(input("Enter no of char to lower the case: "))
        if no_of_char_to_lower > len(text):
            logging.error("Input value must be less than text length")
            return None
    except:
        logging.error("Expected int input")
    text = text[:no_of_char_to_lower-1].lower() + text[no_of_char_to_lower-1:]
    logging.info(f"Updated text: {text}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    lower_n_char("SoMe raNdoM TExt")