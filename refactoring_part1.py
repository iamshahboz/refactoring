# Refactoring is the way to make the code cleaner and more pythonic
# This is our initial function

# from datetime import date, timedelta 

def getStartEndDate(q_start_date, q_end_date):
    if q_start_date:
        start_date = q_start_date
    else:
        start_date = str(date.today()- timedelta(days=7))

    if q_end_date:
        end_date = q_end_date 
    else:
        end_date = str(date.today())

    return start_date, end_date 

print(getStartEndDate())

# how we can refactor this code this way
from typing import Optional 
from datetime import date, timedelta

def get_start_and_end_date(
        q_start_date: Optional[str] = None,
        q_end_date: Optional[str] = None 
)->(str, str):
    last_week = date.today()- timedelta(days=7)
    start_date = q_start_date if q_start_date else str(last_week) # or str(last_week)
    end_date = q_end_date if q_end_date else str(date.today()) # or str(date.today())

    return start_date, end_date

print(get_start_and_end_date())


    
    



