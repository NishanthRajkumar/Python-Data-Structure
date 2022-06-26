'''
    @Author: Nishanth
    @Date: 05-04-2022 11:43:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 11:43:00
    @Title: Unpack a tuple in several variables
'''
import sys
import logging

def unpack_tuple():
    """
        Description:
            Unpack a tuple in several variables
        
        Parameter:
            None
        
        Return:
            None
    """
    car_tuple = ('Xuv700', 'Petrol', 'Black')
    logging.info(f"Car details tuple: {car_tuple}")
    car_model, fuel_type, colour = car_tuple
    logging.info(f"After unpacking:\nCar model: {car_model}\nFuel type: {fuel_type}\nColour: {colour}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    unpack_tuple()