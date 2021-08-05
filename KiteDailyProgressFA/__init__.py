import logging
import sys
import os
import datetime
import azure.functions as func

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

from KiteDailyProgress import get_holdings, play_with_holding
from Login import login_user
from MongoDB import insert_many_into_collection


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
    enctoken = login_user()
    holdings = get_holdings(enctoken)
    play_with_holding(holdings)
    insert_many_into_collection(holdings["data"],'KiteDailyProgress')
