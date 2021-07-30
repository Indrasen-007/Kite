import requests
import json
from Login import login_user
from db import *

def get_holdings(enctoken):
    url = "https://kite.zerodha.com/oms/portfolio/holdings"
    payload = {}
    headers = {
    'authorization': 'enctoken {0}'.format(enctoken)
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

def play_with_holding(holdings):
    if(holdings["status"] == "success"):
        data = holdings["data"]
        total = 0
        for val in data:
            insert_into_daily_progress_table(val)
            daily_change = float(val["day_change"])*float(val["quantity"])
            total += daily_change
            print("Tradingsymbol = ",val["tradingsymbol"].ljust(15,' '), "Change", round(daily_change,2))

        print("Total profit/loss : ",round(total,2))
        insert_into_daily_total_progress_table(total)
        # print(data)
    
def main():
    enctoken = login_user()
    holdings = get_holdings(enctoken)
### this is one time activity
    # get_or_create_table_daily_progress_table()
    # get_or_create_table_total_daily_progress_table()
### end
    play_with_holding(holdings)
    
if __name__ == "__main__":
    main()