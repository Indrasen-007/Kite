import logging
import sys
import os
import datetime
import azure.functions as func

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

from KiteDailyProgress import kite_daily_progress

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
    kite_daily_progress()
