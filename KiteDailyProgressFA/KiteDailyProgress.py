import requests
import json
from Login import login_user
from MongoDB import insert_many_into_collection
from datetime import datetime
import Constants


def get_holdings(enctoken):
    url = "https://kite.zerodha.com/oms/portfolio/holdings"
    payload = {}
    headers = {
        'authorization': 'enctoken {0}'.format(enctoken)
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)


def play_with_holding(holdings):
    try:
        if(holdings["status"] == "success"):
            data = holdings["data"]
            day_pnl = 0
            total_invested = 0
            total_pnl = 0
            current_value = 0
            for val in data:
                quantity = float(val["quantity"]) +  float(val["t1_quantity"])
                day_change = float(val["day_change"]) * quantity
                average_price = float(val["average_price"]) * quantity
                pnl = float(val["pnl"])
                day_pnl += day_change
                total_invested += average_price
                total_pnl += pnl
                print("Tradingsymbol = ", val["tradingsymbol"].ljust(15, ' '), "Change", round(day_change, 2))
                val["total_day_change"] =  day_change
                val["total_average_price"] =  average_price
                val["inserted_at"] = datetime.now()

            current_value = total_pnl + total_invested
            kite_daily_overview = {
                "day_pnl": day_pnl,
                "total_pnl": total_pnl,
                "total_invested": total_invested,
                "current_value": current_value,
                "inserted_at": datetime.now()
            }
            print(kite_daily_overview)

            # Insert data into db
            # Insert the data of overall progress
            insert_many_into_collection([kite_daily_overview], Constants.KiteDailyOverviewCollectionName)
            # Insert the data of all the holdings
            insert_many_into_collection(holdings["data"], Constants.KiteDailyProgressCollectionName)
    except Exception as e:
        print(e)


def kite_daily_progress():
    enctoken = login_user()
    holdings = get_holdings(enctoken)
    play_with_holding(holdings)


if __name__ == "__main__":
    kite_daily_progress()
