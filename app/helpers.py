#my utility functions 
from datetime import datetime

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        print("Error in date format")
        return False
    
def validate_string(text):
#string should not be empty 
    if not text or not text.strip():
        #checking also for whitespaces 
        print("Error:Input cannot be Empty")
        return False
    return True

def get_user_input(prompt, validator=None):
    #Get and validate user input
    while True:
        value = input(prompt)
        if validator is None or validator(value):
            return value
        print("Please try again.")